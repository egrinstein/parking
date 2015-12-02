import serial
from xbee import ZigBee
import sqlite3

tty = '/dev/ttyUSB0'
baud_rate = 9600

serial_port = serial.Serial(tty,baud_rate)
zb = ZigBee(serial_port)    
print "starting"
db_conn = sqlite3.connect('db.sqlite')
while True:
    try:
        print "waiting"
        data = zb.wait_read_frame()
        print "received:"
        print data
        address,value = data.split()

        status = db_conn.execute("""UPDATE parking_status 
                                    SET status = %(value)
                                    WHERE parking_num = %(adr)
                                    """ % {"value":value,"adr":address})
        db_conn.commit()
    except KeyboardInterrupt:
        break

serial_port.close()
