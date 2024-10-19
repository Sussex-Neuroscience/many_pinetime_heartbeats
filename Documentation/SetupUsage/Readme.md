# Setup and Usage Guide
This project involves utilizing PineTime watches worn by visitors to an art installation. The watches will transmit data such as heart rate, acceleration (XYZ), and step count to a computer. This collected information will then be dynamically used to influence and control the audiovisual elements of the installation, such as projections, creating a unique and interactive experience for visitors.

## Table of Contents
1. [Installation]()
2. [Setup]()
3. [Usage]()
4. [Libraries Used]()
4. [Contributing]()
5. [Reports]()
6. [License]()

<br>

### Installation
#### Prerequisties
Before you begin ensure you have the following installed on your machine:
* Python 3.11 (Check your Python version using)
  * This is the most up-to-date Python version ensuring that all libraries and features work correctly.
```shell
python3 --version
```
#### Clone the repository
To get started clone the repository from GitHub:
```shell
git clone https://github.com/KeaganKozlowski/many_pinetime_heartbeats
cd many_pinetime_heartbeats
```
#### Install dependencies
This project uses several Python libraries including Flet, Asyncio, Threading, NumPy, Bleak and Bleak.exc (extension of Bleak).
##### Option 1: Using requirements.txt
```shell
pip install -r requirements.txt
```
##### Option 2: Manual Installation
Alternatively you can manually install the required libraries using pip:
```shell
pip install flet numpy bleak
```
Note: Threading and Asyncio are part of Python's standard library, so they don't need to be installed seperately.

<br>

### Setup
Once dependencies are installed, follow the steps below to set up the project:

<br>

### Usage
Now that setup is complete , here's how to run the app. The app can be run locally or as a web app however both require to be run through the terminal.
#### Option 1: Ran locally
1. Open your terminal and run the following command:
```shell
cd Flet
Flet run
```
This will open the app on your computer which will be fully interactable
#### Option 2: Ran on the web
1. Open your terminal and run the following command:
```shell
cd Flet
Flet run --web
```
This will open the app on your default web browser however it be still be hosted locally on your machine which will mean the URL cannot be shared.

<br>

### Libraries Used
1. #### **Flet**
[Flet](https://flet.dev/) is a Python framework for building web, desktop, and mobile apps. It's used here to create the Graphical User Interface (GUI) for the app.
2. #### **Asyncio**
[Asyncio](https://docs.python.org/3/library/asyncio.html) is a library used to write concurrent code in Python. It's utilized for handling asynchronous tasks like I/O-bound functions and networking.
3. #### **Threading**
[Threading](https://docs.python.org/3/library/threading.html) is used for executing multiple threads (lighter than processes) in parallel, enabling background tasks without blocking the main program.
4. #### **NumPy**
[NumPy](https://numpy.org/) is a powerful numerical computing library in Python. It is used for mathematical operations, array multiplications, or any complex number-crunching tasks.
5. #### **Bleak**
[Bleak](https://github.com/hbldh/bleak) is a Python library for Bluetooth Low Energy (BLE) communications. It is used to interact with BLE devices.
```arduino
- `bleak.exc`: This module contains custom exceptions for handling BLE errors during the communication process.
```

<br>

### Contributing
Contributions are welcome!<br>
If you would like to contribute, please fork the repository and submit a pull request. For significant changes, open an issue first to discuss what you would like to change.

<br>

### Reports
If you find an error or discover a bug/exploit with the program open an issue and describe what you occurred, how you occurred it and any steps that can be taken to replicate it.

<br>

### License
This project is licensed under the GNU General Public License - see [LICENSE](https://github.com/Sussex-Neuroscience/many_pinetime_heartbeats/blob/main/LICENSE) file for details.