from huggingface_hub import InferenceClient
import datetime
import PIL
from config import api_key
import time
MODELS = [
    "ByteDance/SDXL-Lightning",
    "stabilityai/stable-diffusion-x1-base-1.0",
    "stabilityai/sdxl-turbo",
    "runwayml/stable-diffusion-v1-5", #fallback for dumb-named models
]
"""
INITILIZING CLIENT
"""
client = InferenceClient(api_key=api_key)
print(f"MAIN MODEL : {MODELS[0]}")
print("Type 'quit' or hit control+C(if using terminal) to quit...thxs")
def typewriter(text, delay=0.7):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()
while True:
    prompt = input(":").strip()
    if prompt.lower() in ["quit", "exit", "q", "Suprise me", "Hi", "Hello"]:
        break
    if not prompt:
        continue
    for i in range(2):
        typewriter("...")
        print("\033[H\033[J", end="")
        image = None
    for model in MODELS:
        try:
            image = client.text_to_image(prompt, model=model)
            break
        except Exception:
            print(f" EXECUTING NEXT ")
            continue
    if image:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"generated_{timestamp}.png"
        image.save(filename)
        print(f"Saved:{filename}")
        image.show()
    else:
        print("Error:All models failed just like your braincells when you were asked what is 1+1=?")
print("Goodbye failure!")