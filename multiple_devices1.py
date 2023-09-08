import asyncio
from typing import Sequence
import numpy as np
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

step_levels=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


step_cues={"watch1":["/cue/*1a/go",
"/cue/*1b/go",
"/cue/*1c/go",
"/cue/*1d/go",
"/cue/*1e/go",
"/cue/*1f/go",
"/cue/*1g/go",
"/cue/*1h/go",
"/cue/*1i/go",
"/cue/*1j/go",
"/cue/*1k/go",
"/cue/*1l/go",
"/cue/*1m/go",
"/cue/*1n/go",
"/cue/*1o/go"
]
           
           }



step_level1 = 10
step_level2 = 20
step_level3 = 30
step_level4 = 40
step_level5 = 50
step_level6 = 60

def steps_calculation(step_data=0,step_baseline=0, index=0):
    if index == 0:
        step_baseline = step_data
        step_difference = 0
    else:
        step_difference = step_data-step_baseline
        #step_baseline = step_data
    return step_baseline,step_difference


current_time = 0

async def find_all_devices_services():
    devices: Sequence[BLEDevice] = await BleakScanner.discover(timeout=5.0)
    #print(devices)


    #idx=0
    #test = list()
    complete_duration = 15 #duration in min
    start = time.time()
    current_time=0
    #start the displaying the content
    oscClient.send_message("/cue/0/go")
                                
    while current_time-start<complete_duration*60:
        
        #print("big loop")
        #print(current_time-start)
        short_run_duration=1 #time in minutes
        short_run_start=time.time()
        short_run_current_time=0
        max_number=2
        #while index<max_number:
        index = 0
        while short_run_current_time-short_run_start<short_run_duration*60:
            #print("small_loop")
            #print(short_run_current_time-short_run_start)
            for d in devices:
                
                name = str(d.name)
                print(name)
                if name.lower()=="infinitime":
                    print(d)
                    async with BleakClient(d) as client:
                        
                        #heart_buffer = await client.read_gatt_char(HEART_RATE_UUID)
                        #step_buffer = await client.read_gatt_char(STEP_COUNT_UUID)      
                        raw_buffer = await client.read_gatt_char(RAW_XYZ_UUID)
                        
                        raw_data =   np.frombuffer(raw_buffer, dtype=np.int16)
                        #step_data =  np.frombuffer(step_buffer, dtype=np.int16)
                        #heart_data = np.frombuffer(heart_buffer, dtype=np.int8)

                        #here the use cases for each watch
                        #eg watch one uses heart rate to change parameter a, 
                        #watch two uses steps to change parameter b
                        
                        #watch1
                        if client.address.lower()==addresses[0].lower():
                            
                            
                            heart1_buffer = await client.read_gatt_char(HEART_RATE_UUID)
                            heart1_data = np.frombuffer(heart1_buffer, dtype=np.int8)
                            heart1_data = heart1_data[1]
                            
                            
                            step1_buffer = await client.read_gatt_char(STEP_COUNT_UUID)
                            step1_data = np.frombuffer(step1_buffer, dtype=np.int16)
                            #print(step_data)
                            step1_data = step1_data[0]
                            print(step1_data)
                            
                            #raw_buffer = await client.read_gatt_char(RAW_XYZ_UUID)
                        
                            #raw_data =   np.frombuffer(raw_buffer, dtype=np.int16)
                            #print("motion")
                            #print(raw_data)
                            
                            if index==0:
                                step1_baseline=step1_data
                                heart1_baseline=heart1_data
                                
                                
                            step1_difference = step1_data-step1_baseline
                            heart1_difference = heart1_data-heart1_baseline

                            
                            if step1_difference>=step_level1 and step1_difference<step_level2:
                                oscClient.send_message("/cue/*1a/go")
                            if step1_difference>=step_level2 and step1_difference<step_level3:
                                oscClient.send_message("/cue/*1/opacity 0.5")
                            if step1_difference>=step_level3 and step1_difference<step_level4:
                                oscClient.send_message("/cue/*1/opacity 0.8")
                            if step1_difference>=step_level4 and step1_difference<step_level5:
                                oscClient.send_message("/cue/*1/liveScale 1.1 1.1") 
                            if step1_difference>=step_level5 and step1_difference<step_level6:
                                oscClient.send_message("/cue/*1/liveScale 1.2 1.2")
                            if step1_difference>=step_level6 and step1_difference<step_level6+10:
                                oscClient.send_message("/cue/*1/liveScale 1.5 1.5")


                            if heart1_difference>=heart1_baseline*1.1 and heart1_difference<heart1_baseline*1.2:
                                oscClient.send_message("/cue/*1/liveRate 1.2")
                            if heart1_difference>=heart1_baseline*1.2 and heart1_difference<heart1_baseline*1.3:
                                oscClient.send_message("/cue/*1/liveRate 1.4")
                            if heart1_difference>=heart1_baseline*1.3 and heart1_difference<heart1_baseline*1.4:
                                oscClient.send_message("/cue/*1/liveRate 2")



                        #watch2
                        if client.address.lower()==addresses[1].lower():
                            heart2_buffer = await client.read_gatt_char(HEART_RATE_UUID)
                            heart2_data = np.frombuffer(heart2_buffer, dtype=np.int8)
                            heart2_data = heart2_data[1]
                            
                            
                            step2_buffer = await client.read_gatt_char(STEP_COUNT_UUID)
                            step2_data = np.frombuffer(step2_buffer, dtype=np.int16)
                            #print(step_data)
                            step2_data = step2_data[0]
                            print(step2_data)
                            
                            #raw_buffer = await client.read_gatt_char(RAW_XYZ_UUID)
                        
                            #raw_data =   np.frombuffer(raw_buffer, dtype=np.int16)
                            #print("motion")
                            #print(raw_data)
                            
                            if index==0:
                                step2_baseline=step2_data
                                heart2_baseline=heart2_data
                                
                                
                            step2_difference = step2_data-step2_baseline
                            heart2_difference = heart2_data-heart2_baseline

                            
                            if step2_difference>=step_level1 and step2_difference<step_level2:
                                oscClient.send_message("/cue/*1a/go")
                            if step2_difference>=step_level2 and step2_difference<step_level3:
                                oscClient.send_message("/cue/*1/opacity 0.5")
                            if step2_difference>=step_level3 and step2_difference<step_level4:
                                oscClient.send_message("/cue/*1/opacity 0.8")
                            if step2_difference>=step_level4 and step2_difference<step_level5:
                                oscClient.send_message("/cue/*1/liveScale 1.1 1.1") 
                            if step2_difference>=step_level5 and step2_difference<step_level6:
                                oscClient.send_message("/cue/*1/liveScale 1.2 1.2")
                            if step2_difference>=step_level6 and step2_difference<step_level6+10:
                                oscClient.send_message("/cue/*1/liveScale 1.5 1.5")


                            if heart2_difference>=heart2_baseline*1.1 and heart2_difference<heart2_baseline*1.2:
                                oscClient.send_message("/cue/*1/liveRate 1.2")
                            if heart2_difference>=heart2_baseline*1.2 and heart2_difference<heart2_baseline*1.3:
                                oscClient.send_message("/cue/*1/liveRate 1.4")
                            if heart2_difference>=heart2_baseline*1.3 and heart2_difference<heart2_baseline*1.4:
                                oscClient.send_message("/cue/*1/liveRate 2")
                        
                        #watch3
                        if client.address.lower()==addresses[2].lower():
                            #print("watch3")
                            #print(client.address)
                            heart3_buffer = await client.read_gatt_char(HEART_RATE_UUID)
                            heart3_data = np.frombuffer(heart3_buffer, dtype=np.int8)
                            heart3_data = heart3_data[1]
                            
                            
                            step3_buffer = await client.read_gatt_char(STEP_COUNT_UUID)
                            step3_data = np.frombuffer(step3_buffer, dtype=np.int16)
                            #print(step_data)
                            step3_data = step3_data[0]
                            print(step3_data)
                            
                            #raw_buffer = await client.read_gatt_char(RAW_XYZ_UUID)
                        
                            #raw_data =   np.frombuffer(raw_buffer, dtype=np.int16)
                            #print("motion")
                            #print(raw_data)
                            
                            if index==0:
                                step3_baseline=step3_data
                                heart3_baseline=heart3_data
                                
                                
                            step3_difference = step3_data-step3_baseline
                            heart3_difference = heart3_data-heart3_baseline

                            
                            if step3_difference>=step_level1 and step3_difference<step_level2:
                                oscClient.send_message("/cue/*1a/go")
                            if step3_difference>=step_level2 and step3_difference<step_level3:
                                oscClient.send_message("/cue/*1/opacity 0.5")
                            if step3_difference>=step_level3 and step3_difference<step_level4:
                                oscClient.send_message("/cue/*1/opacity 0.8")
                            if step3_difference>=step_level4 and step3_difference<step_level5:
                                oscClient.send_message("/cue/*1/liveScale 1.1 1.1") 
                            if step3_difference>=step_level5 and step3_difference<step_level6:
                                oscClient.send_message("/cue/*1/liveScale 1.2 1.2")
                            if step3_difference>=step_level6 and step3_difference<step_level6+10:
                                oscClient.send_message("/cue/*1/liveScale 1.5 1.5")


                            if heart3_difference>=heart3_baseline*1.1 and heart3_difference<heart3_baseline*1.2:
                                oscClient.send_message("/cue/*1/liveRate 1.2")
                            if heart3_difference>=heart3_baseline*1.2 and heart3_difference<heart3_baseline*1.3:
                                oscClient.send_message("/cue/*1/liveRate 1.4")
                            if heart3_difference>=heart3_baseline*1.3 and heart3_difference<heart3_baseline*1.4:
                                oscClient.send_message("/cue/*1/liveRate 2")
                                
            short_run_current_time=time.time()
            index=index+1#
        current_time=time.time()


asyncio.run(find_all_devices_services())



"""

For watch 1 (red):
Step count -
/cue/*1a/go
/cue/*1b/go
/cue/*1c/go
/cue/*1d/go
/cue/*1e/go
/cue/*1f/go
/cue/*1g/go
/cue/*1h/go
/cue/*1i/go
/cue/*1j/go
/cue/*1k/go
/cue/*1l/go
/cue/*1m/go
/cue/*1n/go
/cue/*1o/go
Heart rate -
For an increase in heart rate -
/cue/*4inc/go
For a decrease in heart rate -
/cue/*4dec/go
For watch 2 (yellow):
Step count -
/cue/*2a/go
/cue/*2b/go
/cue/*2c/go
/cue/*2d/go
/cue/*2e/go
/cue/*2f/go
/cue/*2g/go
/cue/*2h/go
/cue/*2i/go
/cue/*2j/go
/cue/*2k/go
/cue/*2l/go
/cue/*2m/go
/cue/*2n/go
/cue/*2o/go
Heart rate -
For an increase in heart rate -
/cue/*5inc/go
For a decrease in heart rate -
/cue/*5dec/go
For watch 3 (blue):
Step count -
/cue/*3a/go
/cue/*3b/go
/cue/*3c/go
/cue/*3d/go
/cue/*3e/go
/cue/*3f/go
/cue/*3g/go
/cue/*3h/go
/cue/*3i/go
/cue/*3j/go
/cue/*3k/go
/cue/*3l/go
/cue/*3m/go
/cue/*3n/go
/cue/*3o/go
Heart rate -
For an increase in heart rate -
/cue/*6inc/go
For a decrease in heart rate -
/cue/*6dec/go







"""

