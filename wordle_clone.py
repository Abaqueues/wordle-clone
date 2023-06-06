import pathlib
import random
from string import ascii_letters

def main():
    # Pre-process
    words_path = pathlib.Path(__file__).parent / "wordlist.txt"
    word = get_random_word(words_path.read_text(encoding="utf-8").split("\n"))

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

def get_random_word(word_list):    
    """Selects a random five-letter word from the wordlist.txt file.
    
    ## Example:
    
    >>> get_random_word(["broke", "stop", "kn1ght'5"])
    'BROKE'
    """

    words = [
        word.upper()
        for word in word_list
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]
    return random.choice(words)

def show_guess(guess, word):
    """Display user's guess on the terminal and classify letters (i.e. correct, misplaced, wrong)
    
    ## Example:
    
    >>> show_guess("ANGEL", "CRANE")
    Correct Letters: 
    Misplaced Letters: A, E, N
    Wrong Letters: G, L
    """

    correctLetters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }
    misplacedLetters = set(guess) & set(word) - correctLetters
    wrongLetters = set(guess) - set(word)

    print("Correct Letters:", ", ".join(sorted(correctLetters)))
    print("Misplaced Letters:", ", ".join(sorted(misplacedLetters)))
    print("Wrong Letters:", ", ".join(sorted(wrongLetters)))
     
def game_over(word):
    """Display the 'Game Over' message and the random word.
    
    ## Example:
    
    >>> game_over("ANGEL")
    <BLANKLINE>
    --- Game Over ---
    The word was ANGEL
    """

    print(f"\n--- Game Over ---")
    print(f"The word was {word}")

if __name__ == "__main__":
    main()