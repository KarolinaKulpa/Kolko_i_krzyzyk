#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from pygame import mixer

from engine import *


class WindowWithButtons(QWidget):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        QApplication.setStyle(QStyleFactory.create("Fusion"))

        mixer.init()

        self.press_sound = mixer.Sound("music/press_effect.wav")

        self.buttons = []

        self.board = Board()

        self.turn = Turn()

        self.main_structure()

    def main_structure(self):

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Kółko i krzyżyk')

        self.setWindowIcon(QIcon("graphics/cross.ico"))

        for button_nmb in range(0, 9):
            self.buttons.append(QPushButton(EMPTY, self))  # 'stała' EMPTY jest powinna zostać zdefiniowana w silniku
            self.buttons[button_nmb].clicked.connect(self.button_clicked)
            self.buttons[button_nmb].setObjectName("button%d" % button_nmb)
            self.buttons[button_nmb].resize(100, 100)

            self.buttons[button_nmb].setIcon(QIcon("EMPTY_ICON.ico"))
            self.buttons[button_nmb].setIconSize(QtCore.QSize(50, 50))

        self.buttons[0].move(50, 50)

        self.buttons[1].move(200, 50)

        self.buttons[2].move(350, 50)

        self.buttons[3].move(50, 200)

        self.buttons[4].move(200, 200)

        self.buttons[5].move(350, 200)

        self.buttons[6].move(50, 350)

        self.buttons[7].move(200, 350)

        self.buttons[8].move(350, 350)

        self.show()

        mixer.music.load('music/background_music.wav')
        mixer.music.play(-1)

    def button_clicked(self):

        button = self.sender()

        # jeśli pole nie jest zajęte
        if int(button.objectName()[-1:]) in legal_moves(self.board.give_board()):

            mixer.Channel(1).play(self.press_sound)

            # jeśli nie ma jeszcze zwycięzcy
            if not winner(self.board.give_board()):
                self.board.change_board(int(button.objectName()[-1:]), self.turn.give_turn())
                self.turn.change_turn()
                button.setIcon(QIcon("graphics/cross.ico"))
                button.setIconSize(QtCore.QSize(50, 50))

            if not winner(self.board.give_board()):
                move = computer_move(self.board.give_board(), O, X)
                self.board.change_board(move, self.turn.give_turn())
                self.turn.change_turn()
                self.buttons[move].setIcon(QIcon("graphics/circle.ico"))
                self.buttons[move].setIconSize(QtCore.QSize(50, 50))

            # w przypadku remisu
            if winner(self.board.give_board()) == TIE:
                mixer.music.set_volume(0.5)
                mixer.Channel(2).play(mixer.Sound("music/tie.wav"))
                rep = QMessageBox.question(self, 'Koniec gry', "Remis       \n\nCzy chcesz zagrać jeszcze raz?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

                if rep == QMessageBox.Yes:

                    self.board.reset_board()
                    mixer.Channel(5).play(mixer.Sound('music/restart_effect.wav'))
                    mixer.music.set_volume(1)
                    self.turn.change_turn()

                    for button in self.buttons:
                        button.setIcon(QIcon("EMPTY_ICON.ico"))
                        button.setIconSize(QtCore.QSize(50, 50))

                else:
                    self.close()
            # w przypadku wygranej X == człowieka
            elif winner(self.board.give_board()) == "X":
                mixer.music.set_volume(0.5)
                mixer.Channel(2).play(mixer.Sound("music/win.wav"))
                rep = QMessageBox.question(self, 'Koniec gry',
                                           "Brawo, zwyciężyłeś!       \n\nCzy chcesz zagrać jeszcze raz?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

                if rep == QMessageBox.Yes:
                    self.board.reset_board()

                    mixer.music.set_volume(1)

                    for button in self.buttons:
                        button.setIcon(QIcon("EMPTY_ICON.ico"))

                else:
                    self.close()

            # w przypadku wygranej O == komputera
            elif winner(self.board.give_board()) == "O":
                mixer.music.set_volume(0.5)
                mixer.Channel(2).play(mixer.Sound("music/lose.wav"))

                rep = QMessageBox.question(self, 'Koniec gry',
                                           "Tym razem komputer był lepszy       \n\nCzy chcesz zagrać jeszcze raz?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

                if rep == QMessageBox.Yes:
                    self.board.reset_board()

                    for button in self.buttons:
                        button.setIcon(QIcon("EMPTY_ICON.ico"))

                    mixer.Channel(4).play(mixer.Sound('music/restart_effect.wav'))

                    mixer.music.set_volume(1)

                else:
                    self.close()


def change_theme(app):
    palette = QPalette()

    # zmiana koloru okna
    palette.setColor(QPalette.Window, QColor(30, 100, 100))

    # zmiana koloru czcionki
    palette.setColor(QPalette.WindowText, Qt.white)

    # zmiana koloru przycisków
    palette.setColor(QPalette.Button, QColor(30, 100, 100))
    palette.setColor(QPalette.ButtonText, Qt.white)

    # ustawienie wykonanej palety
    app.setPalette(palette)


if __name__ == "__main__":
    pass
