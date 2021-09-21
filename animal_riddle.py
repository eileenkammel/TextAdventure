# -*- coding: utf-8 -*-
# Generates and executes the animal riddle for the library scene.
# Eileen Niedenführ | Matrikelnr. 811770
# Datum


import random
from nltk.corpus import wordnet as wn


def solve_riddle():
    """
    Let's the user guess the animal from a description of it.
    A counter determines weather the correct guess has been
    made within three tries. Otherwise a new
    animal/description pair is generated.

    """
    tries = 0
    print("\nCan you guess the animal?\n")
# The get_riddle() function generates a
# rondom animal/despription pair.
    definition, animal = get_riddle()
# Checking if a riddle definition was generatet. If not,
# the function calls itself again to generate a new riddle.
    if len(definition) == 0:
        solve_riddle()
    print(definition)
# The 'guess-loop' compares the user input to
#  the animal and adds to the counter.
    while tries < 3:
        answer_guess = input("\n>").lower()
        if answer_guess != animal:
            if answer_guess == "###":
                print("\nYou continue without solving the riddle.\n")
                return
            else:
                print("\nThat's incorrect. Try again!\n")
                tries += 1
# If the user guesses correct within three times,
# the game will return to the main game-loop.
        elif answer_guess == animal:
            print("\nYou guessed correct! Finally the librarian is able to \
check out your book for you. You put it in your bag.\n")
            return
# After three incorrect answers, the function
# calls itself to generate a new animal/description pair.
    print("\nJet again incorrect.\
The animal would have been *{}*. Let's try again!\n".format(animal))
    solve_riddle()


def get_riddle():
    """
    Generates the parameters for the riddle.
    Returns a string with random animal name
    from the animals.csv fileand a string with
    the corresponding definition of that animal from wordnet.

    """
    with open("animals.csv") as animals:
        animal_list = animals.readlines()
        animal_choice = random.randint(0, (len(animal_list)-1))
        animal = animal_list[animal_choice].strip().lower()
        definition = ""
        # Making sure, that if there are synonyms,
        # the definition of the animal is used.
        # Taken and adaptet from the moodle forum.
        syns = wn.synsets(animal)
        for syn in syns:
            if syn.lexname() == "noun.animal":
                definition += syn.definition()
                break
        return definition, animal