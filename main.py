
import gtk
from model import ParkingModel
from controller import ParkingController
from view import ParkingView
from  database import Database


def main():
   db = Database()
   db.set_parking(1,0)
   db.set_parking(2,0)
   m = ParkingModel()
   v = ParkingView(m.status)
   c = ParkingController(m, v)
   gtk.main()

if __name__ == "__main__":
    main()
