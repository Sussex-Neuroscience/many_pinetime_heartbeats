"""
Created on Fri 19 13:55 2024

@author: keagan
This script will contain all the code to implement features listed in 'functionality_UI.txt'.
And will connect the other qlabinterface scripts.

"""

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

#Window asking you if you want to connect to watches
#Or import pre-collected data for example test
class IntroWindow(QWidget):
    def __init__(self, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
        super().__init__(parent, flags)
        self.initUI()
        
    def initUI(self):
        pass
 
    
class WatchConWindow(QWidget):
    def __init__(self, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
        super().__init__(parent, flags)
        self.initUI()
            
    def initUI(self):
        pass
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    