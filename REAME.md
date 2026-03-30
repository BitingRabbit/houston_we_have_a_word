![Main Branch Results](https://img.shields.io/badge/Main%20Branch%20Buildresults:-blue)
![pylint-score](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/JuliusWiedemann/d506acc54dead9ca1d070488e813d253/raw/pylint-score.json)
![mypy-warnings](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/JuliusWiedemann/d506acc54dead9ca1d070488e813d253/raw/mypy_warnings.json)
![coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/JuliusWiedemann/d506acc54dead9ca1d070488e813d253/raw/coverage.json)
[![license](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

# Houston we have a word

## Description
"Houston We Have A Word" is a command-line based word guessing game inspired by the classic Hangman.
Set in the dramatic events of the Apollo 13 mission in 1970, the player takes the seat at Mission Control in Houston. An oxygen tank has exploded on board and the player must bring the crew home safely by deciphering the hidden word related to space and aviation.

### Project Structure

- organized into two main directories: `source` for the game implementation and `tests` for unit tests
```
project/
├── source/
│   ├── game.py
│   ├── display.py
│   ├── game_logic.py
│   ├── word_loader.py
│   └── wordrepo.txt
└── tests/
    ├── test_game.py
    ├── test_display.py
    ├── test_game_logic.py
    └── test_word_loader.py
```

## Installation
```bash
git clone https://github.com/BitingRabbit/houston_we_have_a_word.git
cd project
python -m venv .venv
source .venv/bin/activate
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
- **wrong guess:** display will show the wrongly guessed letters under "Falsche Signale" and update the health bar by removing one heart as shown above
- **having made a guess:** the user will be prompted to enter the next guess
- **game continues:** until the user has either guessed the full word correctly or has made 6 wrong guesses, which results in a loss

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
MIT License

Copyright (c) 2026 Christoph Gahabka

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.