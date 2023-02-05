"""
py-stream-cast API

"""
from app.config import CHROME_CAST_UUID, CAST_STREAM_ADDRESS
from app.services.chromecast import Casts
from app.services.audio import Stream
from flask import Flask, Response, jsonify

app = Flask(__name__)
casts = Casts()
stream = Stream()

@app.route("/audio-stream")
def audio_stream():
    if not stream.ready:
        stream.refresh()
    return Response(stream.generate_audio(), mimetype="audio/x-wav;codec=pcm")


@app.route("/list-casts")
def list_casts():
    return jsonify(casts.list_chromecasts()), 200


@app.route("/start-cast")
def start_cast():
    casts.select_cast_device(CHROME_CAST_UUID)
    casts.play("http://{}/audio-stream".format(CAST_STREAM_ADDRESS), "audio/x-wav")
    return Response(None, 200)


@app.route("/stop-cast")
def stop_cast():    
    casts.stop()
    stream.close()
    return Response(None, 200)