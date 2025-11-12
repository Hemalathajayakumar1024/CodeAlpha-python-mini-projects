import random

# List of predefined words
words = ["apple", "banana", "orange", "grapes", "mango"]

# Randomly choose one word from the list
secret_word = random.choice(words)
guessed_letters = []  # Store correctly guessed letters
tries = 6  # Limit of incorrect guesses

print("🎯 Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")
print("_ " * len(secret_word))

# Game loop
while tries > 0:
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("❗ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # If guessed letter is in the secret word
    if guess in secret_word:
        print("✅ Good guess!")

    else:
        tries -= 1
        print(f"❌ Wrong guess! Tries left: {tries}")

    # Display current progress
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word)

    # Check if player has guessed all letters
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word correctly!")
        break

# If player runs out of tries
if tries == 0:
    print(f"\n😞 You ran out of tries. The word was '{secret_word}'.")