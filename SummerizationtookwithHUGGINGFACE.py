import requests
from colorama import Fore, Style, init
from config import api_key
import time
import random
init(autoreset=True)
DEFAULT_MODEL = "google/pegasus-xsum"
randy = 1
def build_api_url(model_name):
    return f"https://api-inference.huggingface.co/models/{model_name}"
def query(payload, model_name = DEFAULT_MODEL):
    api_url = build_api_url(model_name)
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(api_url, headers=headers, json=payload)
    return response.json()
def summarize_text(text, min_length, max_length, model_name):
    payload = {"inputs": text, "parameters": {"min_length": min_length, "max_length": max_length}}
    print(Fore.BLUE + f"\nPerforming AI summarization using model: {model_name}")
    result = query(payload, model_name=model_name)
    
    if isinstance(result, list) and result and "summary_text" in result[0]:
        return result[0]["summary_text"]
    else:
        print(Fore.RED + "failed")
        print("Id1ot error detected, PEBKAC has been confirmed, please try again later")
        return None
def typewriter(text, speed=0.0001):
    for character in text:
        print(character, end='', flush=True)
        time.sleep(speed)
    print()
if __name__ == "__main__":
    typewriter(Fore.YELLOW + Style.BRIGHT + "????Ay, what's your name? Or do I need to check the lost-and-found bin for whatever label your parents forgot to put on you? Honestly, drop the government name—I just need to know what to put on the warning label and my local hazard map so nobody else makes the mistake of interacting with your specific brand of disappointment.")
    user_name = input("Your name:  ").strip()
    if not user_name:
        user_name = "Error_403_Identity_Forbidden"
    typewriter(f"{user_name}, you are just... I am dissapointed that you need an eintire AI+(this)code to summerize this easy code")
    typewriter(Fore.RED + "\n pls enter text to be deleted")
    user_text = input("> ").strip()
    if not user_text:
        print(Fore.RED + f"REJECTED {user_name}, ENTER TEXT, I DONT READ WHITESPACE OR YOUR MIND, WHICH LETS BE REAL, IS THINKING OF EATING PIZZA INSTEAD OF FOCUSING")
    else:
        model_choice = input("model name (leave blank dor a defaulter that is so useless, nobody wants to know about it ):  ").strip()
        if not model_choice:
            model_choice = DEFAULT_MODEL

    print(Fore.YELLOW + "\n Choose text destroying style")
    print("1. Standard destruction(Quick, Consise and reads like you trying to recite your very very real and not ai poem to your teacher)")
    print("2. Enhanced destruction(More detailed, Refined, and carries a hint of AI that looks like nonsense because why not?)")
    style_choice = input("Enter 1 or 2:  ").strip()
    if style_choice == "2":
        min_length = 80
        max_length = 200
        print(Fore.BLUE + "Enhanced destruction mode initiated")
    else:
        min_length = 50
        max_length = 150
        print(Fore.BLUE + "Standard destruction")
    summary = summarize_text(user_text, min_length, max_length, model_name=model_choice)
    if summary:
        print(Fore.GREEN + Style.BRIGHT + f"\n {user_name}, you did it huh?You wrote down text meliticulously, only to just end it for ai slop huh?..fine..here:")
        print(Fore.GREEN + summary)
    else:
        print(Fore.RED + "Failed to generate summary.")
    