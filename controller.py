
from gtkmvc import Controller

class ParkingController(Controller):
 
   @Controller.observe("status", assign=True)
   def value_change(self, model, name, info):
       print info,type(info) 
       status = self.model.get_status()

       self.view.set_status(status)
       return

