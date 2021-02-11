#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from GUI import *

def main():

    app = QApplication(sys.argv)

    change_theme(app)

    window = WindowWithButtons()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
