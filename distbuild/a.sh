#!/bin/zsh

pyinstaller -y --log-level DEBUG --onedir --specpath info --hidden-import PySide2.QtWidgets --hidden-import PySide2.QtCore --windowed tmpmain.py


