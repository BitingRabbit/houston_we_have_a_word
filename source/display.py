"""Module to display the current state of the game and handle all the UI interactions"""


class Display:
    @staticmethod
    def show_welcome_message() -> None:
        print(
            f"{Color.YELLOW}═══════════════════════════════════════════{Color.END}"
        )
        print(
            f"{Color.YELLOW}   APOLLO 13 – HOUSTON, WIR HABEN EIN PROBLEM   {Color.END}"
        )
        print(
            f"{Color.YELLOW}═══════════════════════════════════════════{Color.END}"
        )
        print(f"{Color.CYAN}14. April 1970.{Color.END}")
        print("An Bord der Apollo 13 explodiert ein plötzlich Sauerstofftank.")
        print(
            "Du sitzt in Houston und hast nur eine Chance die Crew zu retten!!"
        )
        print(
            f"{Color.PURPLE}Entschlüssele unbedingt die Begriffe – \
            Buchstabe für Buchstabe oder per direkt Lösung.\n \
            Aber nehme dich in Acht, du hast begrenzte Versuche!{Color.END}"
        )
        print(
            f"{Color.YELLOW}═══════════════════════════════════════════{Color.END}"
        )

    @staticmethod
    def ask_guess() -> str:
        """Prompts the user to enter a guess and returns it."""
        while True:
            guess = (
                input(
                    Color.PURPLE
                    + "Houston, deine Eingabe: "
                    + Color.END
                )
                .strip()
                .lower()
            )
            if guess.isalpha() and guess.isascii():
                return guess
            else:
                print(
                    f"{Color.RED}Übertragung nicht angekommen, ungültig!!. Bitte nur Buchstaben verwenden.{Color.END}"
                )

    @staticmethod
    def show_current_state(
        display_word: str,
        wrong_guesses: set[str],
        attempts_left: int,
        max_attempts: int,
    ) -> None:
        heart = (
            Color.GREEN + "♥ " + Color.END
            if attempts_left > 3
            else Color.RED + "♥ " + Color.END
        )
        lost_heart = "♦ "
        health_bar = heart * attempts_left + lost_heart * (
            max_attempts - attempts_left
        )
        health_visible = attempts_left * 2 + (max_attempts - attempts_left) * 2

        width = (len(display_word) + 10) if len(display_word) > 20 else 30
        health_padding = " " * (width - health_visible - 11)

        display_word = Color.GREEN + display_word + Color.END
        print("╔" + "═" * (width - 1) + "╗")

        # Display health-bar
        print(
            f"║ {Color.CYAN}Sauerstoff:{Color.END} {health_bar}{health_padding} ║"
        )

        # Display the current state of the guessed word
        print(f"║ {Color.CYAN}Begriff:{Color.END} {display_word:<{width}} ║")

        # display guessed letters
        print(
            f"║ {Color.CYAN}Falsche Signale:{Color.END}"
            + " " * (width - 16)
            + "║"
        )
        print(f"║ {', '.join(sorted(wrong_guesses)):<{width - 3}} ║")
        print("╚" + "═" * (width - 1) + "╝")

    @staticmethod
    def show_game_over_message(won: bool, correct_word: str) -> None:
        if won:
            print(f"{Color.GREEN}╔═══════════════════════════════════════════╗{Color.END}")
            print(f"{Color.GREEN}║   SPLASHDOWN – DIE CREW IST GERETTET!!    ║{Color.END}")
            print(f"{Color.GREEN}╚═══════════════════════════════════════════╝{Color.END}")
            print(f"{Color.GREEN}Houston atmet endlich auf. Mission erfolgreich abgeschlossen!{Color.END}")
        else:
            print(f"{Color.RED}╔═══════════════════════════════════════════╗{Color.END}")
            print(f"{Color.RED}║       SIGNAL VERLOREN – CREW VERMISST!!   ║{Color.END}")
            print(f"{Color.RED}╚═══════════════════════════════════════════╝{Color.END}")
            print(f"{Color.RED}Verbindung abgebrochen... Der gesuchte Begriff war: {correct_word.upper()}{Color.END}")

    @staticmethod
    def quit_continue_menu() -> bool:
        """Asks the user if they want to play again or quit."""
        while True:
            choice = (
                input(
                    Color.PURPLE
                    + "Nächste Mission starten? (y/n): "
                    + Color.END
                )
                .strip()
                .lower()
            )
            if choice == "y":
                return True
            elif choice == "n":
                print(f"{Color.BLUE}Houston wird heruntergefahren. Du bist ein Held, du hast ihr Leben gerettet!{Color.END}")
                return False
            else:
                print(
                    f"{Color.RED}Ungültige Eingabe. Bitte 'y' oder 'n' eingeben...{Color.END}"
                )


class Color:
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
