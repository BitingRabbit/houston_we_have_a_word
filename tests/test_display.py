import unittest
from unittest.mock import patch

from source import display


class TestDisplay(unittest.TestCase):
    """Tests for the Display class methods"""

    def test_ask_guess(self):
        """
        guess with capital letter and whitespace should:
        - be stripped of whitespace and converted to lowercase
        not a valid guess should:
        - ask again until a valid guess is given
        """
        with patch(
            "builtins.input", return_value=" T "
        ):  # whitespace and uppercase
            self.assertEqual(
                display.Display.ask_guess(), "t"
            )  # stripped and lowered

        with patch("builtins.input", side_effect=["1", "!", "t"]):
            self.assertEqual(display.Display.ask_guess(), "t")

    def test_quit_continue_menu(self):
        """
        Test the quit_continue_menu method with different inputs:
        - 'y' should return True
        - 'n' should return False
        - invalid input should ask again until a valid input is given
        """

        with patch("builtins.input", return_value="y"):
            self.assertTrue(display.Display.quit_continue_menu())

        with patch("builtins.input", return_value="n"):
            self.assertFalse(display.Display.quit_continue_menu())

        with patch("builtins.input", side_effect=["wrongInput", "y"]):
            self.assertTrue(display.Display.quit_continue_menu())

    def test_show_current_state_displays_word(self):
        """
        tests if display_word is correctly shown as well as that
        the wrong guesses are present
        """
        with patch("builtins.print") as mock_print:
            display.Display.show_current_state(
                display_word="T _ _ T",
                wrong_guesses={"x", "y"},
                attempts_left=3,
                max_attempts=6,
            )
            # alle print-Ausgaben als ein String zusammenfassen
            output = " ".join(str(call) for call in mock_print.call_args_list)

            self.assertIn("T _ _ T", output)
            self.assertIn("x", output)
            self.assertIn("y", output)

    def test_show_systemcheck_counter(self):
        """2 words left out of 5 should show Systemcheck 3 von 5"""
        with patch("builtins.print") as mock_print:
            display.Display.show_systemcheck_counter(
                words=["word1", "word2"],  # 2 words left
                num_check=5,
            )
            args = mock_print.call_args[0][0]
            self.assertIn("3", args)
            self.assertIn("5", args)

    def test_show_game_over_message_won(self):
        """is_won True should show success message"""
        with patch("builtins.print") as mock_print:
            display.Display.show_game_over_message(
                won=True, correct_word="test"
            )
            output = " ".join(str(call) for call in mock_print.call_args_list)
            self.assertIn("DIAGNOSECODE: VALID!!", output)

    def test_show_game_over_message_lost(self):
        """is_won False should show failure message with correct word"""
        with patch("builtins.print") as mock_print:
            display.Display.show_game_over_message(
                won=False, correct_word="test"
            )
            output = " ".join(str(call) for call in mock_print.call_args_list)
            self.assertIn("SYSTEMCHECK FEHLGESCHLAGEN", output)
            self.assertIn("TEST", output)

    def test_splash_down_message(self):
        """
        all True: should show success message
        not all True: should show failure message with correct count
        """
        with patch("builtins.print") as mock_print:
            display.Display.splash_down_message([True, True, True])
            output = " ".join(str(call) for call in mock_print.call_args_list)
            self.assertIn("SPLASHDOWN", output)

            display.Display.splash_down_message(
                [True, False, True]
            )  # two successes, one failure
            output = " ".join(str(call) for call in mock_print.call_args_list)
            self.assertIn(
                "Nur 2 von 3 Systemchecks erfolgreich abgeschlossen", output
            )  # should show correct count in failure message
