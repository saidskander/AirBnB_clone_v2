#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static.
#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static.
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "<html>
         <head>
         </head>
         <body>
             Holberton School
         </body>
      </html>" > /data/web_static/releases/test/index.html

chown -R ubuntu /data/
chgrp -R ubuntu /data/
printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /etc/nginx/html;
    index  index.html index.htm;

    location /hbnb_static {
     alias /data/web_static/current;
     index index.html index.htm;
    }

    location /redirect_me {
        return 301 https://github.com/saidskander/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default
service nginx restart
