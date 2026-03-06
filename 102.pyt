import colorama
from colorama import Fore,Style
from textblob import TextBlob
colorama.init()
print(f"{Fore.CYAN}Welcome to LYNX PROTOTYPE-ALPHA-1{Style.RESET_ALL}")

#Line 8 houses the code for conversation history
conversation_history = []
text: str
polarity: float
sentiment_type: str
user_name = input(f"{Fore.YELLOW}Please enter your name: {Style.RESET_ALL}")
if user_name.strip() == "":#this will make sure the username will be set to a default ... Such as LYSER
    user_name = "LYSER"
print(f"{Fore.GREEN}Hello, {user_name}! How can I assist you today?{Style.RESET_ALL}")
#Now it will analye the sentiment of the user's input and respond accordingly
while True:
    text: str
    polarity: float
    sentiment_type: str
    for idx, (text, polarity, sentiment_type) in enumerate(conversation_history,start=1):
        print(f"{Fore.MAGENTA}{idx}. {text} (Polarity: {polarity}, Sentiment: {sentiment_type}){Style.RESET_ALL}")
    user_input = input(f"{Fore.YELLOW}You: {Style.RESET_ALL}")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print(f"{Fore.CYAN}Goodbye, {user_name}! Have a great day!{Style.RESET_ALL}")
        break
    # Analyze sentiment
    blob = TextBlob(user_input)
    sentiment_type: str
    if sentiment_type > 0:
        print(f"{Fore.GREEN}LYNX: I'm glad to hear that!{Style.RESET_ALL}")
    elif sentiment_type < 0:
        print(f"{Fore.RED}LYNX: I'm sorry to hear that. Is there anything I can do to help?{Style.RESET_ALL}")
    else:
        print(f"{Fore.BLUE}LYNX: I see. Can you tell me more about it?{Style.RESET_ALL}")
polarity = TextBlob(user_input).sentiment.polarity
if polarity > 0.25:
    sentiment_type = "positive"
    color = Fore.GREEN
    emoji = "😊"
elif polarity < -0.25:
    sentiment_type = "negative"
    color = Fore.RED
    emoji = "😞" 
else:
    sentiment_type = "neutral"
    color = Fore.BLUE
    emoji = "😐"