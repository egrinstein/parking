from gtkmvc import Model
from database import Database


 
class ParkingModel (Model):
   """The model contains a set of messages
   and an observable property that represent the current message
   index"""

   # Observable property: code for that is automatically generated
   # by metaclass constructor. The controller will be the observer
   # for this property
   
   __observables__ = ("status",)
   @Model.getter
   def status(self):
       return self.db_conn.get_parking()
   @Model.setter
   def status(self, value): return



   def __init__(self):
       Model.__init__(self)
       self.db_conn = Database()
        

   def get_status(self): 
       print "controller querying database..." 
       return status 
