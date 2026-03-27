import unittest

from source import word_loader


class TestWordLoader(unittest.TestCase):
    def test_load_words_success_and_has_words_true(self):
        loader = word_loader.WordLoader("./tests/test_wordrepo.txt")
        self.assertTrue(loader.has_words())

    def test_load_words_file_not_found(self):
        with self.assertRaises(word_loader.WordLoaderError):
            word_loader.WordLoader("./tests/non_existent_file.txt")

    def test_load_words_empty_file(self):
        with self.assertRaises(word_loader.WordLoaderError):
            word_loader.WordLoader("./tests/empty_wordrepo.txt")

    def test_has_words_false(self):
        loader = word_loader.WordLoader("./tests/test_wordrepo.txt")
        for _ in range(len(loader.words)):
            loader.pick_random_word()
        self.assertFalse(loader.has_words())

    def test_pick_random_word(self):
        loader = word_loader.WordLoader("./tests/test_wordrepo.txt")
        picked_word = loader.pick_random_word()
        self.assertIn(
            picked_word, ["testwordone", "testwordtwo", "testwordthree"]
        )
        self.assertNotIn(picked_word, loader.words)

    def test_words_filter_correct(self):
        loader = word_loader.WordLoader("./tests/test_wordrepo.txt")
        for word in loader.words:
            self.assertTrue(word.isalpha() and word.isascii())
