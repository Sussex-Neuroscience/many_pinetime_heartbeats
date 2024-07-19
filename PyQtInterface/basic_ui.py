"""
Created on Fri 19 13:05 2024

@author: keagan
Creating a basic UI to make sure that the library has been properly imported and setup.
@param: Takes no input except for physical button presses.
@return: Does not return anything to the user.
"""
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Main Window')
        #x,y,width,height --> X cords and Y cords
        self.setGeometry(100,100,300,200)
        
        self.button = QPushButton('Click here',self)
        self.button.clicked.connect(self.on_button_click)
        
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        
        self.setLayout(layout)
        
    def on_button_click(self):
        print('Button clicked')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

        
        


