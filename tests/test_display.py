import unittest
from unittest.mock import patch

from source import display


class TestDisplay(unittest.TestCase):
    def test_ask_guess(self):
        with patch("builtins.input", return_value=" T "): # whitespace and uppercase
            self.assertEqual(display.Display.ask_guess(), "t") # stripped and lowered

        with patch("builtins.input", side_effect=["1", "!", "t"]):
            self.assertEqual(display.Display.ask_guess(), "t")

    def test_quit_continue_menu(self):
        with patch("builtins.input", return_value="y"):
            self.assertTrue(display.Display.quit_continue_menu())

        with patch("builtins.input", return_value="n"):
            self.assertFalse(display.Display.quit_continue_menu())

        with patch("builtins.input", side_effect=["wrongInput", "y"]):
            self.assertTrue(display.Display.quit_continue_menu())

    def test_show_current_state(self):
        with patch("builtins.print") as mock_print:
            display.Display.show_current_state(
                display_word="T _ _ t",
                wrong_guesses={"x", "y"},
                attempts_left=3,
                max_attempts=6,
            )
            self.assertTrue(mock_print.called)
