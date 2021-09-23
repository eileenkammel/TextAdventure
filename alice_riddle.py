# -*- coding: utf-8 -*-
# Generates and executes the alice riddle for the ticket machine scene.
# Eileen Niedenführ | Matrikelnr. 811770
# 23.09.2021


import random
import nltk


def solve_riddle():
    """
    Let's the user guess a missing word in a sentence from it's POS-tag.
    A counter determines weather the correct guess has been
    made within three tries. Otherwise a new
    sentence/answer pair is generated.

    """
    tries = 0
    print("\nCan you guess the missing word based on it's POS-tag?\n")
    riddle_sentence, riddle_answer = get_riddle()
    print(riddle_sentence)
# The 'guess-loop' compares the user input to
#  the answer and adds to the counter.
    while tries < 3:
        answer_guess = input("\n>").lower()
        if answer_guess != riddle_answer.lower():
            if answer_guess == "###":
                print("\nYou continue without solving the riddle.\n")
                return
            else:
                print("\nThat's incorrect. Try again!\n")
                tries += 1
# If the user guesses correct within three times,
# the game will return to the main game-loop.
        elif answer_guess == riddle_answer.lower():
            print("\nYou guessed correct! You paid 5€ and the ticket was added to your bag. \
Now you can get the train.\n")
            return
# After three incorrect answers, the function
# calls itself to generate a new sentence/answer pair.
    print("Jet again incorrect. The word would have been *{}*. \
Let's try again!".format(riddle_answer.lower()))
    solve_riddle()


def get_riddle():
    """

    Generates the parameters for the riddle.
    Chooses a random sentence from 'Alice in Wonderland'.
    From this sentence a random word is replaced with it's
    POS-tag. The sentence woth the POS-tag and the replaced
    word are returned.

    """
# Fetching the raw text.
    alice_text = nltk.corpus.gutenberg.raw('carroll-alice.txt')
# Splitting it into sentences using the nltk method.
    alice_sentences = nltk.sent_tokenize(alice_text)
# Generating a random integer, to determine which index sentence is
# taken for the riddle and then tagging that sentence with the nltk method.
    x = random.randint(0, len(alice_sentences))
    random_sentence = alice_sentences[x].replace("\n", " ")
    tokenized_sentence = nltk.word_tokenize(random_sentence)
    tagged_tokens = nltk.pos_tag(tokenized_sentence, tagset="universal")
# Generating a second random integer to determine a word to replace.
    word_to_replace = random.randint(0, (len(tokenized_sentence)-1))
# Using enumerate(), the words in the sentence get added to
# the corresponding string: If the number of the word is not the prior
# generated random integer, it is added to the riddle_sentence string,
# otherweise te the riddle_answer string
    riddle_sentence = ""
    riddle_answer = ""
    for idx, (word, tag) in enumerate(tagged_tokens):
        if idx == word_to_replace:
            riddle_sentence += "<" + tag + "> "
            riddle_answer = word
        else:
            riddle_sentence += word + " "
# Making sure no empty answer is returned.
    if len(riddle_answer) == 0:
        get_riddle()
    else:
        return riddle_sentence, riddle_answer
