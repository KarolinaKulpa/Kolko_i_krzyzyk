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
   """Wyświetl instrukcję gry."""  
    print(
    """
    Witaj w największym intelektualnym wyzwaniu wszech czasów, jakim jest
    gra 'Kółko i krzyżyk'. Będzie to ostateczna rozgrywka między Twoim
    ludzkim mózgiem a moim krzemowym procesorem.  

    Swoje posunięcie wskażesz poprzez wprowadzenie liczby z zakresu 0 - 8.
    Liczba ta odpowiada pozycji na planszy zgodnie z poniższym schematem:
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

    Przygotuj się, Człowieku.  Ostateczna batalia niebawem się rozpocznie. \n
    """
    )

# odebranie od użytkownika decyzji, kto powinien rozpocząć grę
def ask_yes_no(question):
"""Zadaj pytanie, na które można odpowiedzieć tak lub nie."""
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response
   
# zadanie pytania użytkownikowi, pole o którym numerze, chce zająć
# posiada system zabezpieczający przed podaniem liczby spoza zakresu
def ask_number(question, low, high):
"""Poproś o podanie liczby z odpowiedniego zakresu."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

# ustalenie do kogo należy ruch i przypisanie graczowi odpowiedniego znaku (X lub O)
def pieces():
    """Ustal, czy pierwszy ruch należy do gracza, czy do komputera."""
    go_first = ask_yes_no("Czy chcesz mieć prawo do pierwszego ruchu? (t/n): ")
    if go_first == "t":
        print("\nWięc pierwszy ruch należy do Ciebie.  Będzie Ci potrzebny.")
        human = X
        computer = O
    else:
        print("\nTwoja odwaga Cię zgubi... Ja wykonuję pierwszy ruch.")
        computer = X
        human = O
    return computer, human


# wyświetla planszę do gry
def display_board(board):
"""Wyświetl planszę gry na ekranie."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")
    
# komunikat o błędnym ruchu
def false_move():
   print("\nTo pole jest już zajęte, niemądry Człowieku.  Wybierz inne.\n")

# komunikat o poprawnym ruchu
def move_accepted():
   print("Znakomicie...")

# podanie informacji o ruchu komputera
def print_computer_move(move):
   print("Wybieram pole numer", move)

# wyświetla wynik gry
def congrat_winner(the_winner, computer, human):
    """Pogratuluj zwycięzcy."""
    if the_winner != TIE:
        print(the_winner, "jest zwycięzcą!\n")
    else:
        print("Remis!\n")

    if the_winner == computer:
        print("Jak przewidywałem, Człowieku, jeszcze raz zostałem triumfatorem.  \n" \
              "Dowód na to, że komputery przewyższają ludzi pod każdym względem.")

    elif the_winner == human:
        print("No nie!  To niemożliwe!  Jakoś udało Ci się mnie zwieść, Człowieku. \n" \
              "Ale to się nigdy nie powtórzy!  Ja, komputer, przyrzekam Ci to!")

    elif the_winner == TIE:
        print("Miałeś mnóstwo szczęścia, Człowieku, i jakoś udało Ci się ze mną " \
              "zremisować. \nŚwiętuj ten dzień... bo to najlepszy wynik, jaki możesz " \
              "kiedykolwiek osiągnąć.")


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
  """Spowoduj wykonanie ruchu przez komputer."""
    # utwórz kopię roboczą, ponieważ funkcja będzie zmieniać listę
    board = board[:]
    # najlepsze pozycje do zajęcia według kolejności
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("Wybieram pole numer", end=" ")
    
    # jeśli komputer może wygrać, wykonaj ten ruch
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # ten ruch został sprawdzony, wycofaj go
        board[move] = EMPTY
     # jeśli człowiek może wygrać, zablokuj ten ruch
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # ten ruch został sprawdzony, wycofaj go
        board[move] = EMPTY

    # ponieważ nikt nie może wygrać w następnym ruchu, wybierz najlepsze wolne pole
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move



# zmiana wykonawcy ruchu
def next_turn(turn):



# main
def main():
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

# rozpocznij program
main()
input("\n\nAby zakończyć grę, naciśnij klawisz Enter.")
