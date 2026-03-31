import unittest

from source import game_logic


class TestGameLogic(unittest.TestCase):
    """Tests for the GameLogic class methods"""

    def setUp(self):
        # pylint: disable=too-few-public-methods
        # reason: a simple Mock-Class for WordLoader, hence only one method
        class TestWordLoader:
            """Mock WordLoader class for testing"""

            def pick_random_word(self):
                return "test"

        self.game_logic = game_logic.GameLogic(TestWordLoader())
        self.game_logic.start_new_game()

    def test_guess_letter_correct(self):
        """
        correct guess should:
        - add letter to guessed_letters
        - not add letter to wrong_guesses
        - not decrease attempts_left
        - game should still be running
        """
        self.game_logic.guess_letter("t")
        self.assertIn("t", self.game_logic.guessed_letters)
        self.assertNotIn("t", self.game_logic.wrong_guesses)
        self.assertEqual(
            self.game_logic.attempts_left, self.game_logic.MAX_ATTEMPTS
        )
        self.assertTrue(self.game_logic.is_running())

    def test_guess_letter_incorrect(self):
        """
        incorrect guess should:
        - add letter to wrong_guesses and general guessed_letters
        - decrease attempts_left by 1
        - game should still be running (since attempts_left > 0)
        """
        self.game_logic.guess_letter("x")  # wrong guess
        self.assertIn("x", self.game_logic.wrong_guesses)
        self.assertIn("x", self.game_logic.guessed_letters)
        self.assertEqual(
            self.game_logic.attempts_left,
            self.game_logic.MAX_ATTEMPTS - 1,
        )
        self.assertTrue(self.game_logic.is_running())

    def test_guess_duplicate_correct_letter(self):
        """
        guessing the same correct letter multiple times should:
        - only add it once to guessed_letters
        - not decrease attempts_left hence its not a mistake to guess it again
        - game should still be running
        """
        self.game_logic.guess_letter("t")
        self.game_logic.guess_letter("t")  # second right guess
        self.assertCountEqual(
            self.game_logic.guessed_letters, {"t"}
        )  # only one 't' in guessed_letters
        self.assertEqual(
            self.game_logic.attempts_left, self.game_logic.MAX_ATTEMPTS
        )

    def test_guess_duplicate_wrong_letter(self):
        """
        guessing the same incorrect letter multiple times should:
        - only add it once to wrong_guesses
        - only decrease attempts_left by 1 (not multiple times for the same wrong guess)
        """
        self.game_logic.guess_letter("x")
        self.game_logic.guess_letter("x")  # same wrong guess
        self.assertEqual(
            self.game_logic.attempts_left,
            self.game_logic.MAX_ATTEMPTS - 1,
        )  # only -1, not -2
        self.assertCountEqual(
            self.game_logic.wrong_guesses, {"x"}
        )  # only one 'x' in wrong_guesses

    def test_guess_word_correct(self):
        """
        correct word guess should:
        - mark the game as won
        - set is_running to false
        - not decrease attempts_left
        - add all letters of the word to guessed_letters
        """
        self.game_logic.guess_word("test")
        self.assertTrue(self.game_logic.is_won())
        self.assertFalse(self.game_logic.is_running())
        self.assertEqual(
            self.game_logic.attempts_left, self.game_logic.MAX_ATTEMPTS
        )
        self.assertEqual(self.game_logic.guessed_letters, set("test"))

    def test_guess_word_incorrect(self):
        """
        incorrect word guess should:
        - add the whole word to wrong_guesses
        - mark the game as lost
        - set is_running to false
        - decrease attempts_left to 0
        """
        self.game_logic.guess_word("wrongWord")
        self.assertEqual(self.game_logic.wrong_guesses, {"wrongWord"})
        self.assertFalse(self.game_logic.is_won())
        self.assertFalse(self.game_logic.is_running())
        self.assertEqual(self.game_logic.attempts_left, 0)

    def test_get_display_word(self):
        self.game_logic.guess_letter("t")
        self.assertEqual(self.game_logic.get_display_word(), "T _ _ t")

    def test_get_display_word_no_guesses(self):
        self.assertEqual(self.game_logic.get_display_word(), "_ _ _ _")

    def test_is_won_letters(self):
        """guessing all letters of the word should mark the game as won and not lost"""
        for letter in "tes":
            self.game_logic.guess_letter(letter)
        self.assertTrue(self.game_logic.is_won())

    def test_is_won_false_and_lost_letters(self):
        """
        one correct letter -> not won, but also not lost yet
        then 6 wrong guesses -> lost, hence not won
        """
        self.game_logic.guess_letter("t")
        self.assertFalse(self.game_logic.is_won())
        self.assertTrue(self.game_logic.is_running())
        for letter in "quvwxyz":
            self.game_logic.guess_letter(letter)
        self.assertFalse(self.game_logic.is_won())
        self.assertFalse(self.game_logic.is_running())

    def test_is_running_wrong_word(self):
        """
        guessing one wrong letter: game still running
        guessing wrong word: game should be lost, hence not running
        """
        self.assertTrue(self.game_logic.is_running())
        self.game_logic.guess_letter("t")
        self.assertTrue(self.game_logic.is_running())
        self.game_logic.guess_word("wrongWord")
        self.assertFalse(self.game_logic.is_running())

    def test_start_new_game(self):
        """
        starting a new game should:
        - reset the current word
        - reset attempts_left to MAX_ATTEMPTS
        - clear guessed_letters and wrong_guesses
        """
        self.game_logic.guess_letter("t")
        self.game_logic.guess_letter("x")  # wrong guess
        self.game_logic.start_new_game()
        self.assertEqual(self.game_logic.current_word, "test")
        self.assertEqual(
            self.game_logic.attempts_left, self.game_logic.MAX_ATTEMPTS
        )
        self.assertFalse(self.game_logic.guessed_letters)
        self.assertFalse(self.game_logic.wrong_guesses)
