import contextlib
import pathlib
import random
from string import ascii_letters, ascii_uppercase

from rich.console import Console
from rich.theme import Theme

console = Console(width=40, theme=Theme({"warning": "red on yellow"}))

NUM_LETTERS = 5
NUM_GUESSES = 6
WORDS_PATH = pathlib.Path(__file__).parent / "wordlist.txt"

def main():
    # Pre-process
    words_path = pathlib.Path(__file__).parent / "wordlist.txt"
    word = get_random_word(words_path.read_text(encoding="utf-8").split("\n"))
    guesses = ["_" * NUM_LETTERS] * NUM_GUESSES

    # Process (main loop)
    with contextlib.suppress(KeyboardInterrupt):
        for index in range(NUM_GUESSES):
            refresh_page(headline=f" Guess {index + 1}")
            show_guesses(guesses, word)

            guesses[index] = guess_word(previous_guesses=guesses[:index])
            if guesses[index] == word:
                break

    # Post-process
    game_over(guesses, word, guessed_correctly=guesses[index] == word)

def guess_word(previous_guesses):
    guess = console.input("\nGuess Word: ").upper()

    if guess in previous_guesses:
        console.print(f"You've already guessed {guess}.", style="warning")
        return guess_word(previous_guesses)
    
    if len(guess) != 5:
        console.print("Your guess must be 5 letters.", style="warning")
        return guess_word(previous_guesses)
    
    if any((invalid := letter) not in ascii_letters for letter in guess):
        console.print(
            f"Invalid letter: '{invalid}'. Please use English letters.", style="warning",
        )
        return guess_word(previous_guesses)

    return guess

def get_random_word(word_list):    
    """Selects a random five-letter word from the wordlist.txt file.
    
    ## Example:
    
    >>> get_random_word(["broke", "stop", "kn1ght'5"])
    'BROKE'
    """

    if words := [
        word.upper()
        for word in word_list
        if len(word) == NUM_LETTERS and all(letter in ascii_letters for letter in word)
    ]:
        return random.choice(words)
    else:
        console.print("No words of length 5 are present in the word list", style="warning")
        raise SystemExit()

def show_guesses(guesses, word):
    letter_status = {letter: letter for letter in ascii_uppercase}
    for guess in guesses:
        styled_guess = []
        for letter, correct in zip(guess,word):
            if letter == correct:
                style = "bold white on green"
            elif letter in word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]")
            if letter != "_":
                letter_status[letter] = f"[{style}]{letter}[/]"
        
        console.print("".join(styled_guess), justify="center")
    console.print("\n" + "".join(letter_status.values()), justify="center")

## Deprecated version of the show_guess function
# def show_guess(guess, word):
#     """Display user's guess on the terminal and classify letters (i.e. correct, misplaced, wrong)
    
#     ## Example:
    
#     >>> show_guess("ANGEL", "CRANE")
#     Correct Letters: 
#     Misplaced Letters: A, E, N
#     Wrong Letters: G, L
#     """

#     correctLetters = {
#         letter for letter, correct in zip(guess, word) if letter == correct
#     }
#     misplacedLetters = set(guess) & set(word) - correctLetters
#     wrongLetters = set(guess) - set(word)

#     print("Correct Letters:", ", ".join(sorted(correctLetters)))
#     print("Misplaced Letters:", ", ".join(sorted(misplacedLetters)))
#     print("Wrong Letters:", ", ".join(sorted(wrongLetters)))
     
def game_over(guesses, word, guessed_correctly):
    refresh_page(headline="Game Over")
    show_guesses(guesses, word)

    if guessed_correctly:
        console.print(f"\n[bold white on green]Correct, the word is {word}[/]")
    else:
        console.print(f"\n[bold white on red]Sorry, the word was {word}[/]")

## Deprecated version of the game_over function
# def game_over(word):
#     """Display the 'Game Over' message and the random word.
    
#     ## Example:
    
#     >>> game_over("ANGEL")
#     <BLANKLINE>
#     --- Game Over ---
#     The word was ANGEL
#     """

#     print(f"\n--- Game Over ---")
#     print(f"The word was {word}")

def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:performing_arts: {headline} :performing_arts:[/]\n")

if __name__ == "__main__":
    main()