import unittest

from source import game_logic


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        # pylint: disable=too-few-public-methods
        # reason: a simple Mock-Class for WordLoader, hence only one method
        class TestWordLoader:
            def pick_random_word(self):
                return "test"

        self.game_logic = game_logic.GameLogic(TestWordLoader())
        self.game_logic.start_new_game()

    def test_guess_letter_correct(self):
        self.game_logic.guess_letter("t")
        self.assertIn("t", self.game_logic.guessed_letters)
        self.assertEqual(
            self.game_logic.attempts_left, game_logic.GameLogic.MAX_ATTEMPTS
        )

    def test_guess_letter_incorrect(self):
        self.game_logic.guess_letter("x")  # wrong guess
        self.assertIn("x", self.game_logic.wrong_guesses)
        self.assertEqual(
            self.game_logic.attempts_left,
            game_logic.GameLogic.MAX_ATTEMPTS - 1,
        )

    def test_guess_duplicate_correct_letter(self):
        self.game_logic.guess_letter("t")
        self.game_logic.guess_letter("t")  # second right guess
        self.assertEqual(
            self.game_logic.attempts_left, game_logic.GameLogic.MAX_ATTEMPTS
        )

    def test_guess_duplicate_wrong_letter(self):
        self.game_logic.guess_letter("x")
        self.game_logic.guess_letter("x")  # same wrong guess
        self.assertEqual(
            self.game_logic.attempts_left,
            game_logic.GameLogic.MAX_ATTEMPTS - 1,
        )  # only -1, not -2

    def test_guess_word_correct(self):
        self.game_logic.guess_word("test")
        self.assertTrue(self.game_logic.is_won())
        self.assertEqual(
            self.game_logic.attempts_left, game_logic.GameLogic.MAX_ATTEMPTS
        )

    def test_guess_word_incorrect(self):
        self.game_logic.guess_word("wrongWord")
        self.assertFalse(self.game_logic.is_won())
        self.assertEqual(self.game_logic.attempts_left, 0)

    def test_get_display_word(self):
        self.game_logic.guess_letter("t")
        self.assertEqual(self.game_logic.get_display_word(), "T _ _ t")

    def test_get_display_word_no_guesses(self):
        self.assertEqual(self.game_logic.get_display_word(), "_ _ _ _")

    def test_is_won(self):
        self.game_logic.guess_letter("t")
        self.game_logic.guess_letter("e")
        self.game_logic.guess_letter("s")
        self.assertTrue(self.game_logic.is_won())

    def test_is_won_false(self):
        self.game_logic.guess_letter("t")
        self.assertFalse(self.game_logic.is_won())

    def test_is_running(self):
        self.assertTrue(self.game_logic.is_running())
        self.game_logic.guess_word("wrongWord")
        self.assertFalse(self.game_logic.is_running())

    def test_start_new_game(self):
        self.game_logic.guess_letter("t")
        self.game_logic.guess_letter("x")  # wrong guess
        self.game_logic.start_new_game()
        self.assertEqual(self.game_logic.current_word, "test")
        self.assertEqual(
            self.game_logic.attempts_left, game_logic.GameLogic.MAX_ATTEMPTS
        )
        self.assertFalse(self.game_logic.guessed_letters)
        self.assertFalse(self.game_logic.wrong_guesses)

    def tearDown(self):
        del self.game_logic  # brauche ich das ?
