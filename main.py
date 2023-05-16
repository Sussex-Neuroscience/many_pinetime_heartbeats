"""
Use bleak library to find devices available, connect to them and do periodic requests on their heart rate data
"""

import asyncio
from bleak import BleakScanner
from bleak import BleakClient


async def scan():
    pineTimes = []
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)
        if d == "pine":
            pineTimes.append(d)








