# -*- coding: utf-8 -*- 
# Zweck der Datei
# Eileen Niedenführ | Matrikelnr. 811770
# Datum


import random

class Scene():
    """Creates instances of environments the player can interact with"""
    def __init__(self,name):
        self.connections = {}
        self.name = name
        with open("Scenes/{}.txt".format(self.name)) as x:
            self.description= x.read()

    def handle_input(self, game, command):
        if command == "exit":
            game.keep_playing = False
        elif command == "inspect bag":
            print (game.inventory)



class Trainstation(Scene):
    def __init__(self, name):
        super().__init__(name)

    def handle_input(self, game, command):
        super().handle_input(game, command)
        if command == "get train":
            print ("\nDon't you think you're missing something? \
You need to buy a ticket first!")
        elif command == "buy ticket":
            game.current_scene = ticket_machine
        else:
            print("\nThat command is not helping you get on the train. \
Try another one.")



class TicketMachine(Scene):
    def __init__(self, name):
        super().__init__(name)
    
    def handle_input(self, game, command):
        super().handle_input(game, command)
        if command == "get train":
            if game.tardiness == False:
                game.current_scene = train1
            elif game.tardiness == True:
                game.current_scene = train2
        else:
            print("\nThat command is not helping you get on the train.\
Try another one.")





class TrainOnTime(Scene):
    def __init__(self, name):
        super().__init__(name)
    
    def handle_input(self, game, command):
        super().handle_input(game, command)
        if command == "get to golm":
            probability = random.randint(0,100)
            if probability >= 60:
                game.current_scene = ticket_check
            else:
                game.current_scene = library
        else:
            print("\nTry another command. Maybe something about your destination?")

class TicketCheck(Scene):
    def __init__(self, name):
        super().__init__(name)

    def handle_input(self, game, command):
        super().handle_input(game, command)
        if command == "show ticket":
            probability = random.randint(0,10)
            if probability > 5:
                game.current_scene = library
                print("\nYou show your ticket to the man and continue your journey.")
            else:
                game.current_scene = fee
        else:
            print("\nYour command should help you show your ticket to the man.\
Try another one.")

class Fee(Scene):
    def __init__(self, name):
        super().__init__(name)
    def handle_input(self, game, command):
        if command == "pay fee":
            game.current_scene = library
            game.inventory.money.pay(15)
            print("\nYou pay the fee of 15€ and continue your journey.")
        else:
            print("\nWe all hate paying fees! Nonetheless you should command the fee to be paid.")


class TrainLate(Scene):
    def __init__(self, name):
        super().__init__(name)
    def handle_input(self,game,command):
        super().handle_input(game, command)
        if command == "get to golm":
            game.current_scene = cafe
        else:
            print("\nTry another command. Maybe something about your destination?")


class Library(Scene):
    def __init__(self, name):
        super().__init__(name)
    def handle_input(self, game, command):
        super().handle_input(game, command)
        if command == "read book":
            game.current_scene = book
        elif command == "get coffee":
            if game.inventory.money.value > 0:
                game.current_scene = cafe
            else:
                print ("\nThat stupid fee ate up all your money. \
Sorry, no coffe for you.")
        else:
             print("\nMaybe you should check you bag to determine what to\
command next. Also, am I smelling coffee?")

class Cafe(Scene):
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

cafe = Cafe("cafe")

book = Book("book")

