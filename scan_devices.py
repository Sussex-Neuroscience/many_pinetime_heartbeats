import asyncio
from typing import Sequence
from bleak import BleakClient, BleakScanner
from bleak.backends.device import BLEDevice
from qlabinterface import qlab_interface as pqosc
import time
import sys

oscClient = pqosc.Client()


MOTION_SERVICE_UUID = "00030000-78fc-48fe-8e23-433b3a1942d0"
STEP_COUNT_UUID = "00030001-78fc-48fe-8e23-433b3a1942d0"
RAW_XYZ_UUID = "00030002-78fc-48fe-8e23-433b3a1942d0"
HEART_RATE_UUID = "00002a37-0000-1000-8000-00805f9b34fb"
MODEL_NBR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"



#these need to correspond to the addresses of the watches being used at the exhibition:
if sys.platform == "darwin":
    addresses= ["CB:F9:47:BD:83:F3","DB:0C:6E:BF:B7:5E","F7:E6:68:B7:A4:71"]
else:
    addresses= ["CB:F9:47:BD:83:F3","DB:0C:6E:BF:B7:5E","F7:E6:68:B7:A4:71"]




current_time = 0

async def find_all_devices_services():
    devices: Sequence[BLEDevice] = await BleakScanner.discover(timeout=5.0)
    print(devices)
    for d in devices:
        name = str(d.name)
    return d