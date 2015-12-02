
import gtk
from model import ParkingModel
from controller import ParkingController
from view import ParkingView

def main():
   m = ParkingModel()
   v = ParkingView({1:False,2:False})
   c = ParkingController(m, v)

   gtk.main()
   return

if __name__ == "__main__":
   main()

