# HANGMAN GAME WITH WHILE Loop

import random
import time

print("Welcome to Hangman Game !!!\n")

wordlist=["hacker","bounty","vdp","hall of fame","pentester","developer"]

print("Randomly choosing a secret word  !!!")
time.sleep(2)

secret_word=random.choice(wordlist)
print("Converting secret word into '_' form ")
time.sleep(4)

# Empty list
list=[]

for letter in range(len(secret_word)):
    list += "_"
print(list)

print("\n")

num=0
game_over = False
while not game_over:
    guess = input("Guess a letter : ").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess :
            list[position]= letter
    if guess not in secret_word :
        num += 1
        guess_left = 5-num
        print(f"You have now only {guess_left} guess")
        if num>=5:
            print("You Lose Game Over!!!")

    print(list)

    if "_" not in list:
        print("You Won the Game !!!")
        game_over=True
