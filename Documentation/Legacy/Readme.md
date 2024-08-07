# Breakdowns of the files in Legacy and their libraries

## Context
### What is the Legacy Folder?
The point of this folder is that it contains multiple scripting to assist with connecting pinetime watches to the other series of scripts that is the many_pinetime_heartbeats project. 

### External Libraries
#### Numpy
[Numpy Documentation](https://numpy.org/doc/1.26/)<br>
#### bleak - Bluetooth Low Energy platform Agnostic Klient
[bleak Documentation](https://bleak.readthedocs.io/en/latest/index.html)<br>
### Internal functions and modules
#### asyncio
[asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
#### typing
[typing Documentation](https://docs.python.org/3/library/typing.html)<br>
[typing Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
### Errors in this folder
* bleak
  * bleak library is "randomly" disconnecting
  * There are two possibilities I can think of for this error
    * One of the files which handles connection to the watches has a logic error
    * The library is behaving in a way we weren't expecting
  * Two solutions to above
    * Implementing try and catch statement to understand the logic error
    * Look through library documentation/potentially talk to library developer and ask them for a technical explanation

## Files
### Main

### Many devices

### Multiple devices
The purpose of this file is to:
* Connect to a watch based on address given as input
  * If cannot connect to device output error to user
  * Else 
### new
The purpose of this file is to:
* Connect to a watch based on a address given to it
* Wait for the watch to generate data such as
  * Heartrate
  * Step count
  * Raw data (Not 100% what this entails)
* Output the data it has collected back to the user
* Or if the device address does not link to a devices gives a device not found error back to the User
Used to check that the software can communicate with the watch and ot the user.


Attempt 2:
# Legacy Folder Documentation
## 1. Introduction
### What is the Legacy Folder?
The Legacy Folder contains a collection of scripts to facilitate the connection between Pinetime watches and other scripts within the **many_pinetime_heartbeats** project. These scripts primarily handle communication protocols, data retrieval, and error management associated with connecting multiple devices.<br>


## 2. External Libraries
### Numpy
* **Purpose**: Numpy is utilized for numerical operations and data manipulation within scripts.
* **Documentation**: [Numpy Documentation](https://numpy.org/doc/1.26/)<br>
### bleak - Bluetooth Low Energy platform Agnostic Klient
* **Purpose**: Bleak handles Bluetooth Low Energy (BLE) connections across different platforms.
* **Documentation**: [bleak Documentation](https://bleak.readthedocs.io/en/latest/index.html)<br>


## 3. Internal Functions and Modules 
### asyncio
* **Purpose**: Asyncio is used for writing concurrent code, allowing the scripts to manage multiple connections and tasks asynchronously.
* **Documentation**: [asyncio Documentation](https://docs.python.org/3/library/asyncio.html)<br>
### typing
* **Purpose**: The typing module provides type hints to improve code readability and maintainability.
* **Documentation**: [typing Documentation](https://docs.python.org/3/library/typing.html)
* **Overview Sheet**: [typing Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)<br>

## 4. Common Errors in Legacy Folder
  ### 1. 

## 5. File Breakdown
### [New](https://github.com/KeaganKozlowski/many_pinetime_heartbeats/blob/main/legacy/new.py)
* **Purpose**: The script connects to a Pinetime watch, retrieves specific data such as heart rate, step count, and raw motion data, and outputs to this data to the user. The file is primarily used for testing purposes to verify that the software can successfully communicate with the watch and return the collected data.
* **Functionality**: 
  * **Connections to Watches**: The script connects to multiple Pinetime watches based on their Bluetooth addresses. These addresses are stored in a list, with each address representing a different watch.
  * **Reading Data**: Once connected, the script reads data from three specific Bluetooth GATT characteristics.
    * **Heart Rate**: Uses the HEART_RATE_UUID to read the current heart rate.
    * **Step Count**: Uses the STEP_COUNT_UUID to retrieve the step count.
    * **Raw Motion Data**: Uses the RAW_XYZ_UUID to obtain raw motion data from the watch’s accelerometer.
  * **Data Processing**:The retrieved data is converted from its raw byte format into a more usable form using Numpy:
    * **Heart Rate Data** is interpreted as an 8-bit integer array.
    * **Step Count Data** and **Raw Motion Data** are interpreted as 16-bit integer arrays.
  * **Error Handling**: The script includes error handling to catch instances where a device is not found. If the connection fails, an error message is output to the user indicating which device could not be connected.
  * **Output**: The script prints the heart rate, step count, and raw motion data to the console. This output helps verify that the data is being correctly retrieved and processed.
* **Usage**:
  * The script ensures that the software can communicate with Pinetime watches and correctly retrieve the required data. It is useful for debugging and verifying that the connection logic and data processing are functioning as expected.<br>
### [Multiple devices](https://github.com/KeaganKozlowski/many_pinetime_heartbeats/blob/main/legacy/multiple_devices.py)
* **Purpose**: The script allows multiple Pinetime watches to connect to the software simultaneously, enabling the collection of data from several devices at once. This script is crucial for scenarios where data needs to be gathered concurrently from multiple sources.
* **Functionality**:
  * **Connecting to Multiple Devices**: The script attempts to connect to a list of Pinetime watches, each identified by its Bluetooth address. The addresses are provided as input, and the script runs asynchronously to manage multiple connections at the same time.
  * **Notifications and Data Handling**:
    * Once connected, the script starts listening for notifications on a specified GATT characteristic (in this case, the step count, identified by STEP_COUNT_UUID).
    * A callback function is defined (callback) that is triggered whenever new data is received from the connected watch. The function prints out the characteristics and the received data.
  * **Error Handling**:
    * If the connection to a device fails or an error occurs during the notification process, the script catches and prints the exception. This is important for debugging issues with specific devices or connectivity.
  * **Asynchronous Execution**:
    * The main() function uses asyncio.gather() to run the connection process for all devices concurrently. This allows the script to handle multiple connections in parallel, improving efficiency and ensuring that all devices are managed simultaneously.
* **Usage**:
  * The script is ideal for testing and development scenarios where multiple Pinetime watches need to be connected and monitored at the same time. It allows developers to observe how multiple devices behave and ensure that the software can handle concurrent connections and data streams effectively.
### [Many devices](https://github.com/KeaganKozlowski/many_pinetime_heartbeats/blob/main/legacy/many_devices.py)
### [Main](https://github.com/KeaganKozlowski/many_pinetime_heartbeats/blob/main/legacy/main.py)



