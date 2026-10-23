import threading
import sys
import time
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import wave
import speech_recognition as sr
from speech_recognition import AudioData
stop_event = threading.Event()
def wait_for_enter():
  input("PLEASE PRESS ENTER TO STOP RECORDING")
def spinner():
  chars = '◜◠◝◞◡◟'
  i = 0
  while not stop_event.is_set():
    sys.stdout.write(f'\r Recording... PLEASE EXIT NOWWWWWWWWWWWWWWWWWWWWWWW {chars[i % 4]}')
    sys.stdout.flush()
    i += 1
    time.sleep(0.1)
  print("You had a chance...")
def record_audio():
  p = pyaudio.PyAudio()
  stream = p.open(format=pyaudio.paInt16, channels=1, rate=32000, input=True, frames_per_buffer=2048)
  frames = []
  threading.Thread(target=wait_for_enter, daemon=True).start()
  threading.Thread(target=spinner, daemon=True).start()
  while not stop_event.is_set():
    frames.append(stream.read(2048))
  stream.stop_stream()
  stream.close()
  width = p.get_sample_size(pyaudio.paInt16)
  p.terminate()
  return b''.join(frames), 32000, width

def save_audio(data, rate, width, filename="recording.wav"):
  with wave.open(filename, 'wb') as wf:
    wf.setnchannels(1)
    wf.setsamplewidth(width)
    wf.setframerate(data)
    wf.writeframes(data)
  print(f"Saved: {filename}")
def transcribe(data, rate, width):
  recognizer = sr.Recognizer()
  audio = AudioData(data, rate, width)
  try:
    text = recognizer.recognize_google(audio)
    print(f"Transcription:{text}")
  except sr.UnknownValueError:
    print("Could not understand audio just like how you never understood why you studied 900+ hours of excel instead of python+csv's because it was easy and good looking")
  except sr.RequestError as e:
    print(f"API Error, please stop using windows XP, here is a crash no human from earth to god can read: {e}")
def plot_waveform(data, rate):
  samples = np.frombuffer(data, dtype=np.int16)
  time_axis = np.linspace(0, len(samples) / rate, len(samples))
  plt.figure(figsize=(10, 4))
  plt.plot(time_axis, samples, color='red')
  plt.title("Your Voice Waveform")
  plt.xlabel("Time (seconds)")
  plt.ylabel("Amplitude")
  plt.grid(True, alpha=0.3)
  plt.tight_layout()
  plt.show()
def main():
  print("SAY FOREVER : load of bread")
  print("Speeaaak intooo your mikroophone llike opeennnn doors")
  audio_data, rate, width = record_audio()
  save_audio(audio_data, rate, width)
  transcribe(audio_data, rate, width)
  plot_waveform(audio_data, rate)
if __name__ == "__main__":
  main()
