import requests
url = "https://uselessfacts.jsph.pl/random.json?language=gb"
def get_random_fact():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(f"Did you know? {fact_data['text']}")
    else:
        print("Failed to fetch the useless fact, hey, but atleast we saved a thousand braincells from witnessing these useless facts")

while True:
    input("Press Enter to get a random fact and scar your counciousness or type 'q' to quit and save yourself...")
    if input().lower() == 'q':
        break
    get_random_fact()