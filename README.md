# pi-stream-cast 
## Raspberry Pi to Chromecast Audio Streamer

A Python Flask app that streams USB audio input from a Raspberry Pi to Google Chromecast Audio devices. 

Why buy the [Sonos Port](https://www.sonos.com/en-us/shop/port) for $449 when you can do the same thing with a Raspberry Pi for half the price and twice the headache? At least that's what I thought when I started this project and here we are. 

## Requirements

- Node Js 18
- Python 3.9
- Raspberry Pi
- Google Chromecast Audio device

## API Installation

### Install Python add-ons:
```
sudo apt-get install python3.9-dev portaudio19-dev python3-pyaudio
```
### Install Python packages:
To install the needed python packages, from the `server` folder run:
```
pip install -r requirements.txt
```

## Website Installation
#### Install Node:
```
curl -sL https://deb.nodesource.com/setup_18.x | sudo bash -
``` 
```
sudo apt-get install -y nodejs
```
you may also need:
```
sudo apt-get install gcc g++ make
```
#### Build the site:
From the `www` folder, run:
```
npm install
```
```
npm run build
```

## Starting the development servers
Both the API and site have development servers to faciltate testing and debuggin. 

#### **API** - from the `server` folder, run:
```
python application.py
```
#### **Site** - from the `www` folder, run:
```
npm start
```

## Apache webserver on Raspberry Pi

#### 
```
sudo apt-get install apache2 libapache2-mod-wsgi-py3
```

#### Apache site config:

```
WSGISocketRotation Off
<VirtualHost *:80>
  ServerName pi-stream-cast.io
  DocumentRoot /var/www/html/pi-stream-cast

  WSGIDaemonProcess bridge threads=1 python-home=/var/www/html/pi-stream-cast/api/venv 
  WSGIProcessGroup bridge
  WSGIScriptAlias /api /var/www/html/pi-stream-cast/api/api.wsgi 

  <Directory /var/www/html/pi-stream-cast/>
    Options -Indexes +FollowSymLinks
    AllowOverride All
    Require all granted
  </Directory>

  ErrorLog ${APACHE_LOG_DIR}/pi-stream-cast.io-error.log
  CustomLog ${APACHE_LOG_DIR}/pi-stream-cast.io-access.log combined
</VirtualHost>
```
