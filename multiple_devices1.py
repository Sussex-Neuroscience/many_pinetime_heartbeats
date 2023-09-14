import asyncio
from typing import Sequence
import numpy as np
from bleak import BleakClient, BleakScanner
from bleak.backends.device import BLEDevice
from qlabinterface import qlab_interface as pqosc
from pythonosc import osc_message_builder
from pythonosc import udp_client
import time
import sys


client1 = udp_client.UDPClient('169.254.175.189', 53000)
client2 = udp_client.UDPClient('localhost', 53000)
# oscClient = pqosc.Client()




MOTION_SERVICE_UUID = "00030000-78fc-48fe-8e23-433b3a1942d0"
STEP_COUNT_UUID = "00030001-78fc-48fe-8e23-433b3a1942d0"
RAW_XYZ_UUID = "00030002-78fc-48fe-8e23-433b3a1942d0"
HEART_RATE_UUID = "00002a37-0000-1000-8000-00805f9b34fb"
MODEL_NBR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"



#these need to correspond to the addresses of the watches being used at the exhibition:
if sys.platform == "darwin":
    addresses= ["D7E4D54E-3FD3-D125-6875-5826FC069A7F",
                "9E6B266F-95D9-C834-C162-73C0E7A93F68",
                "49CB51DD-CB82-ADC0-1D4A-C137E492AB9C",
                ]
#else:
#    addresses= ["CB:F9:47:BD:83:F3",
#                "DB:0C:6E:BF:B7:5E",
#                "F7:E6:68:B7:A4:71"]

"""
watch1: "D7E4D54E-3FD3-D125-6875-5826FC069A7F",
watch2: "9E6B266F-95D9-C834-C162-73C0E7A93F68",
watch3: "49CB51DD-CB82-ADC0-1D4A-C137E492AB9C",
watch4: "b581503d-513f-4371-d9b4-5db462438534",
watch5: "762e1be4-364b-5cbc-a146-05a1d725cb5f",
watch6: "72eef89d-257e-c281-308c-4192b9429e24",
watch7: "c2a6c545-b13d-a8de-ec5a-6f9332d14231",
watch8: "083aef46-b376-1c54-c12b-a9140db47513",
watch9: "527697fb-198a-6a02-4b6e-447876b4a41e"

"""

steps_multiplier=10
step_cues={"step_levels":list(range(15,0,-1)),
           "watch1":["/cue/*1a/go","/cue/*1b/go",
                     "/cue/*1c/go","/cue/*1d/go",
                     "/cue/*1e/go","/cue/*1f/go",
                     "/cue/*1g/go","/cue/*1h/go",
                     "/cue/*1i/go","/cue/*1j/go",
                     "/cue/*1k/go","/cue/*1l/go",
                     "/cue/*1m/go","/cue/*1n/go",
                     "/cue/*1o/go"
],
           "watch2":["/cue/*2a/go",
                     "/cue/*2b/go",
                     "/cue/*2c/go",
                     "/cue/*2d/go",
                     "/cue/*2e/go",
                     "/cue/*2f/go",
                     "/cue/*2g/go",
                     "/cue/*2h/go",
                     "/cue/*2i/go",
                     "/cue/*2j/go",
                     "/cue/*2k/go",
                     "/cue/*2l/go",
                     "/cue/*2m/go",
                     "/cue/*2n/go",
                     "/cue/*2o/go"],
           "watch3":[
               "/cue/*3a/go",
               "/cue/*3b/go",
               "/cue/*3c/go",
               "/cue/*3d/go",
               "/cue/*3e/go",
               "/cue/*3f/go",
               "/cue/*3g/go",
               "/cue/*3h/go",
               "/cue/*3i/go",
               "/cue/*3j/go",
               "/cue/*3k/go",
               "/cue/*3l/go",
               "/cue/*3m/go",
               "/cue/*3n/go",
               "/cue/*3o/go"
               ]
           
           }





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
    complete_duration = 12 #duration in min
    start = time.time()
    current_time=0
    #start the displaying the content
    msg1 = osc_message_builder.OscMessageBuilder(address="/cue/0/go")
    client1.send(msg1.build())
    client2.send(msg1.build())
#     oscClient.send_message("/cue/0/go")

    for i in range(45):                            
        while current_time-start<complete_duration*60:
            
            print("started QLAB")
            #print(current_time-start)
            short_run_duration=1 #time in minutes
            short_run_start=time.time()
            short_run_current_time=0
            max_number=2
            #while index<max_number:
            index = 0
            print("start short loop")
            while short_run_current_time-short_run_start<short_run_duration*60:
                
                #print("small_loop")
                #print(short_run_current_time-short_run_start)
                for d in devices:
                    
                    name = str(d.name)
    #                 print(name)
                    if name.lower()=="infinitime":
                        
                        async with BleakClient(d) as client:
                            #print(client.address.lower())
                            #heart_buffer = await client.read_gatt_char(HEART_RATE_UUID)
                            #step_buffer = await client.read_gatt_char(STEP_COUNT_UUID)      
                            #raw_buffer = await client.read_gatt_char(RAW_XYZ_UUID)
                            
                            #raw_data =   np.frombuffer(raw_buffer, dtype=np.int16)
                            #step_data =  np.frombuffer(step_buffer, dtype=np.int16)
                            #heart_data = np.frombuffer(heart_buffer, dtype=np.int8)

                            #here the use cases for each watch
                            #eg watch one uses heart rate to change parameter a, 
                            #watch two uses steps to change parameter b
                            
                            #watch1
                            if client.address.lower()==addresses[0].lower():
                                
                                
    #                             heart1_buffer = await client.read_gatt_char(HEART_RATE_UUID)
    #                             heart1_data = np.frombuffer(heart1_buffer, dtype=np.int8)
    #                             heart1_data = heart1_data[1]
                                
                                
                                step1_buffer = await client.read_gatt_char(STEP_COUNT_UUID)
                                step1_data = np.frombuffer(step1_buffer, dtype=np.int16)
                                #print(step_data)
                                step1_data = step1_data[0]
    #                             print(step1_data)
                                
                                #raw_buffer = await client.read_gatt_char(RAW_XYZ_UUID)
                            
                                #raw_data =   np.frombuffer(raw_buffer, dtype=np.int16)
                                #print("motion")
                                #print(raw_data)
                                
                                if index==0:
                                    print("red watch steps at start")
                                    print(step1_data)
                                    print(client.address.lower())
                                    step1_baseline=step1_data
    #                                 heart1_baseline=heart1_data
                                    old_cue=""
                                    
                                    
                                step1_difference = step1_data-step1_baseline
    #                             heart1_difference = heart1_data-heart1_baseline
                                print("red watch")
                                print("steps")
                                print(step1_difference)
                                cues=list(reversed(step_cues["watch1"]))
                                #index1=0
                                for index1,values in enumerate(step_cues["step_levels"]):
                                    
                                    if step1_difference>values*steps_multiplier:
                                        #print(index1)
                                        if old_cue!=cues[index1]:
                                            msg1 = osc_message_builder.OscMessageBuilder(address=cues[index1])
                                            client1.send(msg1.build())
                                            client2.send(msg1.build())
    #                                         oscClient.send_message(cues[index1])
                                            #print("cues")
                                            #print(old_cue)
                                            print(cues[index1])
                                            old_cue=cues[index1]
                                        break
                                    #index1=index1+1

                                
                             

    #                             if heart1_difference>=heart1_baseline*1.1 and heart1_difference<heart1_baseline*1.2:
    #                                 oscClient.send_message("/cue/*1/liveRate 1.2")
    #                             if heart1_difference>=heart1_baseline*1.2 and heart1_difference<heart1_baseline*1.3:
    #                                 oscClient.send_message("/cue/*1/liveRate 1.4")
    #                             if heart1_difference>=heart1_baseline*1.3 and heart1_difference<heart1_baseline*1.4:
    #                                 oscClient.send_message("/cue/*1/liveRate 2")


    # 
                            #watch2
                            if client.address.lower()==addresses[1].lower():
                                print("yellow watch") 
    #                             heart2_buffer = await client.read_gatt_char(HEART_RATE_UUID)
    #                             heart2_data = np.frombuffer(heart2_buffer, dtype=np.int8)
    #                             heart2_data = heart2_data[1]
                                
                                
                                step2_buffer = await client.read_gatt_char(STEP_COUNT_UUID)
                                step2_data = np.frombuffer(step2_buffer, dtype=np.int16)
                                #print(step_data)
                                step2_data = step2_data[0]
    #                             print(step1_data)
                                
                                #raw_buffer = await client.read_gatt_char(RAW_XYZ_UUID)
                            
                                #raw_data =   np.frombuffer(raw_buffer, dtype=np.int16)
                                #print("motion")
                                #print(raw_data)
                                
                                if index==0:
                                    print("yellow watch steps at start")
                                    print(step2_data)
                                    #print(client.address.lower())
                                    step2_baseline=step2_data
    #                                 heart2_baseline=heart2_data
                                    old_cue1=""
                                    
                                    
                                step2_difference = step2_data-step2_baseline
    #                             heart2_difference = heart2_data-heart2_baseline
                                print("steps")
                                print(step2_difference)
                                cues1=list(reversed(step_cues["watch2"]))
                                #index1=0
                                for index1,values in enumerate(step_cues["step_levels"]):
                                    
                                    if step2_difference>values*steps_multiplier:
                                        #print(index1)
                                        if old_cue1!=cues1[index1]:
                                            #oscClient.send_message(cues[index1])
                                            msg1 = osc_message_builder.OscMessageBuilder(address=cues1[index1])
                                            client1.send(msg1.build())
                                            client2.send(msg1.build())
                                            #print("cues")
                                            #print(old_cue)
                                            print(cues1[index1])
                                            old_cue1=cues1[index1]
                                        break
                                    #index1=index1+1

                                
                             

    #                             if heart2_difference>=heart2_baseline*1.1 and heart2_difference<heart2_baseline*1.2:
    #                                 oscClient.send_message("/cue/*1/liveRate 1.2")
    #                             if heart2_difference>=heart2_baseline*1.2 and heart2_difference<heart2_baseline*1.3:
    #                                 oscClient.send_message("/cue/*1/liveRate 1.4")
    #                             if heart2_difference>=heart2_baseline*1.3 and heart2_difference<heart2_baseline*1.4:
    #                                 oscClient.send_message("/cue/*1/liveRate 2")


    #                         
                            #watch3
                            if client.address.lower()==addresses[2].lower():
                                print("blue watch")
    #                             heart3_buffer = await client.read_gatt_char(HEART_RATE_UUID)
    #                             heart3_data = np.frombuffer(heart3_buffer, dtype=np.int8)
    #                             heart3_data = heart3_data[1]
                                
                                
                                step3_buffer = await client.read_gatt_char(STEP_COUNT_UUID)
                                step3_data = np.frombuffer(step3_buffer, dtype=np.int16)
                                #print(step_data)
                                step3_data = step3_data[0]

                                
                                if index==0:
                                    print("blue watch steps at start")
                                    print(step3_data)
                                    #print(client.address.lower())
                                    step3_baseline=step3_data
    #                                 heart3_baseline=heart3_data
                                    old_cue2=""
                                    
                                    
                                step3_difference = step3_data-step3_baseline
    #                             heart3_difference = heart3_data-heart3_baseline
                                print("steps")
                                print(step3_difference)
                                cues2=list(reversed(step_cues["watch3"]))
                                #index1=0
                                for index1,values in enumerate(step_cues["step_levels"]):
                                    
                                    if step3_difference>values*steps_multiplier:
                                        #print(index1)
                                        if old_cue2!=cues[index1]:
                                            msg1 = osc_message_builder.OscMessageBuilder(address=cues2[index1])
                                            client1.send(msg1.build())
                                            client2.send(msg1.build())
    #                                         oscClient.send_message(cues[index1])
                                            #print("cues")
                                            #print(old_cue)
                                            print(cues2[index1])
                                            old_cue2=cues2[index1]
                                        break
                                    #index1=index1+1

                                
                             

    #                             if heart3_difference>=heart3_baseline*1.1 and heart3_difference<heart3_baseline*1.2:
    #                                 oscClient.send_message("/cue/*1/liveRate 1.2")
    #                             if heart3_difference>=heart3_baseline*1.2 and heart3_difference<heart3_baseline*1.3:
    #                                 oscClient.send_message("/cue/*1/liveRate 1.4")
    #                             if heart3_difference>=heart3_baseline*1.3 and heart3_difference<heart3_baseline*1.4:
    #                                 oscClient.send_message("/cue/*1/liveRate 2")

                                    
                short_run_current_time=time.time()
                index=index+1#
            print("end small loop")
            current_time=time.time()


asyncio.run(find_all_devices_services())
