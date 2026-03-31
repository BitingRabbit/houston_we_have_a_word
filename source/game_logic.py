"""Module containing the core game logic"""

from .display import Color
from .word_loader import WordLoader


class GameLogic:
    """
    Class to handle the core game logic for the game, such as processing guesses,
    tracking game state, and determining wether the player has won or lost

    Class Attributes:
        MAX_ATTEMPTS (int): The maximum number of incorrect guesses allowed until failure

    Attributes:
        word_loader (WordLoader): instance of the WordLoader class to manage word selection
        current_word (str): the word currently being guessed
        guessed_letters (set[str]): a set of letters that have already been guessed
        wrong_guesses (set[str]): a set of letters or words that have been guessed incorrectly
        attempts_left (int): the number of incorrect guesses remaining before the game is lost
        correct_rounds (list[bool]): list tracking the results of each round for the final message
    """

    MAX_ATTEMPTS: int = (
        7  # equal to 6 wrong guesses, 7th wrong guess is the failure
    )

    def __init__(self, word_loader: WordLoader):
        """
        Initializes the GameLogic instance with a WordLoader and sets up the initial game state

        Args:
            word_loader (WordLoader): instance of the WordLoader class to manage word selection
        """
        self.word_loader: WordLoader = word_loader
        self.current_word: str = ""
        self.guessed_letters: set[str] = set()
        self.wrong_guesses: set[str] = set()
        self.attempts_left: int = self.MAX_ATTEMPTS
        self.correct_rounds: list[bool] = []

    def start_new_game(self) -> None:
        """Starts a new game by picking a random word and resetting the game state"""
        self.current_word = self.word_loader.pick_random_word()
        self.guessed_letters.clear()
        self.wrong_guesses.clear()
        self.attempts_left = self.MAX_ATTEMPTS

    # Methods to process guesses
    def guess_letter(self, letter: str) -> None:
        """
        Processes a guessed letter and updates the game state

        Args:
            letter (str): User guess
        """
        if letter not in self.guessed_letters:
            self.guessed_letters.add(letter)

        if (
            letter not in self.current_word
            and letter not in self.wrong_guesses
        ):
            self.wrong_guesses.add(letter)
            self.attempts_left -= 1

            print(
                f"\n{Color.RED}WARNUNG: CO2-Level steigt im LM!!!{Color.END}"
            )
            print(
                f"{Color.YELLOW}Mission Control arbeitet an einer Lösung...{Color.END}"
            )

    def guess_word(self, word: str) -> None:
        """
        Processes a guessed word and updates the game state

        Args:
            word (str): User guess
        """
        if word == self.current_word:
            self.guessed_letters.update(word)
        else:
            self.attempts_left = 0
            self.wrong_guesses.add(word)

    def get_display_word(self) -> str:
        """
        Returns the current state of the guessed word with underscores for unguessed letters

        Returns:
            str: current state of the guessed word
        """
        return " ".join(
            letter if letter in self.guessed_letters else "_"
            for letter in self.current_word
        ).capitalize()

    # Helper methods to check game state
    def is_won(self) -> bool:
        """
        Checks if all letters in the current word have been guessed correctly

        Returns:
            bool: true or false wether won or lost
        """
        return all(
            letter in self.guessed_letters for letter in self.current_word
        )

    def is_running(self) -> bool:
        """
        Checks if the game is still running

        Returns:
            bool: true or false wether the game is won or any attempts left
        """
        return not self.is_won() and self.attempts_left > 0
