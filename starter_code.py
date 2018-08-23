#!/usr/bin/env python3

import random
import string

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def get_rounds_of_play():
    while True:
        rounds = input("Enter the number of rounds to play: ")
        if not rounds.isdigit():
            print("Please enter numbers only")
            continue
        return int(rounds)


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p1_count = 0
        self.p2 = p2
        self.p2_count = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\tPlayer 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if (beats(move1, move2)):
            print("\t** PLAYER ONE WINS **")
            self.p1_count += 1
        elif(beats(move2, move1)):
            print("\t** PLAYER TWO WINS **")
            self.p2_count += 1
        else:
            print("\t** It's a draw **")
        print(f"\tScore: Player One {self.p1_count}, "
              f"Player Two {self.p2_count} \n")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")

    def play_game_two_player(self, rounds=3):
        print("Rock Paper Scissors, Go!")
        for round in range(rounds):
            print(f"Round {round}:")
            self.play_round()
        print("Game Over!\n")
        if self.p1_count > self.p2_count:
            print("** Player ONE WON THE GAME **")
        elif self.p1_count < self.p2_count:
            print("** Player TWO WON THE GAME **")
        else:
            print("** NO ONE WON.....PEACE OUT **")
        print(f"Final Score: Player One {self.p1_count},"
              f"Player Two {self.p2_count}")


class RockPlayer(Player):

    def move(self):
        return moves[0]


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        move1 = None
        while True:
            if move1 not in moves:
                move1 = input("rock, paper, scissors? > ")
            else:
                break
        return move1

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    '''A ReflectPlayer class that remembers what move the
       opponent played last round, and plays that move this round.'''

    def __init__(self):
        self.opponent_last_move = None

    def move(self):
        if self.opponent_last_move is not None:
            return self.opponent_last_move
        else:
            return random.choice(moves)

    def learn(self, my_move, their_move):
        self.opponent_last_move = their_move


class CyclePlayer(Player):
    '''A CyclePlayer class that remembers what move _it_ played last round,
    and cycles through the different moves.'''

    def __init__(self):
        self.ind = 0

    def move(self):
        return moves[self.ind]

    def learn(self, my_move, their_move):
        self.ind = moves.index(my_move)
        self.ind += 1
        self.ind = self.ind % 3


if __name__ == '__main__':
    '''game = Game(Player(), Player())
    game.play_game()'''
    choices = [1, 2, 3, 4, 5, 6]

    input_cont = True
    while input_cont:
        print('''
Welcome to Rock, paper, scissors...!

Select the game you want to play-
    1. Random game
    2. Human vs Random Player(Rock only)
    3. Human vs Random Player
    4. Human vs Reflect Player
    5. Human vs Cycle Player
    6. Quit''')
        choice_input = input("\nYour Choice > ")
        if not choice_input.isdigit():
            print("Please enter numbers only: ")
            continue
        choice = int(choice_input)
        if choice not in choices:
            print("Please enter from above options only")
            continue

        if choice == 1:
            print("\n** Random game **\n")
            random_game = Game(RandomPlayer(), RandomPlayer())
            random_game.play_game_two_player()
        elif choice == 2:
            print("\n** Human vs Random Player(Rock only) **\n")
            rounds = get_rounds_of_play()
            human_random_game = Game(HumanPlayer(), RockPlayer())
            human_random_game.play_game_two_player(int(rounds))
        elif choice == 3:
            print("\n** Human vs Random Player **\n")
            rounds = get_rounds_of_play()
            human_random_game = Game(HumanPlayer(), RandomPlayer())
            human_random_game.play_game_two_player(int(rounds))
        elif choice == 4:
            print("\n** Human vs Reflect Player **\n")
            rounds = get_rounds_of_play()
            human_reflect_game = Game(HumanPlayer(), ReflectPlayer())
            human_reflect_game.play_game_two_player(int(rounds))
        elif choice == 5:
            print("\n** Human vs Cycle Player **\n")
            rounds = get_rounds_of_play()
            human_cycle_game = Game(HumanPlayer(), CyclePlayer())
            human_cycle_game.play_game_two_player(int(rounds))
        elif choice == 6:
            input_cont = False
            print("Goodbye....!!!")
