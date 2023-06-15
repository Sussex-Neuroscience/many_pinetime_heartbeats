"""
Use bleak library to find devices available, connect to them and do periodic requests on their heart rate data
"""
import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

asyncio.run(main())







