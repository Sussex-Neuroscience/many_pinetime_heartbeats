"""
Created on Wed Jun  7 23:28:00 2023
Edited on Tue Jun 18 17:21:00 2024
@author: andre

This code is to allow multiple pinetime watches to connect to the software.
Allows multiple sets of data to be collected at a time.

@param: Takes devices addresses as input
@return: Not 100% what it gives back
"""
import asyncio

from bleak import BleakClient
 
MOTION_SERVICE_UUID = "00030000-78fc-48fe-8e23-433b3a1942d0"
STEP_COUNT_UUID = "00030001-78fc-48fe-8e23-433b3a1942d0"
RAW_XYZ_UUID = "00030002-78fc-48fe-8e23-433b3a1942d0"
HEART_RATE_UUID = "00002a37-0000-1000-8000-00805f9b34fb"
MODEL_NBR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"


notify_uuid = STEP_COUNT_UUID

#temperatureUUID = "45366e80-cf3a-11e1-9ab4-0002a5d5c51b"
#ecgUUID = "46366e80-cf3a-11e1-9ab4-0002a5d5c51b"

#notify_uuid = "0000{0:x}-0000-1000-8000-00805f9b34fb".format(0xFFE1)


def callback(characteristic, data):
    print(characteristic, data)


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



def main(addresses):
    return asyncio.gather(*(connect_to_device(address) for address in addresses))


if __name__ == "__main__":
    asyncio.run(
        main(
            [
                "CB:F9:47:BD:83:F3",
                "DB:0C:6E:BF:5E",
                "F7:E6:68:B7:A4:71",
                #"B9EA5233-37EF-4DD6-87A8-2A875E821C46",
                #"F0CBEBD3-299B-4139-A9FC-44618C720157",
            ]
        )
    )