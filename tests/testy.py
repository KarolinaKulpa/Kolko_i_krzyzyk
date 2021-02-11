#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from engine import *

class legal_movesTest(unittest.TestCase):
    def test_empty_board(self):
        board = Board()
        self.assertEqual([i for i in range(NUM_SQUARES)], legal_moves(board.give_board()))

    def test_board_full_of_X(self):
        board = Board()
        for square in range(NUM_SQUARES):
            board.change_board(square, X)
        self.assertEqual([], legal_moves(board.give_board()))

    def test_board_full_of_O(self):
        board = Board()
        for square in range(NUM_SQUARES):
            board.change_board(square, O)
        self.assertEqual([], legal_moves(board.give_board()))

    def test_some_empty_squares(self):
        board = Board()
        board.change_board(3, X)
        board.change_board(2, O)
        board.change_board(7, X)
        self.assertEqual([i for i in range(NUM_SQUARES) if i not in (2, 3, 7)], legal_moves(board.give_board()))


class computer_moveTest(unittest.TestCase):
    def test_posibility_to_win(self):

        board = Board()

        human = X
        computer = O

        board.change_board(0, computer)
        board.change_board(1, computer)
        board.change_board(3, human)
        board.change_board(4, human)

        turn = computer_move(board.give_board(), computer, human)

        self.assertEqual(2, turn)

    def test_danger_elimination(self):

        board = Board()

        human = X
        computer = O

        board.change_board(7, computer)
        board.change_board(1, computer)
        board.change_board(3, human)
        board.change_board(4, human)

        self.assertEqual(5, computer_move(board.give_board(), computer, human))

    def test_detect_trap(self):

        board = Board()

        human = X
        computer = O

        board.change_board(4, computer)

        board.change_board(0,  human)
        board.change_board(8, human)

        turn = computer_move(board.give_board(), computer, human)

        self.assertIn(turn, (1, 3, 5, 7))


class winnerTest(unittest.TestCase):
    def test_winner_in_row(self):
        board = Board()
        human = X
        computer = O

        board.change_board(0, computer)
        board.change_board(1, computer)
        board.change_board(2, computer)
        board.change_board(3, human)
        board.change_board(4, human)

        self.assertEqual(computer, winner(board.give_board()))

    def test_winner_in_col(self):
        board = Board()
        human = X
        computer = O

        board.change_board(0, computer)
        board.change_board(3, computer)
        board.change_board(6, computer)
        board.change_board(5, human)
        board.change_board(4, human)

        self.assertEqual(computer, winner(board.give_board()))

    def test_winner_diag(self):
        board = Board()
        human = X
        computer = O

        board.change_board(0, computer)
        board.change_board(4, computer)
        board.change_board(8, computer)
        board.change_board(3, human)
        board.change_board(5, human)

        self.assertEqual(computer, winner(board.give_board()))

if __name__ == "__main__":
    print("Moduł testowy silnika gry kółko i krzyżyk")
