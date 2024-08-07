import argparse

class RbGame:
    def __init__(self, num_red, num_blue, version, first_player, depth):
        self.num_red = num_red
        self.num_blue = num_blue
        self.version = version
        self.first_player = first_player
        self.depth = depth
        self.board = {"red": num_red, "blue": num_blue}

    def print_board(self):
        print("Current board: Red = {}, Blue = {}".format(self.board["red"], self.board["blue"]))

    def get_valid_input(self, prompt):
        while True:
            try:
                num_marbles = int(input(prompt))
                if num_marbles in [1, 2]:
                    return num_marbles
                else:
                    print("Invalid input. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def human_move(self):
        print("Your move:")
        color = input("Enter 'red' or 'blue' to remove marbles: ").strip().lower()
        while color not in ["red", "blue"]:
            color = input("Invalid color. Enter 'red' or 'blue': ").strip().lower()
        num_marbles = self.get_valid_input("Enter 1 or 2 to remove marbles: ")
        self.board[color] -= num_marbles
        print(f"You removed {num_marbles} {color} marbles.")

    def computer_move(self):
        print("Computer's move:")
        color = "red" if self.board["red"] > 0 else "blue"
        num_marbles = min(2, self.board[color])
        self.board[color] -= num_marbles
        print(f"Computer removes {num_marbles} {color} marbles.")

    def is_game_over(self):
        return self.board["red"] == 0 or self.board["blue"] == 0

    def get_winner(self):
        if self.version == "standard":
            return "Human" if self.is_game_over() else "Computer"
        else:
            return "Computer" if self.is_game_over() else "Human"

    def play(self):
        current_player = self.first_player
        print(f"Game start! Version: {self.version}, First player: {current_player}")
        
        while not self.is_game_over():
            self.print_board()
            if current_player == "human":
                self.human_move()
                current_player = "computer"
            else:
                self.computer_move()
                current_player = "human"
        
        self.print_board()
        print("Game over! The winner is:", self.get_winner())

def main():
    parser = argparse.ArgumentParser(description="Red-Blue Nim Game")
    parser.add_argument("num_red", type=int, help="Number of red marbles")
    parser.add_argument("num_blue", type=int, help="Number of blue marbles")
    parser.add_argument("version", choices=["standard", "misere"], help="Game version")
    parser.add_argument("first_player", choices=["human", "computer"], help="First player")
    parser.add_argument("depth", type=int, help="Depth for AI search (not used in this implementation)")

    args = parser.parse_args()

    game = RbGame(args.num_red, args.num_blue, args.version, args.first_player, args.depth)
    game.play()

if __name__ == "__main__":
    main()
