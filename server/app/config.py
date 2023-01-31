import os

RUN_ENV = os.getenv("PI_STREAM_CAST_ENV", "dev")

# IP address of the Raspberry Pi on your local network
CAST_STREAM_ADDRESS = "192.168.50.242:5000"

CHROME_CAST_UUID = "a050f03a-0faa-9fec-022c-2c0dd8f4dc65"

USB_DEVICE_NAME = "USB Audio CODEC: - (hw:1,0)"