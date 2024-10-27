#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 23:28:00 2023
Edited on Tue Jun 18 18:08:00 2024
@author: andre
Program is used to search for devices on a network/geographical location.
If it finds a device attempt to communicate with it, after 5 seconds move onto next device.
@param: Does not take any input
@return: Nothing - Outputs services of each device it can communicate with
"""

import asyncio
from typing import Sequence

from bleak import BleakClient, BleakScanner
from bleak.backends.device import BLEDevice


async def find_all_devices_services():
    scanner = BleakScanner()
    devices: Sequence[BLEDevice] = scanner.discover(timeout=5.0)
    for d in devices:
        async with BleakClient(d) as client:
            print(client.services)


asyncio.run(find_all_devices_services())
