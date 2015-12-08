
from gtkmvc import Controller

class ParkingController(Controller):
    #@Controller.observe("status", assign=True)   
    def value_change(self, model, name, info):
       self.view.set_status(self.model.status)
       return
    def register_view(self, view):
        return
 
    def on_button_clicked(self, button):
        self.view.set_status(self.model.status)

    def __init__(self,model,view):
        #Controller.__init__(self, model, view)
        self.view = view
        self.model = model
        print "...controller initiated." 
        self.view.button.connect('clicked', self.on_button_clicked)
