![Main Branch Results](https://img.shields.io/badge/Main%20Branch%20Buildresults:-blue)
![pylint-score](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/JuliusWiedemann/d506acc54dead9ca1d070488e813d253/raw/pylint-score.json)
![mypy-warnings](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/JuliusWiedemann/d506acc54dead9ca1d070488e813d253/raw/mypy_warnings.json)
![coverage](https://img.shields.io/badge/coverage-86%25-brightgreen
)
[![license](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

# Houston We Have A Word

## Description
"Houston We Have A Word" is a command-line based word guessing game inspired by the classic Hangman.
Set in the dramatic events of the Apollo 13 mission in 1970, the player takes the seat at Mission Control in Houston. An oxygen tank has exploded on board and the player must bring the crew home safely by deciphering the hidden words related to space and aviation.

### Project Structure

- organized into two main directories: `source` for the game implementation and `tests` for unit tests

```
project/
├── source/
│   ├── __init__.py
│   ├── game.py
│   ├── display.py
│   ├── game_logic.py
│   ├── word_loader.py
│   └── wordrepo.txt
├── tests/
│   ├── .pylintrc
│   ├── __init__.py
│   ├── test_game.py
│   ├── test_display.py
│   ├── test_game_logic.py
│   ├── test_word_loader.py
│   ├── test_wordrepo.txt
│   ├── test_wordrepo_with_duplicates.txt
│   └── empty_wordrepo.txt
├── images/
├── htmlcov/
├── documentation/
├── mypy.ini
├── README.md
├── requirements.txt
└── LICENSE
```

## Requirements
- Python >= 3.10

## Installation

```bash
# Cloning the repository and navigating into the project directory
git clone https://github.com/BitingRabbit/houston_we_have_a_word.git
cd project

# Creating a virtual environment
python -m venv .venv 

# Activating the virtual environment (Linux/MacOS)
source .venv/bin/activate

# Activating the virtual environment (Windows)
# Script execution is usually disabled on Win11, so:
Set-ExecutionPolicy Unrestricted -Scope CurrentUser
# then
my_env\Scripts\activate

# Installing all dependencies
pip install -r requirements.txt
```

## Usage

### Game Start
- make sure the `wordrepo.txt` file is located in the source  directory
- you need to start it from the root directory of the project, then execute the following command to start the game:
```bash
python -m source.game
```

### User Interface

- **game start:** the game will display a welcome message and the instructions/rules on how to play
![Welcome Message](./images/welcome.png)

- **user input:** one can either input a single letter or the full word as a guess
![User Input](./images/input.png)
- **correct guess:** display will update and show the correctly guessed letters in the word
- **wrong guess:** display will show the wrongly guessed letters under "Fehlerhafte Diagnose" and update the health bar by removing one heart as shown above
- **having made a guess:** the user will be prompted to enter the next guess
- **game continues:** until the user has either guessed the full word correctly or has made 7 wrong guesses, which results in a loss

- **direct guess:** a user can guess directly the full word
- **if correct:** game is won
![correct word guess](./images/won.png)
- **if wrong:** game is lost
![wrong word guess](./images/lost.png)

- **after winning or losing:** the user will be prompted to play again or quit
![new round](./images/new_round.png)

## Development & Contribution

Since the project is part of a university course, contributions are not expected. However, if you want to contribute or have suggestions for improvements, feel free to fork the project, make your changes and submit a pull request. Please ensure that your code adheres to the existing style and includes appropriate tests.


## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.