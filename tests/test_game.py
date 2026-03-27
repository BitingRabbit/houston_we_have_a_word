import unittest
from unittest.mock import MagicMock, patch

from source import game, word_loader


class TestGame(unittest.TestCase):
    def test_single_letter_calls_guess_letter(self):
        game_logic = MagicMock()
        game_logic.is_running.side_effect = [True, False]  # eine Iteration
        game_logic.get_display_word.return_value = "_ _ _ _"
        game_logic.attempts_left = 5
        game_logic.MAX_ATTEMPTS = 6
        game_logic.wrong_guesses = set()

        with patch("source.game.Display.ask_guess") as mock_ask_guess:
            mock_ask_guess.return_value = "t"
            game.play_one_round(game_logic)

        game_logic.guess_letter.assert_called_once_with("t")
        game_logic.guess_word.assert_not_called()

    def test_full_word_calls_guess_word(self):
        game_logic = MagicMock()
        game_logic.is_running.side_effect = [True, False]
        game_logic.get_display_word.return_value = "_ _ _ _"
        game_logic.attempts_left = 5
        game_logic.MAX_ATTEMPTS = 6
        game_logic.wrong_guesses = set()

        with patch("source.game.Display.ask_guess") as mock_ask_guess:
            mock_ask_guess.return_value = "test_word_one"
            game.play_one_round(game_logic)

        game_logic.guess_word.assert_called_once_with("test_word_one")
        game_logic.guess_letter.assert_not_called()

    def test_main_word_loader_error_exits(self):
        """WordLoadError throwing error, leading to sys.exit(1)"""
        with patch(
            "source.game.WordLoader",
            side_effect=word_loader.WordLoaderError("fail"),
        ):
            with self.assertRaises(SystemExit) as wl_error:
                game.main()
        self.assertEqual(wl_error.exception.code, 1)

    def test_main_player_quits_after_one_round(self):
        """Player choosing to quit after one round, leading to sys.exit(0)"""
        mock_word_loader = MagicMock()
        mock_word_loader.has_words.side_effect = [True, False]

        mock_game_logic = MagicMock()
        mock_game_logic.attempts_left = 5
        mock_game_logic.MAX_ATTEMPTS = 6
        mock_game_logic.wrong_guesses = set()

        with (
            patch("source.game.WordLoader", return_value=mock_word_loader),
            patch("source.game.GameLogic", return_value=mock_game_logic),
            patch("source.game.Display") as mock_display,
            patch("source.game.play_one_round"),
        ):
            mock_display.quit_continue_menu.return_value = (
                False  # player chooses to quit
            )

            with self.assertRaises(SystemExit) as quit_error:
                game.main()

        self.assertEqual(quit_error.exception.code, 0)

    def test_main_runs_full_loop_then_no_words(self):
        """After all words used, loop should end normally"""
        mock_word_loader = MagicMock()
        mock_word_loader.has_words.side_effect = [True, False]

        mock_game_logic = MagicMock()
        mock_game_logic.attempts_left = 5
        mock_game_logic.MAX_ATTEMPTS = 6
        mock_game_logic.wrong_guesses = set()

        with (
            patch("source.game.WordLoader", return_value=mock_word_loader),
            patch("source.game.GameLogic", return_value=mock_game_logic),
            patch("source.game.Display") as mock_display,
            patch("source.game.play_one_round"),
        ):
            mock_display.quit_continue_menu.return_value = (
                True  # player chooses to continue
            )

            game.main()  # no sys.exit() expected

        mock_game_logic.start_new_game.assert_called_once()

    def test_main_no_words_from_start(self):
        """If no words from the start, while loop should never be entered"""
        mock_word_loader = MagicMock()
        mock_word_loader.has_words.return_value = False  # directly False

        with (
            patch("source.game.WordLoader", return_value=mock_word_loader),
            patch("source.game.GameLogic"),
            patch("source.game.Display") as mock_display,
        ):
            game.main()  # runs through without error

        mock_display.quit_continue_menu.assert_not_called()
