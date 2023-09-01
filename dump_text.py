                     # heart_buffer = await client.read_gatt_char(HEART_RATE_UUID)
                        # heart_data = np.frombuffer(heart_buffer, dtype=np.int8)
                        # #print("heart1 "+str(heart_data[1]))
                        # if index==0:
                        #     baseHeart1 = heart_data
                        
                        
                        
                                            # #print(d.name)
                    # print("motion")
                    # print(raw_data)
                    
                    
                    # print("heart rate")
                    # #print(heart_rate)
                    # print(heart_data[1])
                    
                    # print("step count")
                    # print(step_data[0])


            #idx=1
#         if d.address=="CB:F9:47:BD:83:F3" or \
#                        "DB:0C:6E:BF:5E" or \
#                        "F7:E6:68:B7:A4:71":
#             #print("here")
#             async with BleakClient(d) as client:
#                 print(client.services)


"""
                    Watch 1:
#Step count. First trigger to operate?
#At 10 steps - opacity 20%. /cue/*1/opacity 0.2
#20 - 50%. /cue/*1/opacity 0.5
#30 - 80%. /cue/*1/opacity 0.8
#40 steps - scale increase by 10%. /cue/*1/liveScale 1.1 1.1
#50 - 20%.  /cue/*1/liveScale 1.2 1.2
#60 - 50%.  /cue/*1/liveScale 1.5 1.5
XYZ
At X, Y shift by 10%, translate cue X by 50 pixels, cue Y by 100 pixels. /cue/*1/liveTranslation 50 100
At X, Y shift by 20%, translate cue X by 100 pixels, cue Y by 200 pixels. /cue/*1/liveTranslation 100 200
At X, Y shift by 30%, translate cue X by 100 pixels, cue Y by 200 pixels. /cue/*1/liveTranslation 150 300
Etc.
#Heart Rate.
#At 10% increase, rate increases by 0.2. /cue/*1/liveRate 1.2
#At 20% increase, rate increase by 0.4.  /cue/*1/liveRate 1.4
#At 30% increase, rate increase by 1.  /cue/*1/liveRate 2

Watch 2:
Step count. First trigger to operate?
At 10 steps - opacity 20%. /cue/*2/opacity 0.2
20 - 50%. /cue/*2/opacity 0.5
30 - 80%. /cue/*2/opacity 0.8
40 steps - scale increase by 10%. /cue/*2/liveScale 1.1 1.1
50 - 20%.  /cue/*2/liveScale 1.2 1.2
60 - 50%.  /cue/*2/liveScale 1.5 1.5
XYZ
At X, Y shift by 10%, translate cue X by 50 pixels, cue Y by 100 pixels. /cue/*2/liveTranslation 50 100
At X, Y shift by 20%, translate cue X by 100 pixels, cue Y by 200 pixels. /cue/*2/liveTranslation 100 200
At X, Y shift by 30%, translate cue X by 100 pixels, cue Y by 200 pixels. /cue/*2/liveTranslation 150 300
Etc.
Heart Rate.
At 10% increase, rate increases by 0.2. /cue/*2/liveRate 1.2
At 20% increase, rate increase by 0.4.  /cue/*2/liveRate 1.4
At 30% increase, rate increase by 1.  /cue/*2/liveRate 2

Watch 3:
Step count. First trigger to operate?
At 10 steps - opacity 20%. /cue/*3/opacity 0.2
20 - 50%. /cue/*3/opacity 0.5
30 - 80%. /cue/*3/opacity 0.8
40 steps - scale increase by 10%. /cue/*3/liveScale 1.1 1.1
50 - 20%.  /cue/*3/liveScale 1.2 1.2
60 - 50%.  /cue/*3/liveScale 1.5 1.5
XYZ
At X, Y shift by 10%, translate cue X by 50 pixels, cue Y by 100 pixels. /cue/*3/liveTranslation 50 100
At X, Y shift by 20%, translate cue X by 100 pixels, cue Y by 200 pixels. /cue/*3/liveTranslation 100 200
At X, Y shift by 30%, translate cue X by 100 pixels, cue Y by 200 pixels. /cue/*3/liveTranslation 150 300
Etc.
Heart Rate.
At 10% increase, rate increases by 0.2. /cue/*3/liveRate 1.2
At 20% increase, rate increase by 0.4.  /cue/*3/liveRate 1.4
At 30% increase, rate increase by 1.  /cue/*3/liveRate 2
                    
"""
