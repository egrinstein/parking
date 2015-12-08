import serial
from database import Database
from time import time


CLOCK_TIME = 5 
AVG_RATE = 35 



database = Database()
status = database.get_parking()
movement_table = {}
print "Database Status:",status
for parking_num in status:
    movement_table[parking_num] = 0
clock = int(time())


park = 0 
park_value = 0
while True:

    ser = serial.Serial('/dev/ttyUSB0', 9600)
    sig = ser.readline().split()
    #print "signal: ",sig,"Length=",len(sig)
    

    if len(sig) == 2:
        try:
            park = int(sig[1])
        except:
            print "Unexpected Format"
        #print "parking #",park," updated"
        continue
    elif len(sig) == 1:
        #print "new status:",sig[0]
        if park == -1:
            continue
        else:
            try:
                park_value = int(sig[0])
            except:
                print "Exception:",sig
    now = int(time())
    #print "time: ",now - clock
    try: 
        movement_table[park] += park_value 
        park = park_value = -1
    except KeyError:
        print "not a parking spot:",park 
        continue
    if now - clock >= CLOCK_TIME:
        print "Database Updated:",movement_table
        for p in movement_table:
            if movement_table[p] >= AVG_RATE:
                occupied = 1
            else:
                occupied = 0
            database.set_parking(p,occupied)
            movement_table[p] = 0
        clock = now


