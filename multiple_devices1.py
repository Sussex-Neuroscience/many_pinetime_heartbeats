import asyncio
from typing import Sequence

from bleak import BleakClient, BleakScanner
from bleak.backends.device import BLEDevice


async def find_all_devices_services():
    #devices: Sequence[BLEDevice] = await BleakScanner.discover(timeout=5.0)
    devices: Sequence[BLEDevice] =  [
                "CB:F9:47:BD:83:F3",
                "DB:0C:6E:BF:5E",
                "F7:E6:68:B7:A4:71",
                #"B9EA5233-37EF-4DD6-87A8-2A875E821C46",
                #"F0CBEBD3-299B-4139-A9FC-44618C720157",
            ]
    for d in devices:
        async with BleakClient(d) as client:
            print(client.services)


asyncio.run(find_all_devices_services())