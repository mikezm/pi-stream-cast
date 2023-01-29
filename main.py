from flask import Flask, Response, render_template
import pyaudio
import time
import pychromecast

CHROME_CAST_UUID = "a050f03a-0faa-9fec-022c-2c0dd8f4dc65"

def get_chromecast(uuid):
  """Return the target Chromecast, or None."""
  try:
      chromecasts, browser = pychromecast.get_chromecasts()
      return [chromecast
              for chromecast
              in chromecasts 
              if str(chromecast.uuid) == uuid][0]
  except IndexError:
      pass

app = Flask(__name__)

p = pyaudio.PyAudio()

def get_device_index():
    for index in range(p.get_device_count()):
        if p.get_device_info_by_index(index).get('name') == "USB Audio CODEC: - (hw:1,0)":
            return index

def genHeader(sampleRate, bitsPerSample, channels):
  datasize = 2000*10**6
  o = bytes("RIFF",'ascii')                                               # (4byte) Marks file as RIFF
  o += (datasize + 36).to_bytes(4,'little')                               # (4byte) File size in bytes excluding this and RIFF marker
  o += bytes("WAVE",'ascii')                                              # (4byte) File type
  o += bytes("fmt ",'ascii')                                              # (4byte) Format Chunk Marker
  o += (16).to_bytes(4,'little')                                          # (4byte) Length of above format data
  o += (1).to_bytes(2,'little')                                           # (2byte) Format type (1 - PCM)
  o += (channels).to_bytes(2,'little')                                    # (2byte)
  o += (sampleRate).to_bytes(4,'little')                                  # (4byte)
  o += (sampleRate * channels * bitsPerSample // 8).to_bytes(4,'little')  # (4byte)
  o += (channels * bitsPerSample // 8).to_bytes(2,'little')               # (2byte)
  o += (bitsPerSample).to_bytes(2,'little')                               # (2byte)
  o += bytes("data",'ascii')                                              # (4byte) Data Chunk Marker
  o += (datasize).to_bytes(4,'little')                                    # (4byte) Data size in bytes
  return o

def generateAudio():
		FORMAT = pyaudio.paInt16 #pyaudio.paInt16 #pyaudio.paFloat32 #salah tunning jadi suara aneh
		CHUNK = 262144 #131072 #65536 #32768 #16384 #8192 #7168 #6144 #5120 #4096 #1024 mulai normal
		CHANNELS = 2
		RATE = 44100 #48000
		DEVICE_INDEX = get_device_index()
		sampleRate = 44100
		bitsPerSample = 16
		channels = 2
		wav_header = genHeader(sampleRate, bitsPerSample, channels)
		stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, input_device_index=DEVICE_INDEX, output=True, frames_per_buffer=CHUNK)
		print("Recording ...")
		first_run = True
		while True:
			if first_run:
				data = wav_header+stream.read(CHUNK* 5)
				first_run = False
			else:
				data = wav_header+stream.read(CHUNK)
			yield(data)


@app.route("/")
def index():
	return render_template('index.html')

@app.route("/api/audio")
def audio():
  return Response(generateAudio(), mimetype="audio/x-wav;codec=pcm")


@app.route("/api/cast")
def cast_audio_stream():
  # Find the Chromecast on the network
  cast = None
  while cast is None:
    print('Searching for Chromecast...')
    time.sleep(2)
    cast = get_chromecast(CHROME_CAST_UUID)
  cast.wait()
  print('Found Chromecast at: ' + cast.cast_info.host)
  mc = cast.media_controller
  mc.play_media("http://192.168.50.242:5000/audio", "audio/x-wav")
  return Response(None, 200)

@app.route('/')
def index():
  """Audio streaming home page."""
  return render_template('index.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True, threaded=True,port=5000)