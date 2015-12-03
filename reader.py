import serial
from database import Database
from time import time


CLOCK_TIME = 10 # 10 secs
MEDIUM_OCCUPATION_RATE = 50

class Reader:
    def __init__(self):
        database = Database()
        status = database.get_parking()
        movement_table = {}
        for parking_num in status:
            movement_table[parking_num] = 0
        clock = int(time())
        while True:
        
            ser = serial.Serial('/dev/ttyUSB0', 9600)
            park = ser.readline()
            
            try:
                park = int(park)
            except ValueError:
                continue
            movement_table[park] += 1
            now = int(time())
            if now - clock >= CLOCK_TIME:
                for p in movement_table[p]:
                    if movement_table[p] >= MEDIUM_OCCUPATION_RATE
                        occupied = 1
                    else:
                        occupied = 0
                    database.set_parking(p,occupied)
                    movement_table[p] = 0
                clock = now
            
