import time
from flask import Flask, Response, render_template
import pyaudio
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


def generate_header(sample_rate, bits_per_sample, channels):
    datasize = 2000*10**6
    output = bytes("RIFF", 'ascii')
    output += (datasize + 36).to_bytes(4, 'little')
    output += bytes("WAVE", 'ascii')
    output += bytes("fmt ", 'ascii')
    output += (16).to_bytes(4, 'little')
    output += (1).to_bytes(2, 'little')
    output += (channels).to_bytes(2, 'little')
    output += (sample_rate).to_bytes(4, 'little')
    output += (sample_rate * channels * bits_per_sample // 8).to_bytes(4, 'little')
    output += (channels * bits_per_sample // 8).to_bytes(2, 'little')
    output += (bits_per_sample).to_bytes(2, 'little')
    output += bytes("data", 'ascii')
    output += (datasize).to_bytes(4, 'little')
    return output


def generate_audio():
    # pyaudio.paInt16 #pyaudio.paFloat32 #salah tunning jadi suara aneh
    FORMAT = pyaudio.paInt16
    CHUNK = 262144  # 131072 #65536 #32768 #16384 #8192 #7168 #6144 #5120 #4096 #1024 mulai normal
    CHANNELS = 2
    RATE = 44100  # 48000
    DEVICE_INDEX = get_device_index()
    BIT_PER_SAMPLE = 16
    wav_header = generate_header(RATE, BIT_PER_SAMPLE, CHANNELS)
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,
                    input_device_index=DEVICE_INDEX, output=True, frames_per_buffer=CHUNK)
    print("Recording ...")

    first_run = True
    while True:
        if first_run:
            data = wav_header+stream.read(CHUNK * 5)
            first_run = False
        else:
            data = wav_header+stream.read(CHUNK)
        yield (data)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/audio")
def audio():
    return Response(generate_audio(), mimetype="audio/x-wav;codec=pcm")


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


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True, port=5000)
