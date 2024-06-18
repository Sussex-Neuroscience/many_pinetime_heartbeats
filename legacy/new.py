
MOTION_SERVICE_UUID = "00030000-78fc-48fe-8e23-433b3a1942d0"
STEP_COUNT_UUID = "00030001-78fc-48fe-8e23-433b3a1942d0"
RAW_XYZ_UUID = "00030002-78fc-48fe-8e23-433b3a1942d0"
HEART_RATE_UUID = "00002a37-0000-1000-8000-00805f9b34fb"
MODEL_NBR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"


"""
Created on Wed Jun  7 23:28:00 2023
Edited on Tue Jun 18 17:54:00 2024
@author: andre

Connects to a watch based on its address adds its data to a 1-D array based on buffer amount.
File is used to testing purposes to check that the software can communicate with the watch and back to the User.
@param Watch address
@return Nothing - outputs data back to user

Below is a condensed version of the code
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
import numpy as np

# Array contains 3 1-D arrays referencing 3 watches
address = [["CB:F9:47:BD:83:F3"],["DB:0C:6E:BF:5E"],["F7:E6:68:B7:A4:71"]]

async def main(address):
    for item in address:
        print(item)
        try:
            async with BleakClient(item) as client:
                
                #model_number = await client.read_gatt_char(MODEL_NBR_UUID)
                #print(model_number)
                heart_buffer = await client.read_gatt_char(HEART_RATE_UUID)
                
                step_buffer = await client.read_gatt_char(STEP_COUNT_UUID)      
                
                raw_buffer = await client.read_gatt_char(RAW_XYZ_UUID)
                
                raw_data =   np.frombuffer(raw_buffer, dtype=np.int16)
                step_data =  np.frombuffer(step_buffer, dtype=np.int16)
                heart_data = np.frombuffer(heart_buffer, dtype=np.int8)
                
                print("motion")
                print(raw_data)
                
                
                print("heart rate")
                #print(heart_rate)
                print(heart_data[1])
                
                print("step count")
                print(step_data[0])
                
                #return heart_data[1]
        except BleakDeviceNotFoundError:
            print(item + " device not found")
                #print(step_data[0]+heart_data[1])
                
                    #print(item.decode())

                #print("HT: {0}".format("".join(map(chr, model_number))))

heart_data = asyncio.run(main(address[0]))

#osc.send(/cue/heart_data)
#except:
#    print("timeout")