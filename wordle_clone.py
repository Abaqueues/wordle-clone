import pathlib
import random
from string import ascii_letters

WORDLIST = pathlib.Path("wordlist.txt")

words = [
    word.upper()
    for word in WORDLIST.read_text(encoding="utf-8").split("\n") 
    if len(word) == 5 and all(letter in ascii_letters for letter in word)
]

word = random.choice(words)

for guess_num in range(1, 7):
    guess = input("Guess a word: ").upper()
    print("Guess " + str(guess_num) + ": " + guess)
    if guess == word:
        print("Correct!")
        break

    correctLetters = {letter for letter, correct in zip(guess, word) if letter == correct}
    misplacedLetters = set(guess) & set(word) - correctLetters
    wrongLetters = set(guess) - set(word)

    print("Correct Letters:", ", ".join(sorted(correctLetters)))
    print("Misplaced Letters:", ", ".join(sorted(misplacedLetters)))
    print("Wrong Letters:", ", ".join(sorted(wrongLetters)))

    if guess_num == 6:
            print("Game Over")
            print(f"The word was {word}")


