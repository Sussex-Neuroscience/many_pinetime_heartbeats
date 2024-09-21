"""
Created on Mon Sep 2 21:30 2024

@author: keagan
This script will contain all the code to implement features listed in 'functionality_UI.txt'.
And will connect the other qlabinterface scripts.
"""
import threading
import asyncio
import threading
import numpy as np
from bleak import BleakScanner, BleakClient
from bleak.exc import BleakDeviceNotFoundError, BleakError
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QStackedWidget, QTextEdit, QFileDialog, QComboBox, QApplication
from PyQt6.QtCore import QThread, pyqtSignal, QTimer, Qt

#Class to deal with asyncio functions never executing due to threading issues
class DeviceWorker(QThread):
    #Signal to send data back to main thread
    update_signal = pyqtSignal(str)

    def __init__(self, devices):
        super().__init__()
        self.devices = devices

    #Connect to device
    async def connect_to_device(self, address):
        print(f"Connect to device: {address}")
        #UUIDs for reading
        HEART_RATE_UUID = "00002a37-0000-1000-8000-00805f9b34fb"
        STEP_COUNT_UUID = "00030001-78fc-48fe-8e23-433b3a1942d0"
        RAW_XYZ_UUID = "00030002-78fc-48fe-8e23-433b3a1942d0"

        #Logic
        try:
            async with BleakClient(address) as client:
                heart_buffer = await client.read_gatt_char(HEART_RATE_UUID)
                step_buffer = await client.read_gatt_char(STEP_COUNT_UUID)
                raw_buffer = await client.read_gatt_char(RAW_XYZ_UUID)

                raw_data = np.frombuffer(raw_buffer, dtype=np.int16)
                step_data = np.frombuffer(step_buffer, dtype=np.int16)
                heart_data = np.frombuffer(heart_buffer, dtype=np.int8)

                result = f"Device {address} connected.\nMotion: {raw_data}\nHeart Rate: {heart_data[1]}\nStep Count: {step_data[0]}\n"
                return result
        except Exception as e:
            return f"Error connecting to device {address}: {e}"
        except BleakDeviceNotFoundError:
            return f"Device {address} not found"
        finally:
            if client.is_connected:
                await client.disconnect()

    #Connect to all devices
    async def connect_all_devices(self):
        results = []
        #Checking self.devices has devices
        print(f"Devices to connect: {self.devices}")
        try:
            for device in self.devices:
                print(f"Connecting to device: {device[0]}")
                result = await self.connect_to_device(device[0])
                print(f"Emitting result for device: {result}")
                results.append(result)
                print(results)
                self.update_signal.emit(result)
            return results
        except Exception as e:
            print(f"Error connecting to device: {e}")

    #Running the asyncio function
    def run(self):
        #asyncio.run(self.connect_all_devices())
        #asyncio.create_task(self.connect_all_devices())
        #Checking that working thread is running
        print("Worker thread started")
        loop = asyncio.get_event_loop()
        asyncio.set_event_loop(loop)
        try:
            print("Connecting to devices")
            loop.run_until_complete(self.connect_all_devices())
        except Exception as e:
            print(f"Error connecting to devices: {e}")



#Main Window class
class IntroWindow(QMainWindow):
    update_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setupUI()
        #Create asyncio event loop
        self.event_loop = asyncio.new_event_loop()
        #Start event loop in seperate thread
        self.async_thread = threading.Thread(target = self.start_asyncio_loop, daemon=True)
        self.async_thread.start()

    def setupUI(self):
        self.setWindowTitle("Pinetime Heartbeat Interface")
        self.setGeometry(0, 0, 400, 400)

        #Initialize QStackedWidget
        self.central_widget = QStackedWidget(self)
        self.setCentralWidget(self.central_widget)

        #Initalizing variables
        self.device_info = []
        self.device_info_stats = []

        #Layout 1: Initial Layout
        layout1_widget = QWidget(self)
        layout1_vbox = QVBoxLayout()
        ##Adding scan button + functionality
        self.scan_button = QPushButton("Scan for devices", self)
        self.scan_button.clicked.connect(self.on_scan_button_clicked)
        ##Adding connect all devices button + functionality
        self.connect_all_button = QPushButton("Connect all devices", self)
        self.connect_all_button.clicked.connect(self.on_connect_all_button_clicked)
        ##Adding connect one device button + functionality
        self.connect_one_button = QPushButton("Connect one device", self)
        self.connect_one_button.clicked.connect(self.on_connect_one_button_clicked)
        ##Exit button to close application
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.clicked.connect(self.close)
        layout1_vbox.addWidget(self.scan_button)
        layout1_vbox.addWidget(self.connect_all_button)
        layout1_vbox.addWidget(self.connect_one_button)
        layout1_vbox.addWidget(self.exit_button)
        layout1_widget.setLayout(layout1_vbox)

        #Layout 2: After Scanning
        layout2_widget = QWidget(self)
        layout2_vbox = QVBoxLayout()
        ##Adding text boxes which output text to user
        self.num_devices_textbox = QLineEdit(self)
        self.device_info_textbox = QTextEdit(self)
        ##Adding back button + functionality
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.on_back_button_clicked)
        layout2_vbox.addWidget(self.num_devices_textbox)
        layout2_vbox.addWidget(self.device_info_textbox)
        layout2_vbox.addWidget(self.back_button)
        layout2_widget.setLayout(layout2_vbox)

        #Layout 3: Connect all devices
        # Just using list already generated connect to each device seperately, read data and add it to a list
        # The list will have each element representing a device
        # Want output box representing "All devices connected", what data getting out
        layout3_widget = QWidget(self)
        layout3_vbox = QVBoxLayout()
        ##Adding text boxes which output text to user
        self.user_info_textbox = QLineEdit(self)
        self.devices_info_textbox = QTextEdit(self)
        ##Adding back button + functionality
        self.back_button2 = QPushButton("Back", self)
        self.back_button2.clicked.connect(self.on_back_button_clicked)
        layout3_vbox.addWidget(self.user_info_textbox)
        layout3_vbox.addWidget(self.devices_info_textbox)
        layout3_vbox.addWidget(self.back_button2)
        layout3_widget.setLayout(layout3_vbox)


        #Layout 4: Connect one device
        # Need text input box to enter max code or drop down to select which device, for this I will be using a drop-down box
        layout4_widget = QWidget(self)
        layout4_vbox = QVBoxLayout()
        ##Adding drop-down box with device and mac address to choose from + functionality
        self.combobox_devices = QComboBox(self)
        #self.combobox_devices.addItem("Select a Device")
        #self.combobox_devices.addItems(self.device_info)
        ##Showing output to users

        ##Adding back button + functionality
        self.back_button3 = QPushButton("Back", self)
        self.back_button3.clicked.connect(self.on_back_button_clicked)
        layout4_vbox.addWidget(self.combobox_devices)
        layout4_vbox.addWidget(self.back_button3)
        layout4_widget.setLayout(layout4_vbox)

        #Add layouts to the QStackedWidget
        self.central_widget.addWidget(layout1_widget)  #Index 0
        self.central_widget.addWidget(layout2_widget)  #Index 1
        self.central_widget.addWidget(layout3_widget)  #Index 2
        self.central_widget.addWidget(layout4_widget)  #Index 3

        #Start with layout 1
        self.central_widget.setCurrentIndex(0)

    def on_scan_button_clicked(self):
        #Change to the second layout
        self.central_widget.setCurrentIndex(1)
        #Running the bleak function
        try:
            async def main():
                devices = await BleakScanner.discover()
                #Explicity raise an error if no devices found
                if not devices:
                    raise BleakError("No devices found")
                for d in devices:
                    print(d)
                return devices
            devices = asyncio.run(main())
            print(devices)
            #Showing how many devices there are around
            self.num_devices_textbox.setText(f"Number of devices: {len(devices)} ")
            #Clearing previous list and combo box
            self.combobox_devices.clear()
            self.combobox_devices.addItem("Select a Device")
            #Showing the all device information
            self.device_info = []
            for device in devices:
                self.device_info_textbox.insertPlainText(str(device)+"\n")
                #Adding device address and name to list to be accessed later
                if device.name == "InfiniTime":
                    self.device_info.append([device.address,device.name])
            print(self.device_info)
            #Adding devices names to combo box
            for device in self.device_info:
                self.combobox_devices.addItem(str(device))
        except BleakError as e:
            print(f"Error occured during scanning: {e}")
            self.num_devices_textbox.setText("Please turn your bluetooth on")
        except OSError as e:
            error = str(e)
            print(f"Error occured during scanning: {error}")
            if "WinError -2147020577" in error:
                self.num_devices_textbox.setText("Please turn your bluetooth on")
            else:
                self.num_devices_textbox.setText("An unexpected error occurred")
        except Exception as e:
            print(f"An error occurred: {e}")
            self.num_devices_textbox.setText("An unexpected error occurred")

    def on_connect_all_button_clicked(self):
        #Change to third layout
        self.central_widget.setCurrentIndex(2)
        """
        #UUIDs I want to use
        MOTION_SERVICE_UUID = "00030000-78fc-48fe-8e23-433b3a1942d0"
        STEP_COUNT_UUID = "00030001-78fc-48fe-8e23-433b3a1942d0"
        RAW_XYZ_UUID = "00030002-78fc-48fe-8e23-433b3a1942d0"
        HEART_RATE_UUID = "00002a37-0000-1000-8000-00805f9b34fb"
        MODEL_NBR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"

        notify_uuid = STEP_COUNT_UUID
        """
        """
        async def connect_to_device(address):
            print("starting", address, "loop")
            async with BleakClient(address, timeout=5.0) as client:

                print("connect to", address)
                try:
                    await client.start_notify(notify_uuid, callback)
                    await asyncio.sleep(10.0)
                    await client.stop_notify(notify_uuid)
                except Exception as e:
                    print(e)
                # Actually allows the watch to be disconnected
                finally:
                    await client.disconnect()
            print("disconnect from", address)
        def callback(characteristic, data):
            print(characteristic, data)

        def main(addresses):
            return asyncio.gather(*(connect_to_device(address[0]) for address in addresses))

        try:
            asyncio.run(main(self.device_info))
            
        except Exception as e:
            print(f"An error occurred: {e}")
        """
        """
        async def main(address):
            #Only have one item
            #for item in address:
            #    print(item)
            try:
                async with BleakClient(address) as client:

                    # model_number = await client.read_gatt_char(MODEL_NBR_UUID)
                    # print(model_number)
                    heart_buffer = await client.read_gatt_char(HEART_RATE_UUID)

                    step_buffer = await client.read_gatt_char(STEP_COUNT_UUID)

                    raw_buffer = await client.read_gatt_char(RAW_XYZ_UUID)

                    raw_data = np.frombuffer(raw_buffer, dtype=np.int16)
                    step_data = np.frombuffer(step_buffer, dtype=np.int16)
                    heart_data = np.frombuffer(heart_buffer, dtype=np.int8)

                    print("motion")
                    print(raw_data)

                    print("heart rate")
                    # print(heart_rate)
                    print(heart_data[1])

                    print("step count")
                    print(step_data[0])

                    return {"raw":raw_data,"step":step_data,"heart":heart_data}
            except BleakDeviceNotFoundError:
                print(address + " device not found")

            finally:
                await client.disconnect()
                print("devices disconnected")

        #Iterating through each device in device_info and getting their data
        try:
            self.user_info_textbox.setText("All devices connected to and data received")
            for device in self.device_info:
                characteristics = asyncio.run(main(device[0]))
                self.device_info_textbox.insertPlainText(str(characteristics) + "\n")
                self.device_info_stats.append(characteristics)
        except Exception as e:
            print("Error occured: ",e)
        """
        try:
            self.user_info_textbox.setText("All devices connected to and data received")
            self.worker = DeviceWorker(self.device_info)
            print("first")
            self.worker.update_signal.connect(self.update_device_info_multiple)
            print("second")
            self.worker.start()
            print("third")
        except Exception as e:
            print(f"An error occurred: {e}")

    def update_device_info_multiple(self, info):
        #self.device_info_textbox.setText("All devices connected to and data received")
        #self.device_info_stats.append(info)
        #Checking if function is being called
        print("Function has been called")
        #Seeing how many times its being called
        global call_count
        call_count += 1
        print(call_count)
        try:
            print(f"updating device_info: {info}")
            if self.device_info_textbox:
                self.devices_info_textbox.insertPlainText(info)
            else:
                print("devices_info_textbox is not initalized")
        except Exception as e:
            print(f"Error occured: ",e)

    def update_device_info_one(self, info):
        try:
            print(f"updating device_info: {info}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def on_connect_one_button_clicked(self):
        #Change to layout 4
        self.central_widget.setCurrentIndex(3)
        # Getting the current selection on drop-down menu
        self.combobox_devices.currentIndexChanged.connect(self.combo_box_changed)

    def combo_box_changed(self):
        choice = self.combobox_devices.currentText()
        try:
            #Find corresponding address for selected device
            for device in self.device_info:
                if device[1] == choice:
                    selected_address = device[0]
                    break
            self.worker = DeviceWorker(choice)
            self.worker.update_signal.connect(self.update_device_info_one)
            self.worker.start()

        except Exception as e:
            print(f"An error occurred: {e}")


    def on_back_button_clicked(self):
        #Go back to the first layout
        self.central_widget.setCurrentIndex(0)

    def start_asyncio_loop(self):
        #Start asyncio loop in seperate thread
        try:
            asyncio.set_event_loop(self.event_loop)
            self.event_loop.run_forever()
        except Exception as e:
            print(f"An error occurred: {e}")

    def close_asyncio_loop(self, event):
        #Stop asyncio loop and close thread when exiting app
        try:
            if hasattr(self, "event_loop") and self.event_loop.is_running():
                self.event_loop.call_soon_threadsafe(self.event_loop.close)
            #Ensure asyncio thread if closed
            if hasattr(self, "async_thread") and self.async_thread.is_alive():
                self.async_thread.join()
            event.accept()
        except Exception as e:
            print(f"An error occurred: {e}")



if __name__ == '__main__':
    #Combating error regarding bleak and thread
    try:
        from bleak.backends.winrt.util import allow_sta
        allow_sta()
    except ImportError:
        pass
    app = QApplication(sys.argv)
    start_window = IntroWindow()
    start_window.show()
    sys.exit(app.exec())
