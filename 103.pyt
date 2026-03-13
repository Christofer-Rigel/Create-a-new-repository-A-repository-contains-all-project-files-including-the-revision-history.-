import time
import sys
init(autoreset=True)

# Global storage
conversation_history = []
sentiment_counts = {"positive": 0, "neutral": 0, "negative": 0}


# 1. Loading Animation
def show_processing_animation():
    animation = ["Analyzing.", "Analyzing..", "Analyzing..."]
    for i in range(3):
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
        time.sleep(0.5)
    print("\r", end="")


# 2. Sentiment Analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "positive"
        color = Fore.GREEN
    elif polarity < 0:
        sentiment = "negative"
        color = Fore.RED
    else:
        sentiment = "neutral"
        color = Fore.YELLOW

    sentiment_counts[sentiment] += 1
    conversation_history.append((text, sentiment, polarity))

    print(color + f"Sentiment: {sentiment.upper()} | Polarity Score: {polarity:.2f}" + Style.RESET_ALL)


# 3. Command Handler
def execute_command(command):
    global conversation_history, sentiment_counts

    if command == "summary":
        print("\nSentiment Summary:")
        print(Fore.GREEN + f"Positive: {sentiment_counts['positive']}")
        print(Fore.RED + f"Negative: {sentiment_counts['negative']}")
        print(Fore.YELLOW + f"Neutral: {sentiment_counts['neutral']}")

    elif command == "reset":
        conversation_history = []
        sentiment_counts = {"positive": 0, "neutral": 0, "negative": 0}
        print("All data has been reset.")

    elif command == "history":
        if not conversation_history:
            print("No history available.")
        else:
            print("\nConversation History:")
            for msg, sentiment, polarity in conversation_history:
                print(f"Message: {msg} | Sentiment: {sentiment} | Score: {polarity:.2f}")

    elif command == "help":
        print("\nAvailable Commands:")
        print("summary  - Show sentiment summary")
        print("reset    - Reset conversation history")
        print("history  - Show previous messages")
        print("help     - Show available commands")
        print("exit     - Exit chatbot")

    else:
        print("Unknown command. Type 'help' for options.")


# 4. Name Validation
def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if name.isalpha():
            return name
        else:
            print("Name must contain only alphabetic characters.")


# Final Report
def generate_final_report(username):
    filename = f"{username}_sentiment_analysis.txt"

    with open(filename, "w") as file:
        file.write("Sentiment Analysis Report\n")
        file.write("========================\n")
        file.write(f"Positive: {sentiment_counts['positive']}\n")
        file.write(f"Negative: {sentiment_counts['negative']}\n")
        file.write(f"Neutral: {sentiment_counts['neutral']}\n\n")

        file.write("Conversation History:\n")
        for msg, sentiment, polarity in conversation_history:
            file.write(f"{msg} | {sentiment} | {polarity:.2f}\n")

    print(f"\nReport saved as {filename}")


# 2. Main Chatbot Loop
def main():
    print("Welcome to the Sentiment Analysis Chatbot!")

    username = get_valid_name()
    print(f"Hello {username}! Type a sentence to analyze sentiment.")
    print("Type 'help' to see commands.\n")

    while True:
        user_input = input("> ").strip()

        if user_input.lower() == "exit":
            break

        if user_input.lower() in ["summary", "reset", "history", "help"]:
            execute_command(user_input.lower())
        else:
            show_processing_animation()
            analyze_sentiment(user_input)

    print("\nFinal Sentiment Summary:")
    execute_command("summary")

    generate_final_report(username)


if __name__ == "__main__":
    main()