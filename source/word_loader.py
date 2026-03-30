"""Module for loading words from a file and picking a random word"""

import random


class WordLoaderError(Exception):
    """Custom exception for errors related to WordLoader"""


class WordLoader:
    """
    Class to load words from a file and pick a random word for the game
    
    Attributes:
        words (list[str]): List of valid words loaded from the file
        loaded_words (int): number of valid words loaded from the file
    """

    def __init__(self, filename: str) -> None:
        """
        Initializes the WordLoader with a file containing words

        Args:
            filename (str): Path to the file containing words, one word per line

        Raises:
            WordLoaderError: if the file is not found
            WordLoaderError: if no valid words are found in the file
        """
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.words: list[str] = []
                for line in file:
                    word: str = line.strip().lower()
                    if (
                        word.isalpha()
                        and word.isascii()
                        and len(word) < 30
                        and len(word) > 4
                        and word not in self.words
                    ):
                        self.words.append(word)

        except FileNotFoundError:
            raise WordLoaderError(f"File not found: {filename}") from None

        if not self.words:
            raise WordLoaderError(f"No valid words found in: {filename}")

        self.loaded_words: int = len(self.words)

    def pick_random_word(self) -> str:
        """
        Picks and returns a random word from the loaded words

        Returns:
            str: randomly picked word from the loaded words
        """
        picked_word: str = random.choice(self.words)
        self.words.remove(picked_word)
        return picked_word

    def has_words(self) -> bool:
        """
        Checks if there are still words available to pick

        Returns:
            bool: True if word list contains words, False if not
        """
        return len(self.words) > 0
