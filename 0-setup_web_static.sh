#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static

# Install Nginx if it is not already installed
if ! command -v nginx &>/dev/null; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

# Create necessary directories if they don't already exist
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link and update ownership
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config="location /hbnb_static {
    alias /data/web_static/current/;
}
"
sudo sed -i "/server_name _;/a ${config}" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
