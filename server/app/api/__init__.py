"""
py-stream-cast API

"""
from app.config import CHROME_CAST_UUID, CAST_STREAM_ADDRESS
from app.services.chromecast import get_chromecast
from app.services.audio import Stream
from flask import Flask, Response

app = Flask(__name__)

cast = None

@app.route("/audio-stream")
def audio():
    stream = Stream()
    return Response(stream.generate_audio(), mimetype="audio/x-wav;codec=pcm")


@app.route("/api/cast")
def cast_audio_stream():
    if not cast:
        cast = get_chromecast(CHROME_CAST_UUID)
    
    cast.play_media("http://{}/audio-stream".format(CAST_STREAM_ADDRESS), "audio/x-wav")
    return Response(None, 200)


@app.route("/api/stop")
def cast_audio_stream():
    if not cast:
        cast = get_chromecast(CHROME_CAST_UUID)
    
    cast.stop()
    return Response(None, 200)