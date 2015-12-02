from gtkmvc import Model
import sqlite3


 
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
       print "querying database..."
       st =self.db_conn.execute("SELECT * FROM parking_status")
       st = st.fetchall()
       status_dict = {}
       for park in st:
           status_dict[park[0]] = bool(park[1])

       return status_dict
   @Model.setter
   def status(self, value): return



   def __init__(self):
       Model.__init__(self)
       self.db_conn = sqlite3.connect('db.sqlite')
        

   def get_status(self): 
       print "controller querying database..." 
       return status 
