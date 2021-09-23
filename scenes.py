# -*- coding: utf-8 -*-
# Creates all scenes for the game and how they handle input.
# Eileen Niedenführ | Matrikelnr. 811770
# 23.09.2021


import random

# Creating a super class for all scenes of the game and a class
# for each unique scene which inherits from the super class.


class Scene():
    """
    Super class for the scenes.
    """
    def __init__(self, name):
        """
        Instances of class will get initialized with
        description read out of a file equal to their name.
        """
        self.name = name
        with open("Scenes/{}.txt".format(self.name)) as description:
            self.description = description.read()

    def handle_input(self, game, command):
        """
        Determines how to handle input that's the \
        same for every scene. Also handles invalid input\
        and prevent the scene description from being printed\
        after the first time.

        Keyword arguments:
        game -- current instance of the game class
        command -- user input
        """
        if command == "exit":
            game.keep_playing = False
        elif command == "inspect bag":
            print(game.inventory)
            game.skip_description = True
        else:
            print("\nThat command is \
not helping you get along with your task.")
            game.skip_description = True


class Trainstation(Scene):
    """
    Class for the first scene of the game.
    Inherits from Scene().
    """
    def __init__(self, name):
        super().__init__(name)

    def handle_input(self, game, command):
        """
        Determines how to handle input that's unique \
        to that scene. Prevents the scene description from being printed\
        after the first time. If none of the defined unique input is given, \
        the handle_input() function of the super class is called.

        Keyword arguments:
        game -- current instance of the game class
        command -- user input
        """
        if command == "get train":
            print("\nDon't you think you're missing something? \
You need to buy a ticket first!")
            game.skip_description = True
        elif command == "buy ticket":
            game.current_scene = ticket_machine
        else:
            super().handle_input(game, command)


class TicketMachine(Scene):
    """
    Class for the first riddle scene of the game.
    Inherits from Scene().
    """
    def __init__(self, name):
        super().__init__(name)

    def handle_input(self, game, command):
        """
        Determines how to handle input that's unique \
        to that scene. Prevents the scene description from being printed\
        after the first time. If none of the defined unique input is given, \
        the handle_input() function of the super class is called.

        Keyword arguments:
        game -- current instance of the game class
        command -- user input
        """
        if command == "get train":
            if game.tardiness is False:
                game.current_scene = train1
            elif game.tardiness is True:
                game.current_scene = train2
        else:
            super().handle_input(game, command)


class TrainOnTime(Scene):
    """
    Class for the first, on time train scene of the game.
    Inherits from Scene().
    """
    def __init__(self, name):
        super().__init__(name)

    def handle_input(self, game, command):
        """
        Determines how to handle input that's unique \
        to that scene. Prevents the scene description from being printed\
        after the first time. If none of the defined unique input is given, \
        the handle_input() function of the super class is called.

        Keyword arguments:
        game -- current instance of the game class
        command -- user input
        """
        if command == "get to golm":
            probability = random.randint(0, 100)
            if probability >= 60:
                game.current_scene = ticket_check
            else:
                game.current_scene = library
        else:
            super().handle_input(game, command)


class TicketCheck(Scene):
    """
    Class for the ticke check scene of the game.
    Inherits from Scene().
    """
    def __init__(self, name):
        super().__init__(name)

    def handle_input(self, game, command):
        """
        Determines how to handle input that's unique \
        to that scene. Prevents the scene description from being printed\
        after the first time. If none of the defined unique input is given, \
        the handle_input() function of the super class is called.

        Keyword arguments:
        game -- current instance of the game class
        command -- user input
        """
        if command == "show ticket":
            probability = random.randint(0, 10)
            if probability > 5:
                game.current_scene = library
                print("\nYou show your ticket \
to the man and continue your journey.")
            else:
                game.current_scene = fee
        else:
            super().handle_input(game, command)


class Fee(Scene):
    """
    Class for the pay fee scene of the game.
    Inherits from Scene().
    """
    def __init__(self, name):
        super().__init__(name)

    def handle_input(self, game, command):
        """
        Determines how to handle input that's unique \
        to that scene. Prevents the scene description from being printed\
        after the first time. If none of the defined unique input is given, \
        the handle_input() function of the super class is called.

        Keyword arguments:
        game -- current instance of the game class
        command -- user input
        """
        if command == "pay fee":
            game.current_scene = library
            game.inventory.money.pay(15)
            print("\nYou pay the fee of 15€ and continue your journey.")
        else:
            super().handle_input(game, command)


class TrainLate(Scene):
    """
    Class for the second, late train scene of the game.
    Inherits from Scene().
    """
    def __init__(self, name):
        super().__init__(name)

    def handle_input(self, game, command):
        """
        Determines how to handle input that's unique \
        to that scene. Prevents the scene description from being printed\
        after the first time. If none of the defined unique input is given, \
        the handle_input() function of the super class is called.

        Keyword arguments:
        game -- current instance of the game class
        command -- user input
        """
        if command == "get to golm":
            game.current_scene = cafe
        else:
            super().handle_input(game, command)


class Library(Scene):
    """
    Class for the second riddle scene of the game.
    Inherits from Scene().
    """
    def __init__(self, name):
        super().__init__(name)

    def handle_input(self, game, command):
        """

        Determines how to handle input that's unique \
        to that scene. Prevents the scene description from being printed\
        after the first time. If none of the defined unique input is given, \
        the handle_input() function of the super class is called.

        Keyword arguments:
        game -- current instance of the game class
        command -- user input

        """
        if command == "read book":
            game.current_scene = book
        elif command == "get coffee":
            if game.inventory.money.value > 0:
                game.current_scene = cafe2
            else:
                print("\nThat stupid fee ate up all your money. \
Sorry, no coffe for you.")
                game.skip_description = True
        else:
            super().handle_input(game, command)


class CafeLate(Scene):
    """
    Class for one of the possible end scenes.
    Inherits from Scene().
    """
    def __init__(self, name):
        super().__init__(name)


class CafeOnTime(Scene):
    """
    Class for one of the possible end scenes.
    Inherits from Scene().
    """
    def __init__(self, name):
        super().__init__(name)


class Book(Scene):
    """
    Class for one of the possible end scenes.
    Inherits from Scene().
    """
    def __init__(self, name):
        super().__init__(name)


# Creating the instances of each class needed for the game.

hbf = Trainstation("hbf")

ticket_machine = TicketMachine("ticket machine")

train1 = TrainOnTime("train1")

train2 = TrainLate("train2")

ticket_check = TicketCheck("check")

fee = Fee("fee")

library = Library("library")

cafe = CafeLate("cafe")

cafe2 = CafeOnTime("cafe2")

book = Book("book")
