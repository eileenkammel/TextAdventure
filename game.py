# -*- coding: utf-8 -*-
# Creates the game class and the method for executing the game.
# Eileen Niedenführ | Matrikelnr. 811770
# 23.09.2021


import scenes
import inventory
import alice_riddle
import animal_riddle
import time


class Game():
    """
    An instance of the game with set variables
    identical for the start point of each game run."

    """
    def __init__(self):
        self.current_scene = scenes.hbf
        self.keep_playing = True
        self.inventory = inventory.Inventory()
        self.tardiness = False
        self.solved_alice = False
        self.solved_animal = False
        # Makes sure that scene description is only printed once
        # when initially entering a scene. Is set to True
        # after giving input which does not result in change
        # of scene.
        self.skip_description = False

    def play(self):
        """
        Initializes the main game loop.

        """
        # Because the player can start a new game loop without
        # closing the file,the next codeline makes sure the
        # new game loop starts with the initial parameters.
        self.__init__()
        # After skipping a scene description the variable
        # will be set to default False.
        while self.keep_playing:
            if self.skip_description is True:
                self.skip_description = False
            else:
                print(self.current_scene.description)
            # Makes sure that the riddle gets only called at the right scene
            # and if it has not already been solved prior.
            if self.current_scene == scenes.ticket_machine and \
                    self.solved_alice is False:
                # Starting end ending a timer before and after the riddle and
                # calculating the time spent solving.
                start = time.time()
                alice_riddle.solve_riddle()
                stop = time.time()
                eval_time(stop, start, self)
                # Paying for the ticket, reducing the
                # value of the money instance in the inventory.
                self.inventory.money.pay(5)
                # creating an item instance and adding it
                # to the inventory.
                self.inventory.add(inventory.Item("ticket"))
                self.solved_alice = True
            # Makes sure that the riddle gets only called at the right scene
            # and if it has not already been solved prior.
            elif self.current_scene == scenes.library and \
                    self.solved_animal is False:
                animal_riddle.solve_riddle()
                # creating an item instance and adding it
                # to the inventory.
                self.inventory.add(inventory.Item("book"))
                self.solved_animal = True
                # Defining the endpoints of the game. Giving the user the
                # opportunitiy to start another loop or to close the game file.
            elif self.current_scene in [scenes.book, scenes.cafe, scenes.cafe2]:
                print("Would you like to try again tomorrow?(y/n)")
                answer = input("\n>")
                if answer == "y":
                    self.play()
                elif answer == "n":
                    self.keep_playing is False
                    self.skip_description = True
                    break
                else:
                    print("Only y and n are accepted answers.")
            # Accepting user input and handeling it based on current scene.
            command = input("\n>").lower()
            self.current_scene.handle_input(self, command)


def eval_time(end, start, game):
    """
    Calculates the time spent solving the riddle and
    evaluates if the player will be late.

    Keyword arguments:
    end -- stop time of the timer
    start -- start time of the timer
    game -- current instance of game class

    """
    time_spent = end-start
    if time_spent > 120.0:
        game.tardiness = True
