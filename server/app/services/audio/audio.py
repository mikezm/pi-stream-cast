from app.config import USB_DEVICE_NAME
import pyaudio

"""
FORMAT = pyaudio.paInt16 # pyaudio.paInt16 #pyaudio.paFloat32 #salah tunning jadi suara aneh
CHUNK = 262144  # 131072 #65536 #32768 #16384 #8192 #7168 #6144 #5120 #4096 #1024 mulai normal
CHANNELS = 2
RATE = 44100  # 48000
BIT_PER_SAMPLE = 16

"""

class Stream:
    def __init__(self) -> None:
        self.ready = False
        self.format = pyaudio.paInt16
        self.chunk = 262144
        self.channels = 2
        self.rate = 44100
        self.bits_per_sample = 16
        self.refresh()
        

    def refresh(self):
        self.p = pyaudio.PyAudio()
        self.device_index = self.get_device_index()
        self.ready = True

    def get_device_index(self):
        for index in range(self.p.get_device_count()):
            if USB_DEVICE_NAME in self.p.get_device_info_by_index(index).get('name'):
                return index

    def generate_header(self):
        datasize = 2000*10**6
        output = bytes("RIFF", 'ascii')
        output += (datasize + 36).to_bytes(4, 'little')
        output += bytes("WAVE", 'ascii')
        output += bytes("fmt ", 'ascii')
        output += (16).to_bytes(4, 'little')
        output += (1).to_bytes(2, 'little')
        output += (self.channels).to_bytes(2, 'little')
        output += (self.rate).to_bytes(4, 'little')
        output += (self.rate * self.channels * self.bits_per_sample // 8).to_bytes(4, 'little')
        output += (self.channels * self.bits_per_sample // 8).to_bytes(2, 'little')
        output += (self.bits_per_sample).to_bytes(2, 'little')
        output += bytes("data", 'ascii')
        output += (datasize).to_bytes(4, 'little')
        return output

    def generate_audio(self):
        wav_header = self.generate_header()
        self.stream = self.p.open(format=self.format, channels=self.channels, rate=self.rate, input=True,
                        input_device_index=self.device_index, output=True, frames_per_buffer=self.chunk)

        first_run = True
        while True:
            if first_run:
                data = wav_header+self.stream.read(self.chunk * 2)
                first_run = False
            else:
                data = self.stream.read(self.chunk)
            yield (data)

    def close(self):
        try:
            self.ready = False
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()
            return [False, None]
        except:
            pass
            return [True, "unable to stop stream"]
