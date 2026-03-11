import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}Welcome to LYNX PROTOTYPE-ALPHA-1{Style.RESET_ALL}")

# conversation history
conversation_history = []

user_name = input(f"{Fore.YELLOW}Please enter your name: {Style.RESET_ALL}")

if user_name.strip() == "":
    user_name = "LYSER"

print(f"{Fore.GREEN}Hello, {user_name}! How can I assist you today?{Style.RESET_ALL}")

while True:

    # show history
    for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
        print(f"{Fore.MAGENTA}{idx}. {text} (Polarity: {polarity:.2f}, Sentiment: {sentiment_type}){Style.RESET_ALL}")

    user_input = input(f"{Fore.YELLOW}You: {Style.RESET_ALL}")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print(f"{Fore.CYAN}Goodbye, {user_name}! Have a great day!{Style.RESET_ALL}")
        break

    # analyze sentiment
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0.25:
        sentiment_type = "positive"
        color = Fore.GREEN
        emoji = "😊"
        print(f"{color}LYNX: I'm glad to hear that! {emoji}{Style.RESET_ALL}")

    elif polarity < -0.25:
        sentiment_type = "negative"
        color = Fore.RED
        emoji = "😞"
        print(f"{color}LYNX: I'm sorry to hear that. Is there anything I can do to help? {emoji}{Style.RESET_ALL}")

    else:
        sentiment_type = "neutral"
        color = Fore.BLUE
        emoji = "😐"
        print(f"{color}LYNX: I see. Can you tell me more about it? {emoji}{Style.RESET_ALL}")

    # save to history
    conversation_history.append((user_input, polarity, sentiment_type))