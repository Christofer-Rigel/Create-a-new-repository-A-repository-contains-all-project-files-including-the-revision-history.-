import requests
def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Full JSON response: {response.json()}")
        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    else:
        return "Failed to retrieve joke just like how you failed to retrieve an A+ in gymnastics even though you are just 12 y/o."
def main():
    print("Welcome to the reason humans will never touch another star, or any star")
    while True:
        user_input = input("Press Enter to get a new reason, or type 'q''/''exit' to save your sanity and tears").strip().lower()

        if user_input in ("q", "exit"):
            print("Goodye, see how we forgot the b?Lets make sure we dont get stung anymore!")
            break
        joke = get_random_joke()
        print(joke)
if __name__ == "__main__":
    main()