---
title: 'Pfsense + UDM + VLANs: The perfect home network'
author: Alevsk
type: post
date: 2022-05-31T06:56:29+00:00
url: /2022/05/pfsense-udm-vlans-the-perfect-home-network/
yarpp_meta:
  - 'a:1:{s:27:"yarpp_display_for_this_post";i:1;}'
categories:
  - Ethical Hacking
  - Linux
  - Networking
  - IT News
  - Technology
  - Tutorials
tags:
  - Linux
  - networking
  - pfsense
  - software libre
  - Solutions
  - Technology
  - Tutorials

---
A couple weeks ago I did a mayor reconfiguration on my home network, I migrated from a single flat insecure network in where any device was able to talk to any other to a more secure design in where the network is segmented (IoT devices, guests, home lab, etc) and where I control who has access to what resources via firewall rules and other tools.

My original home network consisted of a single Google Wifi router, if you are interested the device it's limited but will get the job done. However I wanted to learn more about networking and in particular how to configure a couple of monitoring tools, network packet inspection, security, firewall rules, etc. So I started looking at networking appliances that will let me do more advanced configurations and I quickly found about [Pfsense (Protectli Vault)][1] so I got one.

Additionally, as a birthday gift from @perrohunter, I got [The Dream Machine][2] from Ubiquiti (usually you will use one or the other) so I had two routers now. 

I had to integrate them together but I faced a couple of issues during the process to the point where I got locked out from the network and I had to reset the devices multiple times, either the Pfsense or the UDM would work but not both of them at the same time but after some time it's finally working so I decided to document the process in case it helps someone in the future.

# Designing the network

The main goal was to have a clear separation between IoT devices, guest devices and my home devices so i came out with this design.

![](https://lh4.googleusercontent.com/xrjWuy17uzYlf-koSm4_mhBSNmeug56vAy8YudgMj3qGo1rYcVGlj9Wz6ljz3VpZ1loHzUPW9v5qkVckN4dn3E3lXS3ztQUhEyVz6Z04pNThbD8kS1PVo1NTrEWcmATg22YOJAR7Z2WqoAPN)

_Disclaimer: I'm a security software engineer but I know a thing or two about networking, if you see something wrong or do you think this design can be improved in any way please let me know._

As you can see, I'm putting the Pfsense at the edge of the network so I have full control over the traffic. I'm using the UDM as an access point only because most of the routing and DNS resolution will be done by Pfsense. The home network consists of 3 VLANs.

## IoT network VLAN 30

All my smart lights, roomba, smart locks, cameras will be here, these devices cannot communicate to the other networks or connect to the Internet. Only wireless devices will connect to this network.

## Guests network VLAN 50

Occasionally I get visitors at my place, guests can connect to this network and enjoy access to the Internet however devices here will not be able to talk to devices on the IoT nor the LAN network. TODO: I want to put some rules in place so guests' devices are fully isolated from each other. Only wireless devices will connect to this network.

## LAN 

This is the main network and it's a combination between wired and wireless devices, my work stations, laptops, mobile devices, home servers, smart tv, gaming consoles, etc. These are devices that I trust and most of them have static IPs and dns names.

# Setup

I'm not going to explain in detail how to do the initial configuration for the Pfsense or the UDM, there are thousands of videos and tutorials that can guide you through that, instead I'll focus on the parts I struggled the most and the “hacks" I applied to make this work.

## Pfsense setup

These devices will usually come with two ports, **WAN** and **LAN**. I had to connect the Ethernet cable from the modem to the WAN port (also called an interface) and that will be enough for the device to talk to the internet in most cases. After that, during the initial configuration Pfsense asked me to configure the LAN interface, there I chose the network IP, IP range, etc In my case I selected **10.13.37.1/24** as my network IP range.
![](https://lh5.googleusercontent.com/cvCOPaecByLXtGdPm7xuoRWP6Eeym9L_unq-QNzL_0JUQgwSlG_TkMUDEWpHoukawS1BjjPRu4DaUW0iPJ2PC6xDiaNlJTf84lZ6r8Vkiw0qOKBlSNYurFaxFjTyX62d9n1Nj3_GbqiEtBDY) 
You can tweak and do some more advanced configurations under Services > DHCP Server > LAN

DHCP got configured automatically for this interface so I didn't worry about it.

![](https://lh4.googleusercontent.com/BJRoZR5B3MFCCg0rKbdpCy1sav6vqGKIP9UWtOZccWh73J2SbAzZnNasZG0qLoShN7q_seOLtqQ9WF1yJYMoBoK40_46jeI-pfEG6QlLoSihd0yyS2xzCxBj_RCJJzxJE3ditoFzqxdNeLJW) 

After that I grabbed another Ethernet cable and connected it into the Pfsense LAN port and the UDM WAN port.
![](https://lh4.googleusercontent.com/A8GoVNwDrzTtKluQHR3Y8yK68tlBDk2ygzenGbFt0Ju5hdX1wWZLBEA6qO2msIxNrXpoyXOj56i4AT9eSsAikEOwM_tImcCgUKt0lWQ88SszThkwfnlmCRzo5UeXmsGTCut97YwdcFObJcIZ)  

## The Dream Machine (UDM) setup

Here is where the issues begin, I connected the Ethernet cable to the UDM, the app guided my through the initial configuration, then I created the initial Wireless network and everything seemed to work fine however after looking at Status > DHCP Leases on my Pfsense I could not see any of my wireless devices, that was weird.

I logged in into the Dream Router management console and I could see my wireless network, the default network and the wan interface. I also could see all my connected devices, however the assigned IP addresses were in the **192.168.1.1/24** range not the **10.13.37.1/24**. So I had some idea about what was happening, UDM had its own DHCP server and was assigning the IP addresses itself.

I start trying many different things, some of them were:

  * Disabling DHCP in the default network of the UDM didn't work.
  * Changing the network range in the default network of the UDM to **10.13.37.1/24** didn't work, UDM was complaining that the range conflicts with the IP assigned to it (**10.13.37.2**).
  * Created an additional network on the range I wanted **10.13.37.1/24** didn't work, devices from here were not able to see the Pfsense.

I tried many more things and after a couple weekends of trial and error I found the winning combination of steps, this is probably the most important part of this article.

  * Disconnect the Ethernet cable from the UDM WAN port, this cause the UDM to lose the IP assigned by the Pfsense
  * Change the default network configuration in the UDM to use the **10.13.37.3/24** network, this network will overlap with the **10.13.37.1/24** network in Pfsense but it's ok, also set DHCP Mode to none.
![](https://lh4.googleusercontent.com/Wbnm0UxB-cBoCm6HQysgB9ueARso3i28STCTlBF0aEEFDCrp4t0MTncV0HtzFknkguq07pHw9aaL_aR_6Dsx3J1lGnMHrHEcRgkM-rENqtyfY-g0zWswjCf7zRO_oHdjN0ok-kslC-2PoApP)  

  * In the UDM go to Internet > default WAN and select manual configuration, here I'm setting the primary DNS server as **10.13.37.1** (Pfsense) and IPv4 configuration has to be as follow
![](https://lh3.googleusercontent.com/5QxQ0r1DK5MxG6EQJUmuCQFvrl9LWlb0M3udCy_3YaEyr7TdX0R0wP0mShajK8_OYnJDH74_c9LTKDKNh--0DwDFWeWcBJOVDIw0AaliRuyYwU3yj46B3uCqQKkCEGe6uz1ySQY34CRWBYVt)  

Here I'm telling UDM the next hop will be at 10.13.37.1 (Pfsense), also I want the UDM to use the static IP **10.13.37.2**, and the subnet mask will be **255.255.255.248** which ended being the “hack" that allow me to use the **10.13.37.x** range on the default network
![](https://lh3.googleusercontent.com/9Y3-jWQfObIpdlfsdukgSA7RV0VB5uWSEJ9s7ZpV5u2Cb00YJvj2NFnI29R1vqwcdxRnhcWvL4DHJCRtDzS6zPm3XZnAOQ9AnEPVqIY3YMD44WsV4iu2mcSKm25rocoZOSjjjy90vWiRSHAa)  

Finally plug the Ethernet cable again into the UDM but this time into any of the LAN ports not the WAN (the little world icon), avoid the WAN port seriously!.
![](https://lh4.googleusercontent.com/g8aMbKS4ZHwoYpkzSA6VxUM5mwYWjNMFqLB4aHJ3_P8lhI2dQh7UeiMSmaD5hbY8d7B8ZW3H4H6nXnVsAdswJP5abbAm2oLXD3IHgrofIpBCbe8-0Z4uYDCeeW-QHteCAMbId5ObJgxfaghQ)  

The reason why I want the default network in the UDM to be an overlap of the **10.13.37.1/24** network in the Pfsense was because otherwise I would lose access to the UDM management console, I'm still trying to figure out why is that but my guess is even if the UDM is accessible from the Pfsense network on **10.13.37.2** IP address when I try to go to there (if the default network range is configured to be **192.168.1.1** on UDM) it won't let me in because of some validation on UDM, to avoid this I ended creating a dedicated wireless network just to recover access (after getting locked out multiple times).

Using the above configuration my devices in the **10.13.37.1/24** range are able to talk to **Pfsense** (10.13.37.1) and also the **UDM** (10.13.37.3) and finally I'm able to see and control my devices from the Pfsense as well.
![](https://lh6.googleusercontent.com/TlTfTr_H86SosjilOBHr4kjUFxafRxCOgHAhy2Zvn2lrEp-DXK4k4I-zO4b_GTSJz9lC8e_fkRSRpkylYnDkhk0mVAw1qDywUtk6Ab8HqXlIhCzSutJnxMmvYiptDlaI8bsvRwNkdW-94luo)  

# VLANs

## Network interfaces

The main network is working fine now what? I started creating additional VLANs and firewall rules for the guests and the IoT networks. On the Pfsense I went to  **Interfaces > Assignments > VLANs** and added the two VLANs. It's very important to select **LAN** as the parent interface because all the traffic is going to come from that port.
![](https://lh5.googleusercontent.com/ktmYEBNNiGindeT_GiCprSgzGnJd0C8qNag_CH_oxj6F8ocxtqGtUWcKDvE_lnWj_uJWy0hdMdWFFgV0zGPdlYo3TRWbjy8BCGakSzOxLsgkYnrlu8vgjZmc2rKhz6-yK1ekJxLoSXilceS8)  ![](https://lh3.googleusercontent.com/tZxZjZGQZXgjHd52YTu7zJf5wgSQ1BdqttckOCY6wlK2_44ueNKIru9IXa-11PHGh8ucMCgE7I0llYoxhgkqawMqx1oVoQdcuphk7Pl5K-_9HpvDfw5lWitIyiv9xAo51XcYDs7Zz3L7BbuA) 

For no particular reason I chose **tag 30** for the IoT VLAN and **tag 50** for the guest VLAN, don't forget to assign the new VLANs to the LAN interface and create the new networks.
![](https://lh4.googleusercontent.com/MZFuTnAPEsAw2GOIMNePahbW2xnSOj7kgw9cDJ_aclSoPzgFPEwK19SOG1EINBNlilyZtF8J5up105YPkisV-yQFEBxDwKjTIaG4B9-WUwCEWq09f4ZKqxZw-z-LO5uog9JmUESS06F4ZNeI)  

To be consistent I decided the guests network range will be **10.13.50.1/24** and the IoT will follow **10.13.30.1/24**
![](https://lh6.googleusercontent.com/3QGWGA7DEIQ-bnn5kdGsNsIh04N3MuO78UdTaNIYtodRKlo5YsMnFKT1vVYQvm1_5J6w3peGBhjjHU25HRHv23XH32Hp4yjTmnH6UCdO3H1rHlvW7aLpkogFfCXjxQDO4cl7UAY3iw_RZSHM)  ![](https://lh5.googleusercontent.com/qyqwxRiPkRdT3YmFGT2CsUqqbl63jkwNxZrikGpG09-RA0Qx_Hy6jlV3ItwovtYzwNqKHQ154CgCuTruUTsuW0Pq3l2OqsFWD90gyr7jN5xuOEb7L4-_EuLxsoIWwa6NpsoJtPE2oX0axyfo) 

## DHCP Server

Now it was time to configure the DHCP server for the new networks, I went to Services > DHCP Server and made sure the **enable DHCP** box was checked, additionally I configured the assignable IP range. I did this for both networks.
![](https://lh4.googleusercontent.com/8feGdJNXD9RZ3OsB_9tTHUP-3WOokyfa2nblNfyc31VvV5CQPafMm6Cqa1-PNKXM2a93RbgQG7dF_QQTcrmmu823vvWZ1KXkCEfNRJwvQrrhHvQNa_N4nsVl4Jnl13Ve9d0T-f1WhhXioY9a)  ![](https://lh6.googleusercontent.com/q_ufvqhe5xxTeUEa6wh4Oqga6DBQieitgi0KBMALjxIjkHhTJFKwLCuP1XGzakUdQ-vkUtHQs8JxQMtvcNMC6uNXbCdrpNE7YJn5CJtr4r1UYuJZWVj0gr4YD76IO4jCyYpUY17iV4HR3AHZ) 

## Firewall rules

According to my original design the guests and IoT network have to be isolated from everything else and in particular the IoT devices should not have any access to the Internet, let's do that very quickly by configuring firewall rules on Pfsense (Firewall > Rules).
![](https://lh3.googleusercontent.com/hdrRljWZvB9EVKh4I5avrtPNZ8x26AOmzgC7GECYg92fxpDA-m8Hc-TU_dOmOM6b594aMqWZIP_CPM1ZQhbOh0ONGa6HQOm5vQpXlGbuKkLurVhX2K06DBhYoq3pc2ykt58YLSiuC7E6GHdK)  

These are the rules applied to the IoT_VLAN, here I'm telling Pfsense to block any incoming connection from the IoT network to the home or guests network, I'm also blocking the access to the Pfsense management console itself on port 8443 and 3000. This firewall by default will block any egress traffic in the network and because I'm not saying otherwise this network will not have access to the Internet.
![](https://lh3.googleusercontent.com/zy155hr458M5EW4_qZdeHPn9xuZWNJs1evk7bBeWaK8w9hosvS72rpgnU-sX5_pYzenZcgRA2tzcHx8uZy2uFtg0xPaUVvv8lDTBNjw1u9iwWr89p5MmJ5Wf8N-QoEIGoiQ7Woi2W7-iXj62)  

The guest firewall rules are pretty much the same with the exception that I will allow users to access the Internet (see the last rule).

# The Dream Machine

At this point I was done with the Pfsense part but I was missing one last import piece, configuring the access method for the IoT and guests devices so for that I had to return to the UDM management console and create a couple of wireless and network configurations.

## Guest Network

I created the new guest network configuration, most of the default values were ok but I had to pay special attention to the VLAN ID section, this one has to match to the one I configured on Pfsense (tag 50). Also is very important to set **DHCP Mode** to **None**
![](https://lh6.googleusercontent.com/hxGG7zaRuiCheZSRuHvrTPOxrk7-ZZyMSA3mc2qQCsSXQc9Q4Kg7fmaajdBXo-XPVMDWov5OQ3Wk43qbOYj9NJTl4aVpgiflPqBPW0cw1xNWCQrOtUAKa6NPOubLblHQhEDlhxO7SB_7m_lJ)  

I created the Wifi network and told UDM to use the guest network, all packets will be marked (tag 50) and managed by the guest VLAN.
![](https://lh6.googleusercontent.com/lJ0ifKCMrHhXbM4rd_n74sf6sIGlTfu9g-TxKundj5q1SDgw5Miv_9rxPjMoLAtNlT3NY3J-WJoHyeP6wP_Tyxzm4QOM1IEYlX962_EsPnTYyjPNNSzkDPyQlFv6CVEf4cvVcejMbNZNs27m)  

## IoT Network

I repeated the previous steps but this time for the IoT network, I proceeded to create the network, added the right VLAN (tag 30) and disabled DHCP, then configured the wifi network as well.
![](https://lh4.googleusercontent.com/zZC3gHgNPbLtkDoq8W4mSc_uIlGuK4O-Ejy_VqO4X2g1PL_SOSGuNB1ATYsPvoIA0toGKNj1xmO7HjJh6CPnD9BSRQBYmgdC0B6yi0TLaoMLt-KJz54RwlHkgewZCK5hmMEPhAxlJB-YQBLw)  ![](https://lh5.googleusercontent.com/QKCtWSqJve4fXrxuzQr5B-QfGt01Nv_wrro7EFDhqyAp5wlWIXe1Y8OvUxuEoAs0xDSlwBc6-iH1N8YzSH5TJfaw2G1HY6zYTT3p7DrtSsBBCNtqROWIdBMEkBPISYC9dwlX0L43COeOQqTn) 

# Testing

Once everything is configured the way I wanted I tested by connecting a couple of devices to the IoT network and monitored the traffic with the help of **ntopng** (maybe I will write a blogpost about it in the future), there I confirmed there was not a single request to a remote address.
![](https://lh4.googleusercontent.com/K0gNg5D3-VMnF9uwqeZqeMLPCSnfr8YPE2S5RHUutGRW82e7ukk1iWuSPdVpC3kRLWHYAKPuxKv6eJhLIqv50oBtuRXDWZf-Byg4_FHEoMxBtH1jpLvQP3FMR37ez02epvY7KUIoppFRGjUl)  

# Conclusion

Designing a network is one of the most fun things you can do in IT. The main reason for me to get the Pfsense was because I wanted to learn more about networking and have hands-on experience with several networking and security tools. VLANs, Firewall rules, DHCP, DNS, packet inspection etc are good skills for a security engineer but these are only the tip of the iceberg for a network engineer.

 [1]: https://protectli.com/kb/how-to-install-pfsense-ce-2-4-on-the-vault-2/
 [2]: https://store.ui.com/collections/unifi-network-unifi-os-consoles/products/unifi-dream-machine