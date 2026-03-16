import re,random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Maldives", "Bora Bora", "Maui", "Phuket", "Seychelles"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas", "Andes", "Dolomites"],
    "cities": ["Paris", "Tokyo", "New York", "Barcelona", "Rome"],
    "adventure": ["Costa Rica", "New Zealand", "Iceland", "Peru", "South Africa"],
    "cultural": ["Kyoto", "Marrakech", "Istanbul", "Cairo", "Athens"]
}
jokes = [
    "I tried to debug my travel app while flying…Turns out the real bug was the airplane mode.",
    "Why did the programmer bring a suitcase to the IDE?Because he heard it supports Java packages.",
    "I wrote code while backpacking…Now its called Git commit-ment issues.",
    "Why did the developer get lost in the airport?He kept looking for the terminal but opened VS Code instead.",
    "I asked my laptop for travel advice.It said: Try C:\ amping."
    "I traveled to learn Python.Turns out the snake wasn't part of the course.",
    "A developer went on vacation.He still pushed commits.Thats the joke.",
    "Why do programmers like traveling?Different environments."
    "Why did the programmer delete his custom os , he accidently put a 'c' in it."
]
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())
def recommend():
    print(Fore.CYAN + "Travel bot: Where would you like to travel? (beaches, mountains, cities, adventure, cultural)")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)
    if preference in destinations:
        recommendation = random.choice(destinations[preference])
        print(Fore.GREEN + f"Travel bot: Based on your preference for {preference}, I recommend visiting {recommendation}!")
    else:
        print(Fore.RED + "Travel bot: Sorry, I don't have recommendations for that category. Please choose from beaches, mountains, cities, adventure, or cultural.")
def tell_joke():
    joke = random.choice(jokes)
    print(Fore.MAGENTA + f"Travel bot: HerE iS a TiP fOR yOu : {joke}")
def packing_tips():
    tips = [
    "Pack light and versatile clothing to save space in your luggage.",
    "Don't forget to bring a universal adapter for your electronics.",
    "Roll your clothes instead of folding to maximize space.",
    "Always pack a small first aid kit for emergencies.",
    "Bring a reusable water bottle to stay hydrated while traveling.",
    "Keep digital copies of important documents like your passport.",
    "Download offline maps in case you lose internet access.",
    "Bring snacks for long travel days.",
    "Wear your bulkiest shoes during travel to save suitcase space.",
    "Label your luggage clearly.",
    "Always keep a pen with you for forms.",
    "Check the weather before packing.",
    "Carry a small power bank for your phone.",
    "Pack an extra pair of socks in your carry-on.",
    "Use packing cubes to stay organized.",
    "Bring earplugs for noisy environments.",
    "Always double-check your passport before leaving home.",
    "Take pictures of your luggage in case it gets lost.",
    "Keep valuables in your carry-on bag.",
    "Try local food whenever possible.",
    "Learn a few basic phrases of the local language.",
    "Keep some local currency with you.",
    "Download translation apps before traveling.",
    "Wear comfortable clothes during flights.",
    "Set travel alerts for your bank cards.",
    "Bring a lightweight jacket even in warm climates.",
    "Stretch during long flights to avoid stiffness.",
    "Pack a small laundry bag for dirty clothes.",
    "Use zip bags for liquids to avoid spills.",
    "Check baggage restrictions before heading to the airport.",
    "Set an alarm for early flights.",
    "Take breaks when exploring to avoid exhaustion.",
    "Always carry hand sanitizer.",
    "Keep emergency contact information handy.",
    "Photograph parking spots if you leave your car at the airport.",
    "Save your accommodation address offline.",
    "Drink water regularly while traveling.",
    "Avoid overpacking souvenirs at the start of the trip.",
    "Respect local customs and traditions.",
    "Wake up early to beat tourist crowds.",
    "Bring sunglasses for sunny destinations.",
    "Keep a small notebook for memories.",
    "Don't trust weather apps completely. They lie sometimes.",
    "If you get lost, pretend you're exploring on purpose.",
    "Always blame jet lag for your bad decisions.",
    "Eat dessert first. You're on vacation.",
    "Take photos, but also enjoy the moment.",
    "A nap fixes 90% of travel problems.",
    "Airplane food is a mystery science experiment.",
    "If Google Maps fails, follow the person who looks confident.",
    "Never underestimate the power of snacks.",
    "Your suitcase will always be heavier on the way back.",
    "Souvenirs are just expensive dust collectors.",
    "Airport chairs are designed by people who hate humans.",
    "Traveling teaches patience… mostly while waiting in lines.",
    "Hotel pillows are either clouds or bricks.",
    "If your phone battery dies, congratulations, you're in 1998.",
    "The best stories usually start with 'we got lost'.",
    "Always check if the door is locked… then check again.",
    "If you forgot something, buy it there and call it a souvenir.",
    "Walking 20,000 steps suddenly feels normal while traveling.",
    "Your wallet disappears faster in tourist areas.",
    "Maps make sense until you actually use them.",
    "Jet lag is basically your body arguing with the sun.",
    "Some souvenirs exist purely to confuse airport security.",
    "You will take 200 photos and post 3.",
    "The hotel TV remote will always be confusing.",
    "You will forget at least one thing at the hotel.",
    "Travel rule #1: snacks improve everything."
]
    tip = random.choice(tips)
    print(Fore.BLUE + f"Travel bot: Here's a packing tip for you: {tip}")
    print(Fore.BLUE + "Travel bot: Do you want another tip? (yes/no)")
    response = input(Fore.YELLOW + "You: ").strip().lower()
    if response == "yes":
        packing_tips()
def show_help():
    print("\nAvailable Commands:")
    print("recommend  - Get travel recommendations based on your preferences")
    print("joke       - Hear a travel-related joke")
    print("packing tip - Get useful packing tips for your trip")
    print("help       - Show available commands")
    print("exit       - Exit the chatbot")
def sos_help():
    print(Fore.RED + "Travel bot: It seems like you're in a tough spot. If you need immediate assistance, please contact local emergency services or reach out to someone you trust for help.")
def guide_to_harsh_other_continental_laws :
def guide_to_harsh_other_continental_laws():
    print(Fore.YELLOW + "Travel bot: When traveling to different continents, be aware of local laws and customs. Always research the destination's regulations regarding visas, cultural norms, and prohibited items to avoid any legal issues during your trip.")
def main():
    print(Fore.CYAN + "Welcome to the Travel Bot! How can I assist you today?")
    while True:
        user_input = input(Fore.YELLOW + "You: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input:
            recommend()
        elif "joke" in user_input:
            tell_joke()
        elif "packing tip" in user_input:
            packing_tips()
        elif user_input in ["exit", "quit"]:
            print(Fore.CYAN + "Travel bot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "Travel bot: I'm sorry, I didn't understand that. Please try again or type 'help' for options.")
