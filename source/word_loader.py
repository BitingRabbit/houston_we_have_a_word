"""Module for loading words from a file and picking a random word"""

import random


class WordLoaderError(Exception):
    pass


class WordLoader:
    def __init__(self, filename: str) -> None:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.words: list[str] = [
                    line.strip().lower()
                    for line in file
                    if line.strip().isalpha() and line.strip().isascii()
                ]
        except FileNotFoundError:
            raise WordLoaderError(f"File not found: {filename}") from None

        if not self.words:
            raise WordLoaderError(f"No words found in: {filename}")

    def pick_random_word(self) -> str:
        """Picks and returns a random word from the loaded words."""
        picked_word: str = random.choice(self.words)
        self.words.remove(picked_word)
        return picked_word

    def has_words(self) -> bool:
        """Checks if there are still words available to pick."""
        return len(self.words) > 0
