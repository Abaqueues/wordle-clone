import pathlib
import random
from string import ascii_letters

def main():
    # Pre-process
    word = get_random_word()

    # Process (main loop)
    for guess_num in range(1, 7):
        guess = input(f"\nGuess {guess_num}: ").upper()

        show_guess(guess, word)
        if guess == word:
            print(f"Correct!\n The word was {word}!")
            break

    # Post-process
    else:
        game_over(word)

def get_random_word():
    wordlist = pathlib.Path(__file__).parent / "wordlist.txt"
    words = [
    word.upper()
    for word in wordlist.read_text(encoding="utf-8").split("\n") 
    if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]
    return random.choice(words)

def show_guess(guess, word):
    correctLetters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }
    misplacedLetters = set(guess) & set(word) - correctLetters
    wrongLetters = set(guess) - set(word)

    print("Correct Letters:", ", ".join(sorted(correctLetters)))
    print("Misplaced Letters:", ", ".join(sorted(misplacedLetters)))
    print("Wrong Letters:", ", ".join(sorted(wrongLetters)))
     
def game_over(word):
    print(f"\n--- Game Over ---")
    print(f"The word was {word}")

if __name__ == "__main__":
    main()