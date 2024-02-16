# CS50P Final Project
This is the Final Project in the HarvardX course CS50P - CS50's Introduction to Programming with Python

## Flash Card Quiz
#### [Video Demo](https://youtu.be/inKf5plKhS8)

#### Description:
This program allows users to upload flash cards using csv files, then runs a quiz of one or more flash card desks.

* `choose_category()`: This function prompts the user to select a csv file to open.  If the user enters a file that has not been created or a file that has already been entered, the user is prompted to add a valid file.  The user can begin the quiz by entering "start".

* `build_deck(categories_added)`: This function takes in a list of categories added, opens each csv file, combines them into one list, then shuffles the deck.  This function imports the `random` library to shuffle the deck.

* `quiz(data_list)`: This function takes in the shuffled deck, and shows the front of a card, prompting the user to guess the back.  If the user guesses correctly, a point is added.  If the user guesses incorrectly, the card is added to a mistakes list, and the correct answer is shown.  The correct and incorrect answers are added up and displayed at the end of the quiz.  Finally, the user is prompted to start a new quiz of only the incorrect cards.





## Installation
Use pip to install the package `pytest`
```
$ pip install pytest
```

## Usage
Use [python](https://www.python.org/) to run the application
```
$ python project.py
```
Use [pytest](https://docs.pytest.org/en/7.2.x/) to test the application
```
$ pytest test_project.py
```

