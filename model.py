from gtkmvc import Model



PARKING_SPOTS = 2 

class ParkingModel (Model):
   """The model contains a set of messages
   and an observable property that represent the current message
   index"""

   # Observable property: code for that is automatically generated
   # by metaclass constructor. The controller will be the observer
   # for this property
   status = {}
   __observables__ = ("status",)

   def __init__(self):
       Model.__init__(self)

       for i in range(1,PARKING_SPOTS+1):
            self.status[i] = False
 

   def get_status(self): return status

   def set_parking_status(self,parking_num):
       status[parking_num] = not parking_num

