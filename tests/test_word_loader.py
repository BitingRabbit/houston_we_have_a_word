import unittest

from source import word_loader


class TestWordLoader(unittest.TestCase):
    """Tests for the WordLoader class methods"""

    def test_load_words_success_and_has_words_true(self):
        """
        Test loading words from a valid file and check if has_words returns true
        """
        loader = word_loader.WordLoader("./tests/test_wordrepo.txt")
        self.assertTrue(loader.has_words())

    def test_load_words_file_not_found(self):
        with self.assertRaises(word_loader.WordLoaderError):
            word_loader.WordLoader("./tests/non_existent_file.txt")

    def test_load_words_empty_file(self):
        with self.assertRaises(word_loader.WordLoaderError):
            word_loader.WordLoader("./tests/empty_wordrepo.txt")

    def test_load_words_duplicate_words(self):
        """
        Loads words from a file with duplicate words and checks if only unique words are loaded
        """
        loader = word_loader.WordLoader(
            "./tests/test_wordrepo_with_duplicates.txt"
        )
        self.assertEqual(loader.loaded_words, 2)  # only 2 unique words

    def test_has_words_false(self):
        """
        Test if has_words returns false when all words have been picked
        """
        loader = word_loader.WordLoader("./tests/test_wordrepo.txt")
        for _ in range(len(loader.words)):
            loader.pick_random_word()
        self.assertFalse(loader.has_words())

    def test_pick_random_word(self):
        """
        Test if pick_random_word returns a word from the loaded words and removes it from the list,
        ensuring that the same word cannot be picked again within the same game session
        """
        loader = word_loader.WordLoader("./tests/test_wordrepo.txt")
        picked_word = loader.pick_random_word()
        self.assertIn(
            picked_word, ["testwordone", "testwordtwo", "testwordthree"]
        )
        self.assertNotIn(picked_word, loader.words)

    def test_words_filter_correct(self):
        """
        Test if all loaded words are alphabetic and ASCII only and not too long/short
        Words are valid regardless of case
        """
        loader = word_loader.WordLoader("./tests/test_wordrepo.txt")
        for word in loader.words:
            self.assertTrue(
                word.isalpha() and word.isascii() and 4 < len(word) < 30
            )
        self.assertEqual(loader.loaded_words, 3)
