#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 23:28:00 2023

@author: andre
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
