# -*- coding: utf-8 -*-
# Zweck der Datei
# Eileen Niedenführ | Matrikelnr. 811770
# Datum


import scenes
import inventory
import alice_riddle
import animal_riddle
import time


class Game():
    def __init__(self):
        self.current_scene = scenes.hbf
        self.keep_playing = True
        self.inventory = inventory.Inventory()
        self.tardiness = False
        self.solved_alice = False
        self.solved_animal = False


    def play(self):
        """Game loop"""
        self.__init__()
        while self.keep_playing:
            print(self.current_scene.description)
            if self.current_scene == scenes.ticket_machine and self.solved_alice == False:
                start = time.time()
                alice_riddle.solve_riddle()
                stop = time.time()
                eval_time(stop, start, self)
                self.inventory.money.pay(5)
                self.inventory.add(inventory.Item("ticket"))
                self.solved_alice = True
            elif self.current_scene == scenes.library and self.solved_animal == False:
                animal_riddle.solve_riddle()
                self.inventory.add(inventory.Item("book"))
                self.solved_animal = True
            elif self.current_scene == scenes.book or self.current_scene == scenes.cafe:
                print("Would you like to try again tomorrow?(y/n)")
                answer= input("\n>")
                if answer == "y":
                    self.play()
                elif answer =="n":
                    self.keep_playing == False
                    break
                else:
                    print("Only y and n are accepted answers.")
            command = input("\n>").lower()
            self.current_scene.handle_input(self, command)



def eval_time(end, start, game):
    """Calculates the time spent solving the riddle and
    evaluates if the player will be late."""
    time_spent = end-start
    if time_spent > 120.0:
        game.tardiness = True

def check_for_riddle(current_scene):
    """Checks if the current scene requires solving a riddle"""
