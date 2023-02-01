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

## Website Install
### Install Node:
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
### Build the site:
From the `www` folder, run:
```
npm install
```
```
npm run build
```

## Starting the Development servers
Both the API and site have development servers to faciltate testing and debuggin. 

#### **API** - from the `server` folder, run:
```
python application.py
```
#### **Site** - from the `www` folder, run:
```
npm start
```
