import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in range(len(self.word))]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def ask_for_input(self, guess):
        if len(guess) == 1 and guess.isalpha() and guess not in self.list_of_guesses:
            return True
        else:
            print("Invalid letter. Please, enter a single alphabetical character that you haven't guessed before.")
            return False

    def check_guess(self, guess):
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.update_word_guessed(guess)
        else:
            print(f"Sorry, {guess} is not in the word. Try again")
            print(f"You have {num_lives} lives left")
            self.num_lives -= 1

    def update_word_guessed(self, guess):
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess

    def play_game(self):
        print("Welcome to the Hangman Game!")
        while True:
            print(f"Word to guess: {' '.join(self.word_guessed)}")
            guess = input("Guess a single letter: ").lower()
            
            if not self.ask_for_input(guess):
                continue  # Continue the loop if the input is not valid
            
            self.list_of_guesses.append(guess)
            self.check_guess(guess)

            if self.word_guessed.count('_') == 0:
                print(f"Congratulations! You guessed the word: {self.word}")
                break

            if self.num_lives == 0:
                print(f"Game over! The word was: {self.word}")
                break

# Example usage with guessing the fruit
word_list = ["banana", "kiwi", "strawberry", "papaya", "mango"]
hangman_game = Hangman(word_list)
hangman_game.play_game()
