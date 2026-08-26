import requests
from config import api_key

MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}"
HEADERS = {"Authorization": f"Bearer {api_key}"}

PAIRS = [
    ("Plants make food using sunlight, water, and carbon dioxide.",
     "Plants create their own food with light, water and CO2."),
    ("The water cycle includes evaporation, condensation, and precipitation.",
     "Water evaporates, forms clouds, and then falls as rain."),
    ("A fraction shows a part of a whole, like 1/2 of a pizza.",
     "Fractions represent pieces of something, like half a pizza."),
    ("Python lists can store many values in one variable.",
     "A list in Python keeps multiple items together in one place."),
    ("Rome is the capital of Italy and it has many ancient buildings.",
     "Italy's capital is Rome, famous for old historical monuments."),
    ("I love summer because I can play outside for longer.",
     "Summer is my favorite since I get extra time to play outdoors.")
]

def similarity(a: str, b: str) -> float:
    payload = {"inputs": {"source_sentence": a, "sentences": [b]}}
    r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)
    if not r.ok:
        raise RuntimeError(f"HF error: {r.status_code}: {r.text}")
    data = r.json()
    if isinstance(data, dict):
        raise RuntimeError(data.get("error", str(data)))
    return float(data[0])

def bar(score01: float) -> str:
    blocks = int((score01 * 100) // 10)
    return "█" * blocks + "░" * (10 - blocks)

def verdict(score01: float, threshold: float) -> str:
    if score01 >= threshold:
        return " Very high similarity"
    if score01 >= threshold - 0.15:
        return " Moderate similarity"
    return " Low similarity / Distinct"

def main():
    print("Paraphrase similarity checker")
    threshold = 0.80
    print(f"Rule: similarity ≥ {threshold}\n")
    
    while True:
        mode = input("Enter mode ('demo', 'custom', 'exit'): ").strip().lower()
        if mode == "exit":
            print("Exiting program.")
            break
        elif mode == "demo":
            for i, (a1, a2) in enumerate(PAIRS[:5], 1):
                s = similarity(a1, a2)
                pct = round(s * 100, 1)
                print(f"\n{i}) A1: {a1}\n   A2: {a2}")
                print(f"   Similarity: {pct}% [{bar(s)}]{verdict(s, threshold)}")
        elif mode == "custom":
            a1 = input("Sentence 1: ").strip()
            a2 = input("Sentence 2: ").strip()
            if not a1 or not a2:
                print("Both sentences are required.")
                continue
            s = similarity(a1, a2)
            pct = round(s * 100, 1)
            print(f"\nSimilarity: {pct}% [{bar(s)}]{verdict(s, threshold)}\n")
        else:
            print("Please type: demo, custom, or exit.\n")

if __name__ == "__main__":
    main()