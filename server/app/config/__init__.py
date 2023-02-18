import os
import socket


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip


RUN_ENV = os.getenv("PI_STREAM_CAST_ENV", "dev")
API_BASE = ""

# ip address of the Raspberry Pi on your local network
CAST_STREAM_ADDRESS = get_local_ip()
if RUN_ENV == "dev":
    CAST_STREAM_ADDRESS += ":5000"
    API_BASE = "/api"

CHROME_CAST_UUID = "a050f03a-0faa-9fec-022c-2c0dd8f4dc65"

USB_DEVICE_NAME = "USB Audio CODEC"