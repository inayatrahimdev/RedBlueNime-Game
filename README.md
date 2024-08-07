# RedBlueNim-DEP
# Red-Blue Nim Game

![Game Image](https://via.placeholder.com/800x200?text=Red-Blue+Nim+Game)

## Project Overview

The Red-Blue Nim Game is an engaging and interactive game developed using Python. It allows players to strategically remove marbles from two colors (red and blue) until one color runs out. This game supports both human and computer players, offering a challenging and fun experience.

## Features

- **User-Friendly Interface**: Seamless gameplay experience with simple inputs.
- **Two Game Versions**: Choose between Standard and Misere versions of the game.
- **Intelligent Computer Opponent**: Play against a smart AI for a challenging game.
- **Clear and Concise Code**: Easy to understand and modify for further enhancements.

## Learning Outcomes

- Improved understanding of game theory and AI.
- Enhanced Python programming skills, especially in handling user input and game logic.
- Gained experience in implementing turn-based game mechanics.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/inayatrahimdev/RedBlueNim-DEP.git
    ```
2. Navigate to the project directory:
    ```sh
    cd RedBlueNim-DEP
    ```
    
## Running the Game

To run the game, use the following command:
```sh
python rb_game.py <num_red> <num_blue> <version> <first_player> <depth>
```
Replace the placeholders with appropriate values:

- <num_red>: Number of red marbles (e.g., 10)
- <num_blue>: Number of blue marbles (e.g., 10)
- <version>: Game version (standard or misere)
- <first_player>: First player (human or computer)
- <depth>: Depth for AI search (not used in this implementation but required)
Example Command
```sh
python rb_game.py 10 10 standard human 0
```
## How to Play
- Human's Move: Enter 'red' or 'blue' to select the color of marbles to remove. Then, enter 1 or 2 to specify the number of marbles to remove.
- Computer's Move: The computer will automatically remove 1 or 2 marbles from the color with the remaining marbles.
- The game continues until one color runs out of marbles. The winner is determined based on the chosen game version.

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Thanks to the open-source community for the tools and resources that made this project possible.

# Contact
For any questions or suggestions, feel free to contact me:
**Email: inayatrahim006@gmail.com**
