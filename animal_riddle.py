
import random
from nltk.corpus import wordnet as wn


def solve_riddle():
    tries = 0
    print("\nCan you guess the animal?\n")
    definition, animal = get_riddle()
    print(definition)
    while tries < 3:
        answer_guess = input("\n>").lower()
        if answer_guess != animal:
            print("\nThat's incorrect. Try again!\n")
            tries += 1
        elif answer_guess == animal:
            print("\nYou guessed correct!\n")
            return
    print("\nJet again incorrect.\
The animal would have been *{}*. Let's try again!\n".format(animal))
    solve_riddle()


def get_riddle():
    """Generates the parameters for the riddle.
    Returns a random animal from the animals.csv file
    and the corresponding definition of that animal from wordnet."""
    with open("animals.csv") as animals:
        animal_list = animals.readlines()
        animal_choice = random.randint(0, (len(animal_list)-1))
        animal = animal_list[animal_choice].strip().lower()
        definition = wn.synset(animal + ".n.01").definition()
        return definition, animal
