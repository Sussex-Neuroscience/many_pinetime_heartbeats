import asyncio
from typing import Sequence
import numpy as np
from bleak import BleakClient, BleakScanner
from bleak.backends.device import BLEDevice

MOTION_SERVICE_UUID = "00030000-78fc-48fe-8e23-433b3a1942d0"
STEP_COUNT_UUID = "00030001-78fc-48fe-8e23-433b3a1942d0"
RAW_XYZ_UUID = "00030002-78fc-48fe-8e23-433b3a1942d0"
HEART_RATE_UUID = "00002a37-0000-1000-8000-00805f9b34fb"
MODEL_NBR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"


async def find_all_devices_services():
    devices: Sequence[BLEDevice] = await BleakScanner.discover(timeout=5.0)
    #devices= [ "CB:F9:47:BD:83:F3",
    #           "DB:0C:6E:BF:5E",
    #           "F7:E6:68:B7:A4:71",]
    #devices: Sequence[BLEDevice] =  [
    #            "CB:F9:47:BD:83:F3",
    #            "DB:0C:6E:BF:5E",
    #            "F7:E6:68:B7:A4:71",
                #"B9EA5233-37EF-4DD6-87A8-2A875E821C46",
                #"F0CBEBD3-299B-4139-A9FC-44618C720157",

    #idx=0
    for d in devices:
        if d.name=="InfiniTime" or \
           d.name=="InfiniTimeF7E6" or\
           d.name=="InfiniTimeDB0C":
            #print(d.__dict__)
            async with BleakClient(d) as client:
                #print(client.services)
                heart_buffer = await client.read_gatt_char(HEART_RATE_UUID)
                
                step_buffer = await client.read_gatt_char(STEP_COUNT_UUID)      
                
                raw_buffer = await client.read_gatt_char(RAW_XYZ_UUID)
                
                raw_data =   np.frombuffer(raw_buffer, dtype=np.int16)
                step_data =  np.frombuffer(step_buffer, dtype=np.int16)
                heart_data = np.frombuffer(heart_buffer, dtype=np.int8)
                print(d.name)
                print("motion")
                print(raw_data)
                
                
                print("heart rate")
                #print(heart_rate)
                print(heart_data[1])
                
                print("step count")
                print(step_data[0])
 
            #idx=1
#         if d.address=="CB:F9:47:BD:83:F3" or \
#                        "DB:0C:6E:BF:5E" or \
#                        "F7:E6:68:B7:A4:71":
#             #print("here")
#             async with BleakClient(d) as client:
#                 print(client.services)


asyncio.run(find_all_devices_services())