"""Entry point for the game"""


import os
import sys

from .display import Color, Display
from .game_logic import GameLogic
from .word_loader import WordLoader, WordLoaderError


def main() -> None:
    """Main function to run the Hangman game"""
    filename: str = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "wordrepo.txt"
    )
    try:
        word_loader = WordLoader(filename)
    except WordLoaderError as e:
        print(f"Error loading words: {e}. Exiting the game.")
        sys.exit(1)

    game_logic = GameLogic(word_loader)

    Display.show_welcome_message()

    while word_loader.has_words():
        game_logic.start_new_game()

        play_one_round(game_logic)

        Display.show_current_state(
            display_word=game_logic.get_display_word(),
            wrong_guesses=game_logic.wrong_guesses,
            attempts_left=game_logic.attempts_left,
            max_attempts=game_logic.MAX_ATTEMPTS,
        )

        Display.show_game_over_message(
            won=game_logic.is_won(),
            correct_word=game_logic.current_word
        )

        if not Display.quit_continue_menu():
            sys.exit(0)
    
    print(f"{Color.BLUE}Alle Begriffe entschlüsselt. Apollo 13 ist sicher gelandet. Bis zur nächsten Mission!{Color.END}")
    

def play_one_round(game_logic: GameLogic) -> None:
    """Plays a single round of the game."""
    while game_logic.is_running():
        Display.show_current_state(
            display_word=game_logic.get_display_word(),
            wrong_guesses=game_logic.wrong_guesses,
            attempts_left=game_logic.attempts_left,
            max_attempts=game_logic.MAX_ATTEMPTS,
        )

        guess = Display.ask_guess()

        if len(guess) == 1:
            game_logic.guess_letter(guess)
        else:
            game_logic.guess_word(guess)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Color.BLUE + "\nMission abgebrochen. Bis zum nächsten Mal..." + Color.END)
        sys.exit(0)
