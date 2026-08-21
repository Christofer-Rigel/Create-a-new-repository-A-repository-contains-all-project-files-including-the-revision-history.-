import requests
import rickroll
from config import api_key
from colorama import Fore, Style, init
init(autoreset=True)
DEFAULT_MODEL = "google/pegasus-xsum"
def build_api_url(model_name):
    return f"https://api-inference.huggingface.co/models/{model_name}"
def query(payload, model_name=DEFAULT_MODEL):
    api_url = build_api_url(model_name)
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(api_url, headers=headers, json=payload)
    rickroll.play()
    return response.json()
def summerize_text(text, min_length, max_length, model_name=DEFAULT_MODEL):
    payload = {
        "inputs":text,
        "parameters": {"min_length": min_length, "max_length": max_length}
    }
    print(Fore.BLUE + Style.BRIGHT + f"\n???? Perform AI summerization using model:{model_name}, with a text u written so bad, me wondering if u r human or a robot vacuum with arms 💀")
    #rickroll.play()
    result = query(payload, model_name=model_name)
    if isinstance(result, list) and result and "summary_text" in result[0]:
        return result[0]["summary_text"]
    else:
        print(Fore.RED + "🩴 to 💻, Error in summarization response:", result, "Please check if ur human or litteraly a click-bot")
        rickroll.play()
        return None
if __name__ == "__main__":
    print(Fore.YELLOW + Style.BRIGHT + "????Hi there, whats ur name?💩?")
    user_name = input("Your 🧓 name:    ").strip()
    if not user_name:
        user_name = "🧓 danny"
    print(Fore.GREEN + f"Welcome, {user_name}! lets give ur text an ai-based existential crisis!!!YAY")
    print(Fore.YELLOW + Style.BRIGHT + "\n PLEASE ENTER ZA TEXT YOU WANT TO DESTROY")
    user_text = input("⊡⊤⊚⊑⋈⋀⋁⋛⋛⋚⋘⋙⋙⋙⋙⋙⋙⋙⋙")

    if not user_text:
        print(Fore.GREEN + "Ok, ur text is a gibberish sentence of unicode")
        user_text = "ꙮ ‽ ⎈ ⍼ ⟡ ⨁ ⨂ ⨀ ⎋ ⍎ ⍕ ⍜ ⍞ ⍟ ⌖ ⌖ ⌕ ⊿ ⌁ ⌂ ⌙ ⌨ ⌸ ⌹ ⌺ ⌻ ⌼ ⌽ ⌾ ⌿ ⍀ ⍁ ⍂ ⍃ ⍄ ⍅ ⍆ ⍇ ⍈ ⍉ ⍊ ⍋ ⍌ ⍍ ⍎ ⍏ ⍐ ⍑ ⍒ ⍓ ⍔ ⍕ ⍖ ⍗ ⍘ ⍙ ⍚ ⍛ ⍜ ⍝ ⍞ ⍟ ⍠ ⍡ ⍢ ⍣ ⍤ ⍥ ⍦ ⍧ ⍨ ⍩ ⍪ ⍫ ⍬ ⍭ ⍮ ⍯ ⍰ ⍱ ⍲ ⍳ ⍴ ⍵ ⍶ ⍷ ⍸ ⍹ ⍺ ⺍ ⺎ ⺏ ⺐ ⺑ ⺒ ⺓ ⺔ ⺕ ⺖ ⺗ ⺘"
    else:
        print(Fore.YELLOW + "\n Enter the model name u want (e.g., facebook/bart-large-cnn or leave it blank for useless google ai)")
        model_choice = input("Model name (leave now, blank is defaulted):").strip()
        if not model_choice:
            model_choice = DEFAULT_MODEL
            rickroll.play()
        print(Fore.YELLOW + "\n CHOOSE UR Txt ENDING METHOD: ")
        print("1. Standard destruction(Quick, concise and reads like your essay of interdimenisonal biology at 3am (aka fillets))")
        print("2. Enhanced destruction (More detailed and refines destruction, with extra 1000000000000000000000000 commas)")
        style_choice = input("Enter 1 or 2:  ").strip()
        if style_choice == "2":
            min_length = 80
            max_length = 200
            print(Fore.BLUE + "So you picked destruction, huh? Fine, go ahead. Don't blame me when your entire code reads like a biology thesis from an undergrad physicist at 3 am")
        else:
            min_length = 50
            max_length = 150
            print(Fore.BLUE + "Using standard summerIsation settings....atleast its not refined destruction....")
        summary = summerize_text(user_text, min_length, max_length, model_name=model_choice)
        if summary:
            print(Fore.BLUE + f"Using nonsense {user_name}")
            print(summary)
        else:
            print("Atleast this failed prompt matches ur B+ in chinese")
        