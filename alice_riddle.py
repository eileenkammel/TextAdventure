# -*- coding: utf-8 -*- 
# Zweck der Datei
# Eileen Niedenführ | Matrikelnr. 811770
# Datum


import random
import re
import nltk


def solve_riddle():
    tries = 0
    print("\nCan you guess the missing word based on it's POS-tag?\n")
    riddle_sentence, riddle_answer = get_riddle()
    print(riddle_sentence)
    while tries < 3:
        answer_guess = input(">")
        if answer_guess != riddle_answer:
            print("\nThat's incorrect. Try again!\n")
            tries += 1
        elif answer_guess == riddle_answer:
            print("\nYou guessed correct! The ticket was added to your bag. \
Now you can gat the train.\n")
            return        
    print("Jet again incorrect. The word would have been *{}*. Let's try again!".format(riddle_answer))
    solve_riddle()
    

def get_riddle():
    
    alice_text = nltk.corpus.gutenberg.raw('carroll-alice.txt')
    alice_sentences = nltk.sent_tokenize(alice_text)
    x = random.randint(0,len(alice_sentences))
    random_sentence = alice_sentences[x].replace("\n"," ")
    tokenized_sentence = nltk.word_tokenize(random_sentence)
    tagged_tokens =  nltk.pos_tag(tokenized_sentence, tagset="universal")

    if len(tokenized_sentence) != len(tagged_tokens):
        print("Well this should never happen, but we are still here....HOW?!?!")

    word_to_replace = random.randint(0, (len(tokenized_sentence)-1))

    riddle_sentence = ""
    riddle_answer = ""
    for idx, (word, tag) in enumerate(tagged_tokens):
        if idx == word_to_replace:
            riddle_sentence += "<" + tag + "> "
            riddle_answer = word
        else:
            riddle_sentence += word + " "
    if len(riddle_answer) == 0:
        get_riddle()
    else:
        return riddle_sentence, riddle_answer



