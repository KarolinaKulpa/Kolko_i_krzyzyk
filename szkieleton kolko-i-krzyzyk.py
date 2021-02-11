#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Kółko i krzyżyk
Komputer gra w kółko i krzyżyk przeciwko człowiekowi
"""

# stałe globalne
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

# wyświetla zasady gry i obsługi programu
def display_instruct():

# odebranie od użytkownika decyzji, kto powinien rozpocząć grę
def ask_yes_no(question):

# zadanie pytania użytkownikowi, pole o którym numerze, chce zająć
# posiada system zabezpieczający przed podaniem liczby spoza zakresu
def ask_number(question, low, high):

# ustalenie do kogo należy ruch i przypisanie graczowi odpowiedniego znaku (X lub O)
def pieces():

# wyświetla planszę do gry
def display_board(board):

# komunikat o błędnym ruchu
def false_move():

# komunikat o poprawnym ruchu
def move_accepted():

# podanie informacji o ruchu komputera
def print_computer_move(move):

# wyświetla wynik gry
def congrat_winner(the_winner, computer, human):

"""
/ \
 |
 Funkcje odpowiadające za komunikację z użytkownikiem

#############################################################################################

Funkcje odpowiadające, za właściwą grę
 |
\ /
"""

# tworzy nową planszę do gry
def new_board():

# sprawdza dozwolone ruchy na zadanej planszy
def legal_moves(board):

# sprawdza wynik gry, decyduje także o remisie
def winner(board):

# odpowiada za przepisanie danych podanych od użytkownika to komputerowej reprezentacji planszy
def human_move(board, human):

# implementacja algorytmu otpowiadającego za grę komputera
def computer_move(board, computer, human):

# zmiana wykonawcy ruchu
def next_turn(turn):



# main
def main():

# rozpocznij program
main()
input("\n\nAby zakończyć grę, naciśnij klawisz Enter.")
