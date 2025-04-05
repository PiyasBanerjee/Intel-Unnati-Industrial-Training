# voice_command.py
import vosk
import sounddevice as sd
import json
import queue

q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def listen_for_update(timeout=30):
    model = vosk.Model("models/vosk-model-small-en-us-0.15")  
    with sd.RawInputStream(samplerate=16000, blocksize=8000,
                           dtype='int16', channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, 16000)
        print("Listening for keyword 'update'...")
        for _ in range(timeout * 2):  
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                if 'update' in result.get("text", "").lower():
                    return True
    return False
