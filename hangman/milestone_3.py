import random

word_list = ["Banana", "Kiwi", "Strawberry", "Papaya", "Mango"]
word = random.choice(word_list)

while True:
    guess = input("Guess a single letter: ").lower()

    def check_guess(word, guess):
        if len(guess) == 1 and guess.isalpha():
    # Valid input
            if guess in word.lower():
                print(f"Good guess! {guess} is in the word.")
            else: 
                print(f"Sorry, {guess} is not in the word. Try again")

        else:
            print("Please enter a valid single letter.")


    


