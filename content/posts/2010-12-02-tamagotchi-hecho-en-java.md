---
title: Tamagotchi hecho en Java
author: Alevsk
type: post
date: 2010-12-02T05:14:47+00:00
url: /2010/12/tamagotchi-hecho-en-java/
categories:
  - Java
  - Personal
  - Programming
  - Tutorials
tags:
  - Science
  - Hello world
  - Hello World
  - Java
  - Personal
  - Math
  - Programming
  - software libre
  - web

---
[![](/images/tamagotchi_banner.jpg)](http://www.alevsk.com/2010/12/tamagotchi-hecho-en-java/tamagotchi_banner/)

Este es el código del **tamagotchi** (intento de… xD) que nos dejaron hacer como examen final del curso de fundamentos de programación.

Por mil y una razones yo habría preferido hacerlo en **PHP** aprovechando todo el potencial de la **web** pero pues quisieron en Java y no se mucho de ese lenguaje =/ pero ya salio, aquí les dejo el código fuente, cualquier duda  hacérmela saber por este medio :).

[![](/images/tamagotchi.jpg)](http://www.alevsk.com/2010/12/tamagotchi-hecho-en-java/tamagotchi/)
```Python
/*
 * Tamagotchi hecho en Java
 * Noviembre 2010
 * by Alevsk - www.alevsk.com
 */

import java.awt.*;
import java.applet.Applet;
import javax.print.DocFlavor.URL;
import javax.swing.*;
import java.awt.event.*;
import java.util.Random;
import java.io.*;

public class tamagotchi extends Applet implements ActionListener
{
	//Variables del Tamagotchi
	int energia = 100;
	int hambre = 25;
	int felicidad = 25;
	int fuerza = 25;
	int experiencia = 0;
	int nivel = 0;
	int suciedad = 0;
	int puntos = 0;
	float sigNivel;
	String actual = "No esta haciendo nada";
	boolean advirtio = false;

	  //Checkbox checkcm, checkcd, checkweb, checkprog, checkcs, checkbd;
	  JButton comer, entrenar, dormir, bañar, revivir;
	  JTextField energia00, hambre00, felicidad00, fuerza00, experiencia00, nivel00, suciedad00, actual00;
	  JLabel energia11, hambre11, felicidad11, fuerza11, experiencia11, nivel11, suciedad11, imagen11, actual11;
	  //JTextArea result;
	  JPanel acciones,status, imagen, situacion_actual;

	  public void init()
	  {
		  //setName("Demostración del uso de eventos...");
		  setSize(800,600);

		  //botones
		  comer = new JButton("Darle de comer");
		  entrenar = new JButton("Entrenarlo");
		  dormir = new JButton("Descanzar");
		  bañar = new JButton("Bañarlo");
		  revivir = new JButton("Revivir");
		  	revivir.setEnabled(false);

		  //Campos de Texto
		  energia00 = new JTextField(3);
		  	energia00.setEditable(false);
		  	energia00.setText(String.valueOf(energia));

		  hambre00 = new JTextField(3);
		  	hambre00.setEditable(false);
		  	hambre00.setText(String.valueOf(hambre));

		  felicidad00 = new JTextField(3);
		  	felicidad00.setEditable(false);
		  	felicidad00.setText(String.valueOf(felicidad));

		  fuerza00 = new JTextField(3);
		  	fuerza00.setEditable(false);
		  	fuerza00.setText(String.valueOf(fuerza));

		  experiencia00 = new JTextField(3);
		  	experiencia00.setEditable(false);
		  	experiencia00.setText(String.valueOf(experiencia));

		  nivel00 = new JTextField(3);
		  	nivel00.setEditable(false);
		  	nivel00.setText(String.valueOf(nivel));

		  suciedad00 = new JTextField(3);
		  	suciedad00.setEditable(false);
		  	suciedad00.setText(String.valueOf(nivel));

		  actual00 = new JTextField(20);
		  	actual00.setEditable(false);
		  	actual00.setText(String.valueOf(actual));

		  //Lables
		  energia11 = new JLabel("Energia: ");
		  	energia11.setForeground(Color.white);

		  hambre11 = new JLabel("Hambre: ");
		  	hambre11.setForeground(Color.white);

		  felicidad11 = new JLabel("Felicidad: ");
		  	felicidad11.setForeground(Color.white);

		  fuerza11 = new JLabel("Fuerza: ");
			fuerza11.setForeground(Color.white);

		  experiencia11 = new JLabel("Experiencia: ");
		  	experiencia11.setForeground(Color.white);

		  nivel11 = new JLabel("Nivel: ");
		  	nivel11.setForeground(Color.white);

		  suciedad11 = new JLabel("Suciedad: ");
		  	suciedad11.setForeground(Color.white);

		  actual11 = new JLabel("Situacion actual: ");
		  	actual11.setForeground(Color.white);

		  //Imagen del tamagotchi
		  imagen11 = new JLabel();
		  	ImageIcon im=new ImageIcon("../src/nada.gif");
	        imagen11.setIcon(im);
	        //con esto cheque donde se ejecutaba el programa para saber asi el path correcto de las imagenes
	        System.out.println("Directorio ejecucion = " + System.getProperty("user.dir"));

		  //paneles
		  acciones = new JPanel();
		  	acciones.setBackground(Color.black);

		  status = new JPanel();
		  	status.setBackground(Color.BLUE);

		  imagen = new JPanel();
		  //imagen.setBackground(Color.ORANGE);

		  situacion_actual = new JPanel();
		  situacion_actual.setBackground(Color.DARK_GRAY);

		  //agregar elementos a los paneles
		  acciones.add(comer);
		  acciones.add(entrenar);
		  acciones.add(dormir);
		  acciones.add(bañar);
		  acciones.add(revivir);

		  status.add(energia11);
		  status.add(energia00);
		  status.add(hambre11);
		  status.add(hambre00);
		  status.add(fuerza11);
		  status.add(fuerza00);
		  status.add(felicidad11);
		  status.add(felicidad00);
		  status.add(experiencia11);
		  status.add(experiencia00);
		  status.add(nivel11);
		  status.add(nivel00);
		  status.add(suciedad11);
		  status.add(suciedad00);

		  imagen.add(imagen11);

		  situacion_actual.add(actual11);
		  situacion_actual.add(actual00);

		  //mostrar los paneles
		  add(acciones);
		  add(status);
		  add(imagen);
		  add(situacion_actual);

	    comer.addActionListener(this);
	    entrenar.addActionListener(this);
	    dormir.addActionListener(this);
	    bañar.addActionListener(this);
	    revivir.addActionListener(this);
	  } //init

	  public void paint(Graphics g)
	  {
		  acciones.setSize(620,35);
		  acciones.setLocation(50,200);

		  situacion_actual.setSize(340,30);
		  situacion_actual.setLocation(50,350);

		  imagen11.setSize(100,100);
		  imagen11.setLocation(0,0);

		  status.setSize(700,30);
		  status.setLocation(50,500);
	  }

	   public void actionPerformed(ActionEvent evento)
	   {
	         // el usuario oprimió Intro en objeto JTextField campoTexto1
	         if ( evento.getSource() == comer )
	         {
	        	 //aumentar los valores de hambre(comida)
	        	 hambre = hambre + 20 + bonus();
	             hambre00.setText(String.valueOf(hambre));
	             puntos = 20 + bonus();

	             //aumentar los valores de energia
	        	 energia = energia + 20 + (bonus()/2);
	             energia00.setText(String.valueOf(energia));

	             //aumentar los valores de felicidad
	             felicidad = felicidad + 10 + (bonus()/3);
	             felicidad00.setText(String.valueOf(felicidad));

	             //aumentar los valores de fuerza
	        	 suciedad = suciedad + 10 + (bonus()/2);
	             suciedad00.setText(String.valueOf(suciedad));

	             //para efectos de debug ver cuales son los valores agregas en la shell
	             System.out.println("[Accion] Le diste de comer [Pts.comida+]: "+(20 + bonus())+" [Pts.energia+]: "+(20 + (bonus()/2))+" [Pts.felicidad+]: "+(10 + (bonus()/3))+" [Pts.suciedad+]:"+(20 + (bonus()/2)));
	        	 ImageIcon im = new ImageIcon("../src/comiendo.gif");
	        	 imagen11.setIcon(im);

	        	 actual = "Comiendo";
	        	 actual00.setText(actual);

	             JOptionPane.showMessageDialog(null, "Le diste de comer al Tamagotchi y gano "+puntos+" puntos de comida y algo de energia", "Comiendo", JOptionPane.INFORMATION_MESSAGE);
	             muere();
	             //repaint();

	         }
	         if ( evento.getSource() == entrenar )
	         {
	        	 //generar un entrenamiento
	        	 Random rnd = new Random();
	        	 int ax = 0;

	        	 ax = ((int)(rnd.nextDouble() * 2));

	        	 if( ax == 1)
	        	 {
	        		 ImageIcon im=new ImageIcon("../src/entrenando_corre.gif");
		        	 imagen11.setIcon(im);
		        	 actual = "corriendo";

	        	 }
	        	 else
	        	 {
	        		 ImageIcon im=new ImageIcon("../src/entrenando_pelea.gif");
		        	 imagen11.setIcon(im);
		        	 actual = "peleando con otro tamagotchi";
	        	 }

	        	 //aumentar los valores de experiencia
	             experiencia = experiencia + 40 + bonus();
	             experiencia00.setText(String.valueOf(experiencia));

	             //Restar valores a energia
	        	 energia = energia - 20 - (bonus()/3);
	             energia00.setText(String.valueOf(energia));

	             //Restar los valores de hambre
	        	 hambre = hambre - 25 - (bonus()/2);
	             hambre00.setText(String.valueOf(hambre));

	             //aumentar los valores de fuerza
	        	 fuerza = fuerza + 10 + bonus();
	             fuerza00.setText(String.valueOf(fuerza));

	             //aumentar los valores de fuerza
	        	 suciedad = suciedad + 20 + (bonus()/2);
	             suciedad00.setText(String.valueOf(suciedad));

	             felicidad = felicidad - 20 - bonus();
	             felicidad00.setText(String.valueOf(felicidad));

	             //para efectos de debug ver cuales son los valores agregas en la shell
	             System.out.println("[Accion] Esta entrenando [Pts.felicidad-]: "+20 + bonus()+"[Pts.experiencia+]: "+(40 + bonus())+" [Pts.energia-]: "+(20 + (bonus()/2))+" [Pts.hambre-]: "+(25 + (bonus()/2))+" [Pts.fuerza+]: "+(10+bonus())+" [Pts.suciedad+]:"+(20 + (bonus()/2)));

	             actual00.setText(actual);
	             puntos = 40 + bonus();

	             JOptionPane.showMessageDialog(null, "El Tamagotchi esta entrenando muy duro ... ha ganado "+puntos+" puntos de exp", "Entrenando", JOptionPane.INFORMATION_MESSAGE);
	             subirNivel();

	             	if(energia < 20 && advirtio != true)  	             	{ 	             		energia00.setBackground(Color.RED); 	             		JOptionPane.showMessageDialog(null, "Ten cuidado si la energia del tamagotchi llega a 0 morira, dale de comer", "Peligro", JOptionPane.INFORMATION_MESSAGE); 	       	            advirtio = true; 	             	} 	              	             muere(); 	        	 //repaint(); 	         } 	         if ( evento.getSource() == dormir ) 	         {         		 ImageIcon im=new ImageIcon("../src/descanzando.gif"); 	        	 imagen11.setIcon(im); 	        	 actual = "Esta descanzando"; 	        	 actual00.setText(actual); 	        	  	        	 energia = 100; 	             energia00.setText(String.valueOf(energia)); 	              	             felicidad = felicidad + 30 + bonus(); 	             felicidad00.setText(String.valueOf(felicidad)); 	              	             fuerza = fuerza - 40 - (bonus()/3); 	             fuerza00.setText(String.valueOf(fuerza)); 	        	  	             //para efectos de debug ver cuales son los valores agregas en la shell 	             System.out.println("[Accion] Tomando un descanzo [Pts.energia+]: "+100+" [Pts.felicidad+]: "+(30 + bonus()+" [Pts.fuerza-]: "+(40 + (bonus()/3)))); 	             JOptionPane.showMessageDialog(null, "El tamagotchi ha descanzado y recobrado todas sus fuerzas, tambien es mas feliz", "Descanzando", JOptionPane.INFORMATION_MESSAGE); 	        	 muere(); 	         } 	         if ( evento.getSource() == bañar ) 	         {         		 ImageIcon im=new ImageIcon("../src/bañar.gif"); 	        	 imagen11.setIcon(im); 	        	 actual = "Bañandose ... no le gusta"; 	        	 actual00.setText(actual); 	        	  	        	 felicidad = felicidad - 10 - (bonus()/3); 	        	 felicidad00.setText(String.valueOf(felicidad)); 	        	 suciedad = 0; 	        	 suciedad00.setText(String.valueOf(suciedad)); 	        	  	        	//para efectos de debug ver cuales son los valores agregas en la shell 	             System.out.println("[Accion] Bañandose [Pts.suciedad-]: "+0+" [Pts.felicidad-]: "+(10 + (bonus()/3))); 	               	        	 JOptionPane.showMessageDialog(null, "El tamagotchi tomo un baño, aunque no le gusta >.<", "Bañandose", JOptionPane.INFORMATION_MESSAGE);

	        	 muere();
	         }
	         if ( evento.getSource() == revivir )
	         {
	        	 hambre00.setBackground(Color.WHITE);
	        	 energia00.setBackground(Color.WHITE);
	        	 felicidad00.setBackground(Color.WHITE);
	        	 fuerza00.setBackground(Color.WHITE);
	        	 experiencia00.setBackground(Color.WHITE);
	        	 nivel00.setBackground(Color.WHITE);
	        	 suciedad00.setBackground(Color.WHITE);

	        		energia = 100;
	        		hambre = 25;
	        		felicidad = 25;
	        		fuerza = 25;
	        		experiencia = 0;
	        		nivel = 0;
	        		suciedad = 0;

	             energia00.setText(String.valueOf(energia));
	             	energia00.setBackground(Color.WHITE);
	             hambre00.setText(String.valueOf(hambre));
	             felicidad00.setText(String.valueOf(felicidad));
	             fuerza00.setText(String.valueOf(fuerza));
	             experiencia00.setText(String.valueOf(experiencia));
	             nivel00.setText(String.valueOf(nivel));
	             suciedad00.setText(String.valueOf(suciedad));

	        	 comer.setEnabled(true);
	        	 entrenar.setEnabled(true);
	        	 dormir.setEnabled(true);
	        	 bañar.setEnabled(true);
	        	 revivir.setEnabled(false);

	             ImageIcon im=new ImageIcon("../src/nada.gif");
	        	 imagen11.setIcon(im);

	        	 System.out.println("Reviviendo");
	             JOptionPane.showMessageDialog(null, "El tamagotchi ha revivido", "Revivio", JOptionPane.INFORMATION_MESSAGE);

	         }
	               //acción
	   }
	   private void muere()
	   {
		   if(energia <= 0)
		   {
			   energia00.setBackground(Color.RED);
	      		 ImageIcon im=new ImageIcon("../src/muere.gif");
	        	 imagen11.setIcon(im);
	        	 actual = "muerto";
	        	 actual00.setText(actual);
	        	 JOptionPane.showMessageDialog(null, "El tamagotchi ha muerto .. no lo cuidaste lo suficientemente bien", "Murio", JOptionPane.INFORMATION_MESSAGE);

	        	 //descativamos todos los botones y activamos el de revivir para que juege de nuevo
	        	 comer.setEnabled(false);
	        	 entrenar.setEnabled(false);
	        	 dormir.setEnabled(false);
	        	 bañar.setEnabled(false);
	        	 revivir.setEnabled(true);
		   }
		   else
		   {
			   if(hambre <= 0)
			   {
				   hambre00.setBackground(Color.RED);
		             ImageIcon im=new ImageIcon("../src/hambre.gif");
		        	 imagen11.setIcon(im);
		        	 actual = "Tiene mucha hambre";
		        	 actual00.setText(actual);
				   JOptionPane.showMessageDialog(null, "Estas matando de hambre al tamagotchi, dale de comer rapido", "Sugerencia: Darle de comer", JOptionPane.INFORMATION_MESSAGE);
			   }
			   else
			   {
				   hambre00.setBackground(Color.WHITE);
			   }
			   if(fuerza <= 0)
			   {
				   fuerza00.setBackground(Color.RED);
		             ImageIcon im=new ImageIcon("../src/debil.gif");
		        	 imagen11.setIcon(im);
		        	 actual = "Esta muy debil";
		        	 actual00.setText(actual);
				   JOptionPane.showMessageDialog(null, "El tamagotchi esta muy debil, entrenalo", "Sugerencia: Entrenarlo", JOptionPane.INFORMATION_MESSAGE);
			   }
			   else
			   {
				   fuerza00.setBackground(Color.WHITE);
			   }
			   if(felicidad <=0) 			   { 				   felicidad00.setBackground(Color.RED); 		             ImageIcon im=new ImageIcon("../src/enojado.gif"); 		        	 imagen11.setIcon(im); 		        	 actual = "Te odia, correee!"; 		        	 actual00.setText(actual); 				   JOptionPane.showMessageDialog(null, "Hiciste que el tamagotchi te odie >.<, haz algo para que se ponga feliz", "Sugerencia: Entrenar, Comer o Descanzar", JOptionPane.INFORMATION_MESSAGE); 			   } 			   else 			   { 				   felicidad00.setBackground(Color.WHITE); 			   } 			   if(suciedad >= 100)
			   {
				   suciedad00.setBackground(Color.RED);
		             ImageIcon im=new ImageIcon("../src/sucio.gif");
		        	 imagen11.setIcon(im);
		        	 actual = "Esta muy sucio";
		        	 actual00.setText(actual);
				   JOptionPane.showMessageDialog(null, "Esta muy sucio, dale un baño", "Sugerencia: Darle un baño", JOptionPane.INFORMATION_MESSAGE);
			   }
			   else
			   {
				   suciedad00.setBackground(Color.WHITE);
			   }
		   }
	   }
	 //Metodo para gestionar los niveles del tamagotchi
	    private void subirNivel()
	    {
	        Random rnd = new Random();
	        float expExtra;

	        //nivel = Integer.parseInt(nivelField.getText());
	        //sigNivel = Integer.parseInt(confianzaField.getText());

	        if(nivel == 0)
	        {
	            if(experiencia > 100)
	            {

	                nivel = nivel + 1;
	                nivel00.setText(String.valueOf(nivel));
	                expExtra = ((float)(rnd.nextDouble() * 0.5));
	                sigNivel = (experiencia * 2)+(experiencia * expExtra); //Experiencia requerida para el siguiente nivel
	                JOptionPane.showMessageDialog(null, "Felicidades  ha avanzado al nivel 1\nPara el siguiente nivel necesitaras "+sigNivel+" puntos de exp.", "Felicidades", JOptionPane.INFORMATION_MESSAGE);
	                System.out.println("experiencia*2:"+experiencia*2+" aleatorio: "+(experiencia * expExtra));
	                //confianzaField.setText(String.valueOf(sigNivel));
	            }
	        }
	        else
	        {
	            if(experiencia >= sigNivel)
	            {
	                nivel = Integer.parseInt(nivel00.getText());
	                nivel = nivel + 1;
	                nivel00.setText(String.valueOf(nivel));
	                expExtra = ((float)(rnd.nextDouble() * 0.5));
	                sigNivel = (experiencia * 2)+(experiencia * expExtra); //Experiencia requerida para el siguiente nivel
	                JOptionPane.showMessageDialog(null, "Felicidades  ha avanzado al nivel "+nivel+"\nPara el siguiente nivel necesitaras "+sigNivel+" puntos de exp.", "Felicidades", JOptionPane.INFORMATION_MESSAGE);
	                System.out.println("experiencia*2:"+experiencia*2+" aleatorio: "+(experiencia * expExtra));
	                //confianzaField.setText(String.valueOf(sigNivel));
	            }
	        }
	    }
	    public static int bonus()
	    {
	        int bonus = 0;
	        Random rnd = new Random();
	        bonus = (int)(rnd.nextDouble() * 30.0);//Asignar el valor aleatorio a la variable
	        return bonus;
	    }
}

```

Pueden descargar el codigo fuente junto con los recursos (imágenes) del siguiente link

<div class="demobox">
[![](http://www.alevsk.com/wp-content/themes/ModernStyle//images/download.png)](http://www.megaupload.com/?d=SHG3OQWS)
</div>

Ahora lo que sigue es presentar este viernes el otro proyecto desarrollado con Java del que también posteare el código fuente, consiste en una aplicación para reconocer varios gestos del WiiMote y realizar distintas tareas en el SO, lo desarrollamos para una Mac.

salu2