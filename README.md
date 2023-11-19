# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

Tnis is my first attempt at creating a game using Python - part of my cloud engineering course at AiCore.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Description
The Hangman Game Project is an evolving Hangman game that starts as a simple guessing game. It randomly selects a fruit from a predefined list of five fruits, and the player is prompted to guess a letter from the chosen fruit. The aim of the project is to progressively build upon the basic game, introducing new features and challenges.

### Project Goals
- Build a foundational Hangman game
- Expand the game's complexity over time
- Provide an interactive and enjoyable gaming experience

I will start off with conditional statements to create a basic version of the Hangman game that asks for user input and validates if the input is valid before checking whether the user's input is a correct guess.

#### Defining methods

- ask_for_input
- check_guess
- update_word_guessed
- play_game

These methods shield the user from the complexities of the game's internal mechanics, promoting a clear and simplified interaction model. Abstraction allows for a more straightforward understanding of the game's functionality and facilitates future enhancements without impacting the external interface.

#### Building a class

Finally, introduces a Hangman class, encapsulating the game's logic and functionality. The class includes methods for handling user input, checking guesses, updating the word state, and orchestrating the game loop.

Through the use of abstraction, the Hangman Game Project achieves a modular and organized structure, promoting maintainability and ease of extension as the project evolves.

### What I Learned
Throughout the development of this project, I aim to enhance my programming skills, especially in areas related to game development, user input handling, and project evolution.

## Installation
To run the Hangman Game Project on your local machine, follow these installation instructions:

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/fredringrose/hangman420.git

## Usage

Execute the Hangman game by running the script. Follow the on-screen instructions to guess letters and try to uncover the chosen word.

## File Structure

hangman420/
│
├── hangman.py
├── README.md
├── .gitignore
│
└── 

## License

This project is licensed under the MIT License.





