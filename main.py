"""
Main  code for tic-tac-toe game
"""
from Utils.Board import Board, InvalidMoveException
from Players.Human import Human
from random import randint
import os
import neat


def main():
    """
    Main game loop
    """
    # Initialize board
    board = Board(setup=True)
    print(board)

    # Initialize players
    player1 = Human("X")
    player2 = Human("O")

    players = (player1, player2)

    player1_turn = bool(randint(0, 1))

    while True:
        current_player = players[0] if player1_turn is True else players[1]

        valid_move = False
        while not valid_move:
            move = current_player.make_move()
            try:
                board = board.move(move)
                valid_move = True
            except InvalidMoveException:
                print("Invalid Move {}".format(move))

        print(board)

        if board.check_winning_move(move):
            break
        player1_turn = not player1_turn

    if player1_turn:
        print("Player 1 wins")
    else:
        print("Player 2 wins")


def run(config_path):
    """
    runs a feedforward neat neural network, fitness is
    determined by if the neural network wins or ties
    :param config_path:
    :return:
    """
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)
    p = neat.Population(config)
    # 50 generations may be too high
    winner = p.run(main(), 50)


if __name__ == "__main__":
    print(r""" 
     _____ _      _        _____               _____           
    /__   (_) ___| | __   /__   \__ _  ___    /__   \___   ___ 
      / /\/ |/ __| |/ /____ / /\/ _` |/ __|____ / /\/ _ \ / _ \
     / /  | | (__|   <_____/ / | (_| | (_|_____/ / | (_) |  __/
     \/   |_|\___|_|\_\    \/   \__,_|\___|    \/   \___/ \___|
""")
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)
    main()
