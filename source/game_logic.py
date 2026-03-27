"""Module containing the core game logic"""


from .word_loader import WordLoader


class GameLogic:
    MAX_ATTEMPTS: int = 7

    def __init__(self, word_loader: WordLoader):
        self.word_loader: WordLoader = word_loader
        self.current_word: str = ""
        self.guessed_letters: set[str] = set()
        self.wrong_guesses: set[str] = set()  # bewusste Entscheidung -> Doku
        self.attempts_left: int = self.MAX_ATTEMPTS  # Global Variable

    def start_new_game(self) -> None:
        """Starts a new game by picking a random word and resetting the game state."""
        self.current_word = self.word_loader.pick_random_word()
        self.guessed_letters.clear()
        self.wrong_guesses.clear()
        self.attempts_left = self.MAX_ATTEMPTS

    ## Methods to process guesses
    def guess_letter(self, letter: str) -> None:
        """Processes a guessed letter and updates the game state."""
        if letter not in self.guessed_letters:
            self.guessed_letters.add(letter)

        if (
            letter not in self.current_word
            and letter not in self.wrong_guesses
        ):
            self.wrong_guesses.add(letter)
            self.attempts_left -= 1

    def guess_word(self, word: str) -> None:
        """Processes a guessed word and updates the game state."""
        if word == self.current_word:
            self.guessed_letters.update(self.current_word)
        else:
            self.attempts_left = 0
            self.wrong_guesses.add(word)

    def get_display_word(self) -> str:
        """Returns the current state of the guessed word with underscores for unguessed letters."""
        return " ".join(
            letter if letter in self.guessed_letters else "_"
            for letter in self.current_word
        ).capitalize()

    ## Helper methods to check game state
    def is_won(self) -> bool:
        """Checks if the game has been won."""
        return all(
            letter in self.guessed_letters for letter in self.current_word
        )

    def is_running(self) -> bool:
        """Checks if the game is still running."""
        return not self.is_won() and self.attempts_left > 0
