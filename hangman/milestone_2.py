import random


print("Welcome to the Word Guess Game!")
word_list = ["Banana", "Kiwi", "Strawberry", "Papaya", "Mango"]
word = random.choice(word_list)

guess = input("Guess a single letter: ").lower()

if len(guess) == 1 and guess.isalpha():
    # Valid input
    if guess in word.lower():
     print("Good guess!")

else: 
    print("Invalid letter. Please, enter a single alphabetical character.")






