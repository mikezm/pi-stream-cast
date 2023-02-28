"""
py-stream-cast API

"""
from app.config import CHROME_CAST_UUID, CAST_STREAM_ADDRESS, API_BASE
from app.services.chromecast import Casts, STATUS_ACTIVE, STATUS_NEW
from app.services.audio import Stream
from flask import Flask, Response, Blueprint, jsonify
from flask_cors import CORS


bp = Blueprint('api', __name__, url_prefix=API_BASE)
CORS(bp)

casts = Casts()
stream = Stream()

@bp.route("/status")
def status():
    cast_status = False
    cast_object = {}
    if casts.status == STATUS_ACTIVE:
        cast_status = True
        cast_object = casts.get_cast_info()

    if casts.status == STATUS_NEW:
        cast_status = True

    response = {
        'streamStatus': (stream.ready),
        'castStatus': cast_status,
        'castInfo': cast_object
    }
    return jsonify(response), 200

@bp.route("/audio-stream")
def audio_stream():
    if not stream.ready:
        stream.refresh()
    return Response(stream.generate_audio(), mimetype="audio/x-wav;codec=pcm")

@bp.route("/list-casts")
def list_casts():
    return jsonify(casts.list_chromecasts()), 200

@bp.route("/refresh-casts")
def refresh_casts():
    casts.fetch_chromecasts()
    return jsonify({'success': True, 'message': 'refreshed'}), 200

@bp.route("/start-cast/<string:id>")
def start_cast(id):
    casts.select_cast_device(id)
    casts.play("http://{}{}/audio-stream".format(CAST_STREAM_ADDRESS, API_BASE), "audio/x-wav")
    #response = casts.get_cast_info()
    return jsonify({'success': True, 'message': 'cast started'}), 200

@bp.route("/stop-cast")
def stop_cast():
    err, message = casts.stop()
    if err:
        return jsonify({'success': False, 'message': message}), 500

    return jsonify({'success': True, 'message': 'cast stopped'}), 200

@bp.route("/stop-stream")
def stop_stream():   
    err, message = stream.close()
    if err:
        return jsonify({'success': False, 'message': message}), 500

    return jsonify({'success': True, 'message': 'stream stopped'}), 200

@bp.route("/get-volume")
def get_volume():   
    return jsonify({'success': True, 'volume': casts.get_volume()}), 200

@bp.route("/set-volume/<float:volume>")
def set_volume(volume):   
    err, message = casts.set_volume(volume)
    if err:
        return jsonify({'success': False, 'message': message}), 500

    return jsonify({'success': True, 'message': 'volume set to: {}'.format(volume) }), 200

@bp.route("/volume-up")
def volume_up():   
    err, message = casts.volume_up()
    if err:
        return jsonify({'success': False, 'message': message}), 400

    return jsonify({'success': True, 'message': 'volume up'}), 200

@bp.route("/volume-down")
def volume_down():   
    err, message = casts.volume_down()
    if err:
        return jsonify({'message': message}), 400

    return jsonify({'success': True, 'message': 'volume down'}), 200

@bp.route("/volume-mute")
def volume_mute():   
    err, message = casts.volume_mute()
    if err:
        return jsonify({'success': False, 'message': message}), 400

    return jsonify({'success': True, 'message': 'volume muted'}), 200

@bp.route("/volume-unmute")
def volume_unmute():   
    err, message = casts.volume_unmute()
    if err:
        return jsonify({'success': False, 'message': message}), 400

    return jsonify({'success': True, 'message': 'volume unmuted'}), 200

app = Flask(__name__)
app.register_blueprint(bp)