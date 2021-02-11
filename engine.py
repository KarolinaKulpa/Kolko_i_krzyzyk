#!/usr/bin/python
# -*- coding: utf-8 -*-

# 'stałe' globalne
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9
X = "X"
O = "O"


# klasa przechowująca oraz rozporządzająca ruchami
class Turn:

    def __init__(self):
        self.turn = X

    # zwraca obecny ruch
    def give_turn(self):
        return self.turn

    # odpowiada za zmianę ruchu
    def change_turn(self):
        self.turn = X if self.turn == O else O


# klasa przechowująca oraz rozporządzająca planszą
class Board:

    # tworzy pustą planszę
    def __init__(self):
        self.board = NUM_SQUARES * [EMPTY]

    def give_board(self):
        return self.board

    # zmienia stan danego miejsca na planszy
    def change_board(self, position: int, value):
        self.board[position] = value

    # resetuje plansze do stanu początkowego
    def reset_board(self):
        self.board = NUM_SQUARES * [EMPTY]


# zwraca listę dozwolonych ruchów
def legal_moves(board):
    """Utwórz listę prawidłowych ruchów."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


# wyznacza zwycięzcę
def winner(board):
    """Ustal zwycięzcę gry."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None


# algorytm odpowiadający za grę komputera - zwraca nr. pola planszy
def computer_move(board, computer, human):
    """Spowoduj wykonanie ruchu przez komputer."""
    # utwórz kopię roboczą, ponieważ funkcja będzie zmieniać listę
    board = board[:]

    # najlepsze pozycje do zajęcia według kolejności
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    # jeśli komputer może wygrać, wykonaj ten ruch
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            return move
        # ten ruch został sprawdzony, wycofaj go
        board[move] = EMPTY

    # jeśli człowiek może wygrać, zablokuj ten ruch
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            return move
        # ten ruch został sprawdzony, wycofaj go
        board[move] = EMPTY

    # jeszcze jedna możliwość zrobienia pułapki przez czlowieka
    if human in board[5] and human in board[7]:
        if 8 in legal_moves(board):
            return 8

    # jeśli człowiek próbuje oskrzydlić komputer
    for move in (1, 3, 5, 7):
        if (human in board[0] and human in board[8]) or (human in board[2] and human in board[6]):
            if move in legal_moves(board):
                board[move] = computer
                return move

    # ponieważ nikt nie może wygrać w następnym ruchu, wybierz najlepsze wolne pole
    for move in BEST_MOVES:
        if move in legal_moves(board):
            return move


if __name__ == "__main__":
    pass
