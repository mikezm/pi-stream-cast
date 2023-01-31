import time
import pychromecast


class Casts:
    uuid = None
    cast = None
    mc = None

    def __init__(self) -> None:
        self.fetch_chromecasts()

    def fetch_chromecasts(self):
        """Return a list of chromecasts"""
        self.chromecasts, self.browser = pychromecast.get_chromecasts()

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
        except IndexError:
            pass

    def play(self, url, content_type):
        self.mc.play_media(url, content_type)

    def stop(self):
        self.mc.stop()
