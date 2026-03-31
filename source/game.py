"""
Entry point for the game, orchestrating the flow and interaction between all classes
"""

import sys

from .display import Color, Display
from .game_logic import GameLogic
from .word_loader import WordLoader, WordLoaderError


def main() -> None:
    """
    Main function orchestrating the game flow and all classes:
    - loading words
    - starting new games
    - handling user input
    - displaying game state and messages
    """
    filename: str = "./source/wordrepo.txt"
    try:
        word_loader = WordLoader(filename)
    except WordLoaderError as e:
        print(
            f"{Color.RED}Error loading words: {e}. Exiting the game.{Color.END}"
        )
        sys.exit(1)

    game_logic = GameLogic(word_loader)

    Display.show_game_start_message()

    while word_loader.has_words():
        game_logic.start_new_game()

        Display.show_systemcheck_counter(
            word_loader.words, word_loader.loaded_words
        )

        play_one_round(game_logic)

        Display.show_current_state(
            display_word=game_logic.get_display_word(),
            wrong_guesses=game_logic.wrong_guesses,
            attempts_left=game_logic.attempts_left,
            max_attempts=game_logic.MAX_ATTEMPTS,
        )

        Display.show_game_over_message(
            won=game_logic.is_won(), correct_word=game_logic.current_word
        )

        # track results of rounds to determine final message at the end
        game_logic.correct_rounds.append(game_logic.is_won())

        if not Display.quit_continue_menu():
            sys.exit(0)

    Display.splash_down_message(result=game_logic.correct_rounds)


def play_one_round(game_logic: GameLogic) -> None:
    """
    Plays a single round of the game:
    - displaying game state
    - getting user guess
    - updating game logic based on the guess
    - checking if the game is won or lost


    Args:
        game_logic (GameLogic): game logic instance managing the current game state
    """
    while game_logic.is_running():
        Display.show_current_state(
            display_word=game_logic.get_display_word(),
            wrong_guesses=game_logic.wrong_guesses,
            attempts_left=game_logic.attempts_left,
            max_attempts=game_logic.MAX_ATTEMPTS,
        )

        guess: str = Display.ask_guess()

        if len(guess) == 1:
            game_logic.guess_letter(guess)
        else:
            game_logic.guess_word(guess)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(
            Color.BLUE
            + "Systemcheck abgebrochen. Die Crew wurde leider nicht gerettet."
            + " Bis zum nächsten Mal..."
            + Color.END
        )
        sys.exit(0)
