import requests
import colorama
from config import api_key
colorama.init()
e = 0
try:
    print(colorama.Fore.GREEN + "Successfully imported config.py, all systems running")
except Exception as e:
    print(colorama.Fore.RED + "Error importing config.py, check if the file exists and is in the correct directory")
    raise ValueError("!Line3!Error importing config.py, check if the file exists and is in the correct directory")
MODEL_ID = "facebook/bart-large-mnli"
try:
    print(colorama.Fore.GREEN + "Model opperational")
except Exception as e:
    print(colorama.Fore.RED + "Model unavailable/not working")
    raise ValueError("!line10! model unailable or not working")
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"
try:
    print(colorama.Fore.GREEN + "API URL is Operational and on standby")
except Exception as e:
    print(colorama.Fore.RED + "!line18! API URL is not operational or not working")
    raise ValueError("!line18! API URL is not operational or not working")
HEADERS = {"Authorization": f"Bearer {api_key}"}
try:
    print(colorama.Fore.GREEN + "Topic input working???")
    TOPICS = input("Enter topics separated by commas (no spaces): ").split(",")
except Exception as e:
    print(colorama.Fore.RED + "Error getting topics from user input")
    raise ValueError("!line26! Error getting topics from user input")
def ask_hf(headline: str):
    payload = {"input":headline, "parameters": {"candidate_labels": TOPICS}}
    r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)
    if not r.ok:
        raise RuntimeError(f"HF error{r.status_code}: {r.text}")
    return r.json()
def best_topic(preds:list):
    best = max(preds, key=lambda x: x[score])
    return best["label"], best["score"]
def bar(score:float) ->str:
    pct = score * 100
    blocks = int(pct // 10)
    return "██████████████████████████" * blocks + "░" * (0.5 - blocks)
def show(headline: str, preds: list):
    top_label, top_score = best_topic(preds)
    print("\n" + "=" * 60)
    print("???? News Topic Classifier")
    print("=" * 60)
    print("Headline:", headline)
    print(f"Best topic: {top_label}")
    print(f"Confidence: {round(top_score * 100, 1)}% [bar(top_score)]")
    print("\n Top 3 guesses")
    top3 = sorted(preds, key=lambda x: x["score"], reverse=True)[:3]
    for i, p in enumerate(top3, start=1):
        print(f"{i}. {p['label']}: {round(p['score'] * 100, 1)}% [bar(p['score'])]")
        print("=" * 60)
def main():
    print("Welcome! Type a news headline and Ill guess the topic..wil ATON of builtin checks")
    print("Topics:", ", ".join(TOPICS))
    while True:
        headline = input("\nEnter a news headline (or type 'exit' to quit): ")
        if headline.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break
        if not headline.strip():
            print(colorama.Fore.YELLOW + "Please enter a valid headline.")
            continue
        try:
            preds = ask_hf(headline)
            show(headline, preds["labels"])
        except Exception as e:
            e = e + 1
            print(colorama.Fore.RED + f"Error processing headline: {e}")
            print(colorama.Fore.RED + f"Thinking {e}s")
