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

## 4. Error Handling
  ### 1. bleak library randomly disconnects
  * **Issue**: The bleak library disconnects from devices without a clear pattern
  * **Possible Causes**:
    * There might be a logic error in one of the scripts responsible for managing the connection to the watches.
    * The bleak library could be exhibiting behaviour that we did not anticipate.
  * **Potential Solutions**:
    * Implement try and catch statements around connection logic to better understand where the error occurs.
    * Review the bleak documentation for any known issues or contact the library maintainers for a deeper technical explanation.
  * **Actual Solution**:
    * Whilst testing the scripts on a MacOS Device the user disabled their WI-FI which in turn disabled their BLUETOOTH connection which led to the connection between the computer and watches being severed.
    * To prevent this issue occurring whilst attempting to connect to the watch and or transferring data between the watches and your devices, please do not disable the WI-FI or BLUETOOTH.

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
  * The script is ideal for testing and development scenarios where multiple Pinetime watches need to be connected and monitored at the same time. It allows developers to observe how multiple devices behave and ensure that the software can handle concurrent connections and data streams effectively.<br>
### [Many devices](https://github.com/KeaganKozlowski/many_pinetime_heartbeats/blob/main/legacy/many_devices.py)
* **Purpose**: The script  is designed to scan for Bluetooth Low Energy (BLE) devices in the vicinity, attempt to connect to each discovered device, and then output the available GATT services provided by each device. This script is useful for identifying and communicating with multiple BLE devices within a specific geographic area or network.
* **Functionality**:
  * **Device Discovery**: 
    * The script uses the BleakScanner to scan for BLE devices. It performs a scan for 5 seconds (timeout=5.0) to discover any nearby BLE devices.
  * **Service Discovery**:
    * Once devices are discovered, the script attempts to connect to each one using BleakClient. If the connection is successful, it retrieves and prints the list of GATT services provided by the device. GATT services define how data is structured and exchanged, making this step crucial for understanding the device's capabilities.
  * **Asynchronous Execution**:
    * The script runs asynchronously using asyncio, which allows it to efficiently manage the scanning and connecting processes without blocking the main execution thread. This is particularly important when dealing with multiple devices, as it enables the script to move on to the next device after 5 seconds, even if a connection attempt is ongoing or fails.
  * **No Input or Output Parameters**:
    * The script does not take any inputs and does not return any outputs. Instead, it directly prints the available services of each device it successfully connects to. This output is typically used for diagnostic or setup purposes, helping users identify the available devices and their capabilities.
* **Usage**:
  * The script is primarily used for scanning and identifying BLE devices within a certain area. It’s useful in situations where you need to know what devices are nearby and what services they offer, such as in the initial setup of a network of BLE devices or when troubleshooting connectivity issues.<br>
### [Main](https://github.com/KeaganKozlowski/many_pinetime_heartbeats/blob/main/legacy/main.py)
* **Purpose**: The script is designed to use the Bleak library to scan for nearby Bluetooth Low Energy (BLE) devices and print out a list of the devices it finds. This script is primarily used for identifying BLE devices within range, which is often the first step before connecting to and interacting with these devices for further data retrieval.
* **Functionality**:
  * **Device Discovery**:
    * The script uses BleakScanner.discover() to initiate a scan for nearby BLE devices. This function asynchronously scans for devices and returns a list of discovered devices.
  * **Printing Discovered Devices**:
    * Once the devices are discovered, the script iterates over the list of devices and prints each one. The printed output typically includes details such as the device name, address, and other relevant metadata.
  * **Asynchronous Execution**:
    * The script is designed to run asynchronously using the asyncio framework. This ensures that the scanning process is non-blocking, allowing other tasks to run concurrently if needed. The asyncio.run(main()) call is used to execute the asynchronous main() function.
  * **No Input or Output Parameters**:
    * The script does not take any input parameters nor does it return any outputs. It simply performs the device discovery and outputs the results directly to the console.
* **Usage**:
  * The main.py script is useful for quickly identifying what BLE devices are within range. This is typically the first step in any Bluetooth-related project, allowing developers to confirm that their devices are discoverable and accessible before attempting more complex interactions, such as connecting to the devices or retrieving specific data.<br>




