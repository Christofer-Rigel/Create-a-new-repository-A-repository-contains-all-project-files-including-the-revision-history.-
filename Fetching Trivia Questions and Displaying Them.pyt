import requests

import random

import html #fix or forereinstalalation cycle pip

#import rickroll
EDUCATION_CATAGORY_ID = 9
API_URL = f"https://opentdb.com/api.php?amount=1&catagory={EDUCATION_CATAGORY_ID}&type=multiple"

def get_education_question():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        if data['response_code'] == 0 and data['results']:
            return data['results']

    return None

score = 0

print("Welcome to the Educational QUIZ!\n")

def run_quiz():

    questions = get_education_question()
    if not questions:
        print("Failed to fetch educational questions, auto-opening a help video")
        #rickroll.roll()
        return

    for i, q in enumerate(questions, 1):
        question = html.unescape(q['question'])
        correct = [html.unescape(a) for a in q['incorrect_answers']]
        incorrect = [html.unescape(a) for a in q['incorrect_answers']]
        options = incorrect_answers + [correct]
        random.shuffle(options)
        print(f"Question {i}: {question}")
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {options}")
            while True:
                try:
                    choice = int(input("\n YOUR ANSWER (1-4):[]"))
                    if 1 <= choice <= 4:
                        break
                except ValueError:
                    pass
                    print("Invalid input! Please enter 1-4")
                    #rickroll.roll()
    
    print(f"final Score:{score}/(len(question))")
run_quiz()