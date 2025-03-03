import random

# List of words for the game
words = ["python", "hangman", "programming", "developer", "challenge"]

# Choose a random word
word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = 6  # Number of incorrect guesses allowed
guessed_letters = []

print("Welcome to Hangman!")

while attempts > 0 and "_" in guessed_word:
    print("\nCurrent word: " + " ".join(guessed_word))
    print(f"Incorrect attempts left: {attempts}")
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a valid single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good job! That letter is in the word.")
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

if "_" not in guessed_word:
    print(f"\nCongratulations! You guessed the word: {word}")
else:
    print(f"\nGame over! The word was: {word}")
