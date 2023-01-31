import sys
import glob


pub_html = glob.glob("/var/www/html/pi-stream-cast/api")

if pub_html:
    sys.path.extend(pub_html)

from application import app as application