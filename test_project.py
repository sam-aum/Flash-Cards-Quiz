from project import choose_category, build_deck, quiz
import pytest


def test_choose_category():
    categories_added = ["nouns"]
    assert choose_category() == categories_added



def test_build_deck():
    categories_added = ["eimi"]
    deck = build_deck(categories_added)

    for category in categories_added:
        cards = eval(category + '()')
        assert all(card in deck for card in cards)


def test_quiz():
    data_list = [{"front": "question1", "back": "correct_answer"}]
    assert quiz(data_list) == "***Perfect Score!***"

