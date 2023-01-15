FROM klakegg/hugo:0.92.2 as uilayer
WORKDIR /app

COPY ./ .
RUN hugo --minify

FROM docker.io/library/nginx:1.23.1-alpine
MAINTAINER Lenin Alevski "lenin@alevsk.com"
EXPOSE 8080

COPY --from=uilayer /app/public /usr/share/nginx/html
COPY --from=uilayer /app/nginx/nginx.conf /etc/nginx/nginx.conf

USER nginx

CMD nginx -g "daemon off;"
