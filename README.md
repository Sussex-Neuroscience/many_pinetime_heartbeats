# many_pinetime_heartbeats
 code to connect many pineTimes to a computer and extract heart rates
 
 This project is initially to support an art installation where PineTime watches 
 being used by visitors will send information (Heart rate, xyz, step count) to a computer and this will be used to 
 control what is being shown to visitors (audio visual projections, etc).
 
 The best way to do this so far was:
 - PineTime Watches with [Infinitime firmware](https://github.com/InfiniTimeOrg/InfiniTime/tree/main) (from firmware v1.8, the heart rate signals, XYZ and steps can be broadcast via bluetooth)
  - https://github.com/InfiniTimeOrg/InfiniTime/blob/main/doc/ble.md 
 - Python code connects to PineTimes using [Bleak library](https://bleak.readthedocs.io/en/latest/)
 - Python code extracts HR, XYZ, step count data and manipulates it (change ranges, scales, etc)
 - Python code to convert the manipulated data into [Open Sound Control](https://en.wikipedia.org/wiki/Open_Sound_Control) (OSC) Messages
 - OSC messages are sent to [QLab](https://qlab.app/) (software being used to control the media part of the art installation)
  - [This library](https://github.com/hjwp/python-osc-qlab-interface) seems a good place to start for the implementation of OSC -> QLab
  
  
 ---
 
 Notes:
 
 - [Upgrading the Infinitime firmware](https://github.com/InfiniTimeOrg/InfiniTime/blob/main/doc/gettingStarted/updating-software.md) can be done with [companion apps](https://github.com/InfiniTimeOrg/InfiniTime/blob/main/README.md#companion-apps) (at the momemnt - May/2023 - on Android, Linux or Mac systems). 
 
 
 
