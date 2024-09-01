"""
Created on Fri 19 13:55 2024

@author: keagan
This script will contain all the code to implement features listed in 'functionality_UI.txt'.
And will connect the other qlabinterface scripts.

"""

# Creating the GUI
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

#Window asking you if you want to connect to watches
#Or import pre-collected data for example test
class IntroWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Pinetime Heartbeat Interface")
        # Setting the size of the window (X size, Y size, X cords, Y cords)
        self.setGeometry(0, 0, 400, 400)

        # Creating the buttons
        self.scan_button = QPushButton("Scan for devices",self)
        self.scan_button.clicked.connect(self.on_scan_button_clicked)
        self.connect_all_button = QPushButton("Connect all devices",self)
        self.connect_all_button.clicked.connect(self.on_connect_all_button_clicked)
        self.connect_one_button = QPushButton("Connect one device",self)
        self.connect_one_button.clicked.connect(self.on_connect_one_button_clicked)

        # Adding the buttons to the layout
        layout = QVBoxLayout()
        layout.addWidget(self.scan_button)
        layout.addWidget(self.connect_all_button)
        layout.addWidget(self.connect_one_button)
        self.setLayout(layout)

    def on_scan_button_clicked(self):
        watchScan = WatchScanWindow()
        watchScan.show()

    def on_connect_all_button_clicked(self):
        watchConA = WatchScanWindow()
        watchConA.show()

    def on_connect_one_button_clicked(self):
        watchConO = WatchConAllWindow()
        watchConO.show()

# Window for scanning for devices
class WatchScanWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        # After the user has pressed scan button and change window scan for devices
        exec(open("many_devices.py").read())


# Window for connecting to one device
class WatchConOneWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        pass



# Window for connecting to all devices
class WatchConAllWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
            
    def initUI(self):
        pass
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    start_window = IntroWindow()
    start_window.show()
    sys.exit(app.exec())
    