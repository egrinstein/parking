
import gtk
from model import ParkingModel
from controller import ParkingController
from view import ParkingView

import sqlite3

def main():
   m = ParkingModel()
   v = ParkingView(m.status)
   print v,type(v)
   c = ParkingController(m, v)

   gtk.main()

if __name__ == "__main__":
    main()
