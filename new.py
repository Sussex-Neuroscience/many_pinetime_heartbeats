"""
import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

asyncio.run(main())

"""
import asyncio
from bleak import BleakClient

address = "CB:F9:47:BD:83:F3"
#"F7:E6:68:B7:A4:71"
MODEL_NBR_UUID = "00002a37-0000-1000-8000-00805f9b34fb"#"InfiniTime"#"00002a24-0000-1000-8000-00805f9b34fb"

async def main(address):
    async with BleakClient(address) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        #print(model_number)
        for item in model_number:
            print(item)
            #print(item.decode())

        print("HT: {0}".format("".join(map(chr, model_number))))

asyncio.run(main(address))