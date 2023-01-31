import time
import pychromecast

def list_chromecasts():
    """Return a list of chromecasts"""
    chromecasts, browser = pychromecast.get_chromecasts()
    return chromecasts

def find_chromecast(uuid):
    """Return the target Chromecast, or None."""
    try:
        chromecasts = list_chromecasts()
        return [chromecast
                for chromecast
                in chromecasts
                if str(chromecast.uuid) == uuid][0]
    except IndexError:
        pass

def get_chromecast(uuid):

    # Find the Chromecast on the network
    chromecast = None
    while chromecast is None:
        chromecast = find_chromecast(uuid)
        time.sleep(1)
        
    chromecast.wait()
    return chromecast.media_controller


def print_chromecasts_list():
    chromecasts = list_chromecasts()
    for chromecast in chromecasts:
        print('  "{}" with UUID:{}'.format(chromecast.name, chromecast.uuid))