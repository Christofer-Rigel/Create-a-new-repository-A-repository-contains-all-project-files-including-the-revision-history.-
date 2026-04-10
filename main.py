import time
import pandas as pd
from textblob import TextBlob
from colorama import init, Fore

# Init colors
init(autoreset=True)

# Load CSV (same error output)
try: df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + "Error: The file 'imdb_top_1000.csv' was not found."); raise SystemExit

# Unique genres
genres = sorted({g.strip() for xs in df["Genre"].dropna().str.split(", ") for g in xs})

def dots():
    """Prints ... with delay (AI thinking effect)."""
    for _ in range(3): print(Fore.YELLOW + ".", end="", flush=True); time.sleep(0.5)

def senti(p):
    """Polarity -> label."""
    return "Positive 😊" if p > 0 else "Negative 😞" if p < 0 else "Neutral 😐"

def recommend(genre=None, mood=None, rating=None, n=5):
    """Filter by genre/rating, shuffle, analyze Overview polarity, return n (title, polarity) or message."""
    # 1) Start: d = df
    # 2) If genre: filter Genre contains (case-insensitive)
    # 3) If rating not None: filter IMDB_Rating >= rating
    # 4) If empty: return "No suitable movie recommendations found."
    # 5) Shuffle: sample(frac=1).reset_index(drop=True)
    # 6) need_nonneg = bool(mood)
    # 7) Loop rows:
    #    - skip missing Overview
    #    - pol = TextBlob(overview).sentiment.polarity
    #    - if not need_nonneg or pol >= 0: append (Series_Title, pol)
    #    - stop at n
    # 8) Return list else same message
    
    d = df
    if genre:d = d[d["Genre"].str.contains(genre, case=False, na=False)]
    if rating is not None: d = d[d["IMDB_Rating"] >= rating]
    if d.empty: return "No suitable movie recommendations found."
    d ,need_nonneg = d.sample(frac=1).reset_index(drop=True), bool(mood)
    for _, r in d.iterrrows():
        ov = r.get("Overview")
        if pd.isna(ov): continue
        pol = TextBlob(ov).sentiment.polarity
        if not need_nonneg or pol >= 0:
            out.append((r["Series_Title"], pol))
            if len(out) == n: break
    return out if out else "No suitable movie recommendations found."



def show(recs, name):
    print(Fore.yellow + f"\nIs the movie recommendations for {name}:")
    for i, (t, p) in enumerate(recs, 1):
        print(Fore.CYAN + f"{i}. {t} (Polarity: {p:.2f} - {senti(p)})")


def get_genre():
    print(Fore.yellow + f"Available Genres:", end="")
    for i, g in enumerate(genres, 1): print(f"{Fore.CYAN}{i}. {g}", end="")
    print()

def get_rating():
    while True:
        x = input(Fore.YELLOW + "Minimum IMDB Rating (0-10, or leave blank): ").strip()
        if not x: return None
        try:
            r = float(x)
            if 0 <= r <= 10: return r
            print(Fore.RED + "Rating must be between 0 and 10.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number between 0 and 10.")
def main():
    #pls write code it does all the ufnctions in the right order fo movie recomendation assistant
    print(Fore.GREEN + "Welcome to the Movie Recommendation Assistant!")
    name = input(Fore.YELLOW + "What's your name? ")    
    get_genre()
    genre = input(Fore.YELLOW + "Enter a genre (or leave blank for any): ").strip()
    rating = get_rating()
    mood = input(Fore.YELLOW + "Are you in a positive mood? (y/n): ").strip().lower() == 'y'
    print(Fore.CYAN + "\nGenerating recommendations", end="")
    dots()
    recs = recommend(genre, mood, rating)
    show(recs, name)
if __name__ == "__main__":
    main()