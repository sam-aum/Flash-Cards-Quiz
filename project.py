# add front and back cards
# add them to a csv
# quiz you randomly on each card
# if you give the right answer you get a point
# show final points
# goes through all the endings
# keeps track of mistakes for each ending
# can reset points



"""
Title: Flash Cards Quiz
Name: Sam Aum
Github: sam-aum
edX: S-Aum
City: Houston, TX, USA


"""
import sys
import csv
import random



def main():
    categories_added = choose_category()

    shuffled_deck = build_deck(categories_added)

    print(quiz(shuffled_deck))



# ADD CATEGORIES INTO THE DECK
def choose_category():
    category_list = ["nouns", "eimi", "verbs", "vocab_01"]

    for i, item in enumerate(category_list):
        print(f"[{i+1}]", item)

    categories_added = []

    while True:
        category = input('Add categories (enter "start" to start the quiz): ')

        if category == "start" and len(categories_added) > 0:
            break
        elif category not in category_list:
            print("Not a category")
        elif category in categories_added:
            print("Category already added")
        else:
            categories_added.append(category)

    return categories_added



# BUILD THE DECK
def build_deck(categories_added):
    deck = []

    for category in categories_added:
        function_call = category + "()"
        cards = eval(function_call)
        for card in cards:
            deck.append(card)

    shuffled_deck = random.sample(deck, len(deck))
    return shuffled_deck



# RUN THE QUIZ
def quiz(data_list):
    print("***Starting Quiz***")

    correct = 0
    incorrect = 0
    incorrect_list = []

    for i in range(len(data_list)):
        data = data_list[i]
        word = data["front"]
        correct_answer = data["back"].strip().lower()

        print(f"[Cards Remaining: {len(data_list)-i}]")
        answer = input(f"{word}: ").strip().lower()


        if answer == correct_answer:
            correct += 1
            print("***Correct +1***")
        else:
            print(f"***Incorrect +1, Correct Answer: {correct_answer}***")
            incorrect += 1
            incorrect_list.append(data)

    print("[Quiz Completed]")
    print(f"Correct: {correct}")
    print(f"Incorrect: {incorrect}")

    if incorrect == 0:
        return "***Perfect Score!***"
    else:
        new_test = input("Would you like to fix your mistakes? ").lower()
        if new_test == "yes":
            quiz(incorrect_list)
            return "***Great job!***"
        else:
            return "***Try Again Next Time!***"



# IMPORT CSV FILES / FLASH CARDS
def nouns():
    nouns = []

    try:
        with open("nouns.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nouns.append(row)
    except FileNotFoundError:
        sys.exit("File not found")

    return nouns


def eimi():
    eimis = []

    try:
        with open("eimi.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                eimis.append(row)
    except FileNotFoundError:
        sys.exit("File not found")

    return eimis


def verbs():
    print("TBD")


def vocab_01():
    vocab = []

    try:
        with open("vocab_01.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                vocab.append(row)
    except FileNotFoundError:
        sys.exit("File not found")

    return vocab



if __name__ == "__main__":
    main()

