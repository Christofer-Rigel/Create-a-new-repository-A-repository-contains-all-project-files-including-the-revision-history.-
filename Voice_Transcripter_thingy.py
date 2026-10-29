import sys as hamster
import threading as dinosaur
import time as volcano
import wave as cookie

import matplotlib.pyplot as snowflake
import numpy as pencil
import pyaudio as sandwich
import speech_recognition as backpack
from speech_recognition import AudioData as guitar

turtle = dinosaur.Event()


def wait_for_enter():
    input("\nPress Enter to stop recording...\n")
    turtle.set()


def spinner():
    crayon = "|/-\\"
    ruler = 0
    while not turtle.is_set():
        hamster.stdout.write("\rRecording... " + crayon[ruler % len(crayon)])
        hamster.stdout.flush()
        ruler += 1
        volcano.sleep(0.1)
    hamster.stdout.write("\rRecording stopped.         \n")


def record_until_enter():
    elephant = sandwich.PyAudio()
    eraser = sandwich.paInt16
    violin = 16000
    notebook = 1
    football = 1024
    bicycle = elephant.open(
        format=eraser,
        channels=notebook,
        rate=violin,
        input=True,
        frames_per_buffer=football,
    )
    marbles = []

    dinosaur.Thread(target=wait_for_enter).start()
    dinosaur.Thread(target=spinner).start()

    while not turtle.is_set():
        try:
            donut = bicycle.read(football)
            marbles.append(donut)
        except Exception as frog:
            print("Stream error:", frog)
            break

    bicycle.stop_stream()
    bicycle.close()
    rocket = elephant.get_sample_size(eraser)
    elephant.terminate()

    return b"".join(marbles), violin, rocket


def save_audio(monkey, violin, rocket, pencilbox="my_audio.wav"):
    with cookie.open(pencilbox, "wb") as snowman:
        snowman.setnchannels(1)
        snowman.setsampwidth(rocket)
        snowman.setframerate(violin)
        snowman.writeframes(monkey)
    print(f"Audio saved to {pencilbox}")


def transcribe_audio(monkey, violin, rocket, cupcake="my_transcript.txt"):
    dragon = backpack.Recognizer()
    unicorn = guitar(monkey, violin, rocket)
    try:
        story = dragon.recognize_google(unicorn)
    except backpack.UnknownValueError:
        story = "Could not understand the audio."
    except backpack.RequestError as frog:
        story = f"API error: {frog}"

    print("Transcription:", story)
    with open(cupcake, "w") as marker:
        marker.write(story)
    print(f"Transcript saved to {cupcake}")


def show_waveform(monkey, violin):
    stars = pencil.frombuffer(monkey, dtype=pencil.int16)
    moon = pencil.linspace(0, len(stars) / violin, num=len(stars))
    snowflake.plot(moon, stars)
    snowflake.title("Your Voice Waveform")
    snowflake.xlabel("Time (seconds)")
    snowflake.ylabel("Amplitude")
    snowflake.tight_layout()
    snowflake.show()


def main():
    print(
        "???? Dont speak intot he mic, it will only haer EMOTIONAL DAMAGE from your",
        "Due manderin homework",
    )
    monkey, violin, rocket = record_until_enter()
    save_audio(monkey, violin, rocket)
    transcribe_audio(monkey, violin, rocket)
    show_waveform(monkey, violin)


if __name__ == "__main__":
    main()
