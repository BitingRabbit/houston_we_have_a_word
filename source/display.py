"""Module to display the current state of the game and handle all the UI interactions"""


class Display:
    """Class to handle all display and user interaction logic"""

    @staticmethod
    def show_game_start_message() -> None:
        """Text at the beginning of the game, introducing the topic"""
        print(
            f"{Color.YELLOW}════════════════════════════════════════════════{Color.END}"
        )
        print(
            f"{Color.YELLOW}   APOLLO 13 - HOUSTON, WIR HABEN EIN PROBLEM   {Color.END}"
        )
        print(
            f"{Color.YELLOW}════════════════════════════════════════════════{Color.END}"
        )
        print(f"{Color.CYAN}13. April 1970...{Color.END}")
        print(
            f"{Color.BOLD}An Bord von Apollo 13 explodiert plötzlich ein Sauerstofftank."
        )
        print(
            "Die Mission zum Mond wird abgebrochen. \nDie Crew kämpft ums Überleben."
        )
        print(
            f"Du sitzt in Houston und hast nur eine Chance die Crew zu retten!!{Color.END}"
        )
        print(
            Color.PURPLE
            + "Du musst es schaffen, alle Systemchecks erfolgreich durchzuführen"
            " und dabei pro Systemcheck die Diagnosecodes \nrichtig zu entschlüsseln:"
            " Buchstabe für Buchstabe oder per direkter Lösung des Diagnosecodes.\n"
            f"Aber nehme dich in acht, denn der CO2-Level steigt im LM mit jedem Fehler!!!"
            f"{Color.END}{Color.CYAN}"
            "\nMit Ctrl + C kannst du jederzeit die ganze Mission sicher abbrechen!"
            f"{Color.END}{Color.YELLOW}"
            "\nViel Erfolg, die Crew zählt auf dich!!" + Color.END
        )
        print(
            f"{Color.YELLOW}═══════════════════════════════════════════{Color.END}"
        )

    @staticmethod
    def show_systemcheck_counter(words: list[str], num_check: int) -> None:
        """
        Displays the current round count based on the remaining words in the word loader

        Args:
            words (list[str]): the list of remaining words in the word loader
            num_check (int): the total number of system checks (rounds)
        """
        current_check: int = num_check - len(words)
        print(
            f"\n{Color.DARKCYAN}Systemcheck {current_check} von {num_check}{Color.END}"
        )

    @staticmethod
    def ask_guess() -> str:
        """
        Prompts the user to enter a guess and returns it normalized

        Returns:
            str: guess of the user
        """
        while True:
            guess: str = (
                input(Color.PURPLE + "Houston, deine Eingabe: " + Color.END)
                .strip()
                .lower()
            )
            if guess.isalpha() and guess.isascii():
                return guess

            print(
                f"{Color.RED}Übertragung nicht angekommen, ungültig!!"
                f" Bitte nur Buchstaben verwenden.{Color.END}"
            )

    @staticmethod
    def show_current_state(
        display_word: str,
        wrong_guesses: set[str],
        attempts_left: int,
        max_attempts: int,
    ) -> None:
        """
        Displays the current state of the game, including the guessed word,
        wrong guesses, and remaining attempts.

        Args:
            display_word (str): the current state of the word being guessed
            wrong_guesses (set[str]): a set of incorrect guesses made by the player
            attempts_left (int): the number of attempts remaining
            max_attempts (int): the maximum number of attempts allowed
        """
        heart: str = (
            Color.GREEN + "♥ " + Color.END
            if attempts_left > 3
            else Color.RED + "♥ " + Color.END
        )
        lost_heart: str = "♦ "
        # healthbar to be printed
        health_bar: str = heart * attempts_left + lost_heart * (
            max_attempts - attempts_left
        )
        health_visible: int = (
            attempts_left * 2 + (max_attempts - attempts_left) * 2
        )

        # padding values for the box
        width: int = (len(display_word) + 25) if len(display_word) > 20 else 40
        health_padding: str = " " * (width - health_visible - 15)

        display_word = Color.GREEN + display_word + Color.END

        print("\n╔" + "═" * (width - 1) + "╗")

        # display health bar
        print(
            f"║ {Color.CYAN}Sauerstoff:{Color.END} {health_bar}{health_padding} ║"
        )

        # display the current state of the guessed word
        print(
            f"║ {Color.CYAN}Diagnosecode:{Color.END} {display_word:<{width - 8}} ║"
        )

        # display wrongly guessed letters
        print(
            f"║ {Color.CYAN}Fehlgeschlagene Diagnosen:{Color.END}"
            + " " * (width - len("Fehlgeschlagene Diagnosen:") - 2)
            + "║"
        )
        print(
            f"║ {Color.RED}{', '.join(sorted(wrong_guesses)):<{width - 3}}{Color.END} ║"
        )
        print("╚" + "═" * (width - 1) + "╝")

    @staticmethod
    def show_game_over_message(won: bool, correct_word: str) -> None:
        """
        Displays a win/loss message after the game has ended based wether
        the player won or lost.

        Args:
            won (bool): indicates if the player won the game
            correct_word (str): the correct word that had to be guessed
        """
        if won:
            print(
                f"\n{Color.GREEN}╔════════════════════════════════════╗{Color.END}"
            )
            print(
                f"{Color.GREEN}║      DIAGNOSECODE: VALID!!         ║{Color.END}"
            )
            print(
                f"{Color.GREEN}╚════════════════════════════════════╝{Color.END}"
            )
            print(
                Color.GREEN
                + "Wir kommen der Rettung der Crew einen Schritt näher!!"
                + Color.END
            )
        else:
            print(
                f"\n{Color.RED}╔═══════════════════════════════════════════╗{Color.END}"
            )
            print(
                f"{Color.RED}║       SYSTEMCHECK FEHLGESCHLAGEN          ║{Color.END}"
            )
            print(
                f"{Color.RED}╚═══════════════════════════════════════════╝{Color.END}"
            )
            print(
                Color.RED
                + f"Der gesuchte Diagnosecode war: {correct_word.upper()}"
                + Color.END
            )

    @staticmethod
    def splash_down_message() -> None:
        """Displays the splash down message at the end of the game"""
        print(
            f"\n{Color.GREEN}╔═══════════════════════════════════════════╗{Color.END}"
        )
        print(
            f"{Color.GREEN}║   SPLASHDOWN: DIE CREW IST GERETTET!!     ║{Color.END}"
        )
        print(
            f"{Color.GREEN}╚═══════════════════════════════════════════╝{Color.END}"
        )
        print(
            Color.GREEN
            + "Houston atmet endlich auf. Mission erfolgreich abgeschlossen!"
            + Color.END
        )

    @staticmethod
    def quit_continue_menu() -> bool:
        """
        Asks the user if they want to play again or quit.

        Returns:
            bool: True if the user wants to play again, False if not
        """
        while True:
            choice: str = (
                input(
                    Color.PURPLE
                    + "\nNächste Mission starten? (y/n): "
                    + Color.END
                )
                .strip()
                .lower()
            )

            if choice == "y":
                return True

            if choice == "n":
                print(
                    Color.BLUE
                    + "Houston wird heruntergefahren."
                    + " Die Crew wurde leider nicht gerettet."
                    + Color.END
                )
                return False

            print(
                f"{Color.RED}Ungültige Eingabe. Bitte 'y' oder 'n' eingeben...{Color.END}"
            )


# pylint: disable=too-few-public-methods
# reason: a simple class to hold color codes, no need for more methods
class Color:
    """Class holding ANSI color codes for a colored terminal output"""

    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[31m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"
