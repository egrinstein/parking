from gtkmvc import Observer

class ParkingObserver(Observer):

   @Observer.observe("parking_database", assign=True,before=True,after=True)
   def assign_notification(self, model, prop_name, info):
       print "assign_notification:", prop_name, info.old, info.new

