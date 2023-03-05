import time
import pychromecast

STATUS_ACTIVE = "ACTIVE"
STATUS_INACTIVE = "INACTIVE"
STATUS_NEW = "NEW"
VOLUME_STEP = 0.01


class Casts:
    def __init__(self) -> None:
        self.uuid = None
        self.cast = None
        self.mc = None
        self.chromecasts = None
        self.browser = None
        self.before_mute_volume = None
        self.playing = False
        self.volume = 0.0
        self.status = STATUS_INACTIVE
        self.fetch_chromecasts()

    def fetch_chromecasts(self):
        """Return a list of chromecasts"""
        self.chromecasts, self.browser = pychromecast.get_chromecasts()

    def is_player_ready(self):
        return (
            self.uuid is not None and
            self.cast is not None and
            self.mc is not None and
            self.chromecasts is not None and
            self.browser is not None
        )

    def select_cast_device(self, uuid):
        """Return the target Chromecast, or None."""
        self.uuid = uuid
        try:
            self.cast = [cast
                    for cast
                    in self.chromecasts
                    if str(cast.uuid) == uuid][0]
            self.cast.wait()
            self.mc = self.cast.media_controller
            self.mc.block_until_active()
        except IndexError:
            pass

    def play(self, url, content_type):
        self.mc.play_media(url, content_type)
        self.mc.block_until_active()
        self.playing = True
        self.status = STATUS_ACTIVE

    def stop(self):
        try:
            self.mc.stop()
            self.cast.wait()
            self.status = STATUS_INACTIVE
            self.playing = False
            return [False, None]
        except:
            pass
            return [True, "unable to stop cast"]          

    def list_chromecasts(self):
        return [{
            'name': cast.name,
            'uuid': str(cast.uuid),
            'ip': cast.cast_info.host,
            'port': cast.cast_info.port,
            'type': cast.cast_info.cast_type,
            'volume': 0
        } for cast in self.chromecasts]

    def get_cast_info(self):
        self.cast.wait()
        volume = self.get_volume()
        return {
            'name': self.cast.name,
            'uuid': str(self.cast.uuid),
            'ip': self.cast.cast_info.host,
            'port': self.cast.cast_info.port,
            'type': self.cast.cast_info.cast_type,
            'volume': volume
        }

    def set_volume(self, volume):
        if volume >= 0 and volume <= 1:
            self.cast.set_volume(volume)
            self.mc.block_until_active()
            return [False, None]
        
        return [True, "volume out of range"]

    def get_volume(self):
        self.mc.block_until_active()
        return round(self.cast.status.volume_level, 2)

    def volume_up(self):
        current_volume = self.get_volume()
        return self.set_volume(current_volume + VOLUME_STEP)

    def volume_down(self):
        current_volume = self.get_volume()
        return self.set_volume(current_volume - VOLUME_STEP)

    def volume_mute(self):
        if self.cast.is_volume_muted:
            return [True, "already muted"]
        
        self.cast.set_volume_muted(True)
        self.mc.block_until_active()
        return [False, None]
        
    def volume_unmute(self):
        if not self.cast.is_volume_muted:
            return [True, "must be muted first"]
        
        self.cast.set_volume_muted(False)
        self.mc.block_until_active()
        return [False, None]
