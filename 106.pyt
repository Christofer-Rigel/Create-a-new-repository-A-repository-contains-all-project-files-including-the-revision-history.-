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
    "I asked my laptop for travel advice.It said: Try Camping.",
    "I traveled to learn Python.Turns out the snake wasn't part of the course.",
    "A developer went on vacation.He still pushed commits.Thats the joke.",
    "Why do programmers like traveling?Different environments.",
    "A programmer was coding C++ on a beach ...when he deleted his code since he put a c in it."
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
def Budjet_input_cheking():#This checks the users input ofr a budjet , and then uses it to cross refrence other countries travel budgets , for examply , the maldives is a high budget
    #there is an if and else , cheking if hte user has inputed low  meduim or high , if true , it will then ask the user for the budget amount , low medium or high, else if the user has not inputed low medium or high , it will then ask the user to input a valid budjet and then call the function again
    print(Fore.CYAN + "Travel bot: What is your budget for this trip? (low, medium, high)")
    budget = input(Fore.YELLOW + "You: ")   
    if budget in ["low", "medium", "high"]:
        print(Fore.GREEN + f"Travel bot: Based on your budget of {budget}, I will recommend destinations that fit within that range.")
        # Here you would add logic to recommend destinations based on the budget
        if budget == "low":
            print(Fore.GREEN + "Travel bot: For a low budget, I recommend visiting places like Thailand, Vietnam, or Portugal.")
        elif budget == "medium":
            print(Fore.GREEN + "Travel bot: For a medium budget, I recommend visiting places like Spain, Italy, or Greece.")
        elif budget == "high":
            print(Fore.GREEN + "Travel bot: For a high budget, I recommend visiting places like the Maldives, Bora Bora, or the Swiss Alps.")
    else:
        print(Fore.RED + "Travel bot: Please enter a valid budget (low, medium, high).")
        Budjet_input_cheking()
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
    "A nap fixes 90 percent of travel problems.",
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
def guide_to_harsh_other_continental_laws():
    print(Fore.YELLOW + "Travel bot: When traveling to different continents, be aware of local laws and customs. Always research the destination's regulations regarding visas, cultural norms, and prohibited items to avoid any legal issues during your trip.")
def main():#This will do all of the def dunctions like show help paking tips puns etc , to make the chatbot sequencial , it will say hello , ask your name , then do budget,,,crack a pun , show a few random tips and so forth
    print(Fore.CYAN + "Travel bot: Hello! I'm your travel assistant. What's your name?")
    name = input(Fore.YELLOW + "You: ")
def Cultural_tips():#facts such as in china , a red letter is but on the ground if a family's daughter dies unmarrier , these redl etters contain money...so if you pick one up , you need to marry the dead daughters spirit.abs
    Culture.tips = [
    "In Japan, it's considered rude to tip at restaurants. Instead, excellent service is expected as part of the experience.",
    "In many Middle Eastern countries, it's customary to greet with a handshake and a kiss on each cheek, but be sure to follow the lead of your host.",
    "In India, it's common to eat with your right hand, as the left hand is considered unclean. Always use your right hand for eating and greeting.",
    "In some cultures, such as in parts of Africa and the Middle East, it's considered disrespectful to show the soles of your feet. Be mindful of your body language when sitting or crossing your legs.",
    "In many Latin American countries, it's common to greet with a hug or a kiss on the cheek, even in professional settings. Don't be surprised if your business meeting starts with a warm embrace!",
    "In some cultures, such as in parts of Southeast Asia, it's customary to remove your shoes before entering someone's home. Always look for cues and follow the local customs."
    ]
def main():
    name = input(Fore.YELLOW + "Your name ( aliases are allowed ): ")
    print(Fore.GREEN + f"Travel bot: Nice to meet you, {name}! How can I assist you with your travel plans today? (Type 'help' for options)")
    while True:
        command = input(Fore.YELLOW + "You: ").strip().lower()
        if command == "recommend":
            recommend()   
        elif command == "joke":
            tell_joke()
        elif command == "packing tip":
            packing_tips()
        elif command == "help":
            show_help()
        elif command == "sos":
            sos_help()
        elif command == "laws":
            guide_to_harsh_other_continental_laws()
        elif command == "exit":
            print(Fore.CYAN + "Travel bot: Safe travels, goodbye!")
            break
        elif command == "cultural tips":
            Cultural_tips()
        else:
            print(Fore.RED + "Travel bot: Sorry, I didn't understand that command. Type 'help' for options.")
main()