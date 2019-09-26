"""
Main  code for tic-tac-toe game
"""
from Utils.Board import Board, InvalidMoveException
from Players.Human import Human
from Players.AI import AI
from random import randint
import os
import neat
from typing import List


def main(genomes: List, config):
    """
    Main game loop
    """
    genome_number = 0
    for g in genomes:
        # Initialize board
        board = Board(setup=True)
        print(board)
        tie_game = False
        # Initialize Human Player
        player1 = Human("X")

        # Initialize AI
        g[1].fitness = 0
        net = neat.nn.FeedForwardNetwork.create(g[1], config)
        player2 = AI("O", net, config, board)

        players = (player1, player2)
        player1_turn = bool(randint(0, 1))
        ai_wrong_move = False
        while True:
            print(g[1].fitness)
            player2.board = board
            current_player = players[0] if player1_turn is True else players[1]
            valid_move = False
            while not valid_move:
                if current_player is player2 and ai_wrong_move is False or current_player is player1:
                    move = current_player.make_move()
                    g[1].fitness += 0.4
                elif current_player is player2 and ai_wrong_move is True:
                    move = current_player.randomize()
                try:
                    board = board.move(move)
                    valid_move = True
                    ai_wrong_move = False
                except InvalidMoveException:
                    if current_player is player2:
                        ai_wrong_move = True
                        g[1].fitness -= 5

                    print("Invalid Move {}".format(move))

            print(board)

            if board.check_winning_move(move):
                break
            if len(board.get_valid_moves()) is 0:
                print("Tie Game")
                g[1].fitness += 5
                tie_game = True
                break
            player1_turn = not player1_turn

        if player1_turn and not tie_game:
            print("Player 1 wins")
            g[1].fitness -= 2
        elif not player1_turn and not tie_game:
            print("Player 2 wins")
            g[1].fitness += 8

            # add fitness?


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
    winner = p.run(main, 50)


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

