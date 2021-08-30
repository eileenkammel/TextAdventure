# -*- coding: utf-8 -*-
# Zweck der Datei
# Eileen Niedenführ | Matrikelnr. 811770
# Datum


import random
from re import S


class Scene():
    """Creates instances of environments the player can interact with"""
    def __init__(self, name):
        self.connections = {}
        self.name = name
        with open("Scenes/{}.txt".format(self.name)) as description:
            self.description = description.read()

    def handle_input(self, game, command):
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
    def __init__(self, name):
        super().__init__(name)

    def handle_input(self, game, command):
        if command == "get train":
            print("\nDon't you think you're missing something? \
You need to buy a ticket first!")
            game.skip_description = True
        elif command == "buy ticket":
            game.current_scene = ticket_machine
        else:
            super().handle_input(game, command)


class TicketMachine(Scene):
    def __init__(self, name):
        super().__init__(name)

    def handle_input(self, game, command):
        if command == "get train":
            if game.tardiness is False:
                game.current_scene = train1
            elif game.tardiness is True:
                game.current_scene = train2
        else:
            super().handle_input(game, command)


class TrainOnTime(Scene):
    def __init__(self, name):
        super().__init__(name)

    def handle_input(self, game, command):
        if command == "get to golm":
            probability = random.randint(0, 100)
            if probability >= 60:
                game.current_scene = ticket_check
            else:
                game.current_scene = library
        else:
            super().handle_input(game, command)


class TicketCheck(Scene):
    def __init__(self, name):
        super().__init__(name)

    def handle_input(self, game, command):
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
    def __init__(self, name):
        super().__init__(name)

    def handle_input(self, game, command):
        if command == "pay fee":
            game.current_scene = library
            game.inventory.money.pay(15)
            print("\nYou pay the fee of 15€ and continue your journey.")
        else:
            super().handle_input(game, command)


class TrainLate(Scene):
    def __init__(self, name):
        super().__init__(name)

    def handle_input(self, game, command):
        if command == "get to golm":
            game.current_scene = cafe
        else:
            super().handle_input(game, command)


class Library(Scene):
    def __init__(self, name):
        super().__init__(name)

    def handle_input(self, game, command):
        if command == "read book":
            game.current_scene = book
        elif command == "get coffee":
            if game.inventory.money.value > 0:
                game.current_scene = cafe
            else:
                print("\nThat stupid fee ate up all your money. \
Sorry, no coffe for you.")
                game.skip_description = True
        else:
            super().handle_input(game, command)


class CafeLate(Scene):
    def __init__(self, name):
        super().__init__(name)


class CafeOnTime(Scene):
    def __init__(self, name):
        super().__init__(name)


class Book(Scene):
    def __init__(self, name):
        super().__init__(name)


hbf = Trainstation("hbf")

ticket_machine = TicketMachine("ticket machine")

train1 = TrainOnTime("train 1")

train2 = TrainLate("train 2")

ticket_check = TicketCheck("check")

fee = Fee("fee")

library = Library("library")

cafe = CafeLate("cafe")

cafe2 = CafeOnTime("cafe2")

book = Book("book")
