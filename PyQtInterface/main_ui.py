"""
Created on Fri 19 13:55 2024

@author: keagan
This script will contain all the code to implement features listed in 'functionality_UI.txt'.
And will connect the other qlabinterface scripts.

"""


#Creating the GUI
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow, QLineEdit


#Window asking you if you want to connect to watches
#Or import pre-collected data for example test
class IntroWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUI()

    #Inital UI you will see when opening the app
    def setupUI(self):
        #Initalize central widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        #Setting up the Window
        self.setWindowTitle("Pinetime Heartbeat Interface")
        #Setting the size of the window (X size, Y size, X cords, Y cords)
        self.setGeometry(0, 0, 400, 400)

        #Creating the buttons
        self.scan_button = QPushButton("Scan for devices",self)
        self.scan_button.clicked.connect(self.on_scan_button_clicked)
        self.connect_all_button = QPushButton("Connect all devices",self)
        self.connect_all_button.clicked.connect(self.on_connect_all_button_clicked)
        self.connect_one_button = QPushButton("Connect one device",self)
        self.connect_one_button.clicked.connect(self.on_connect_one_button_clicked)
        self.disconnect_button = QPushButton("Disconnect all devices",self)
        self.disconnect_button.clicked.connect(self.on_disconnect_button_clicked)
        self.back_button = QPushButton("Back",self)
        self.back_button.clicked.connect(self.on_back_button_clicked)

        #Creating the textboxes to output
        self.num_devices_textbox = QLineEdit(self)

        #Adding the buttons to the primary layout
        self.layout1 = QVBoxLayout()
        self.layout1.addWidget(self.scan_button)
        self.layout1.addWidget(self.connect_all_button)
        self.layout1.addWidget(self.connect_one_button)
        self.layout1.addWidget(self.disconnect_button)
        #self.setLayout(layout1)

        #Adding the buttons to secondary layout
        self.layout2 = QVBoxLayout()
        self.layout2.addWidget(self.num_devices_textbox)
        self.layout2.addWidget(self.back_button)

        #Adding the buttons to the third layout

        #Set inital layout
        self.current_layout = self.layout1
        self.central_widget.setLayout(self.current_layout)


    def on_scan_button_clicked(self):
        self.switch_layout(self.layout2)
        try:
            exec(open("many_devices.py").read())
        except FileNotFoundError:
            print("File not found or not executable")
        self.num_devices_textbox.clear()
        self.num_devices_textbox.setText("Number of devices")
        #watchScan = WatchScanWindow()
        #watchScan.show()

    def on_connect_all_button_clicked(self):
        #watchConA = WatchScanWindow()
        #watchConA.show()
        pass

    def on_connect_one_button_clicked(self):
        #watchConO = WatchConAllWindow()
        #watchConO.show()
        pass

    def on_disconnect_button_clicked(self):
        #Should output telling the user all devices have been disconnected from
        #And obviously should have functionality that allows it to do this
        print("All devices disconnected")
        pass

    def on_back_button_clicked(self):
        #Go back to original layout
        self.switch_layout(self.layout1)

    def switch_layout(self, new_layout):
        #Remove old layout
        for i in reversed(range(self.current_layout.count())):
            widget = self.current_layout.itemAt(i).widget()
            self.current_layout.removeWidget(widget)
            widget.setParent(None)
        #Apply new layout
        self.current_layout = new_layout
        self.central_widget.setLayout(self.current_layout)

"""
#Window for scanning for devices
class WatchScanWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        #After the user has pressed scan button and change window scan for devices
        exec(open("many_devices.py").read())


#Window for connecting to one device
class WatchConOneWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        pass



#Window for connecting to all devices
class WatchConAllWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
            
    def initUI(self):
        pass
"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    start_window = IntroWindow()
    start_window.show()
    sys.exit(app.exec())
    