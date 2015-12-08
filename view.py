from gtkmvc import View
import gtk
import os.path

#gambiarra
from database import Database

GREEN = gtk.gdk.Color(red=0, green=65535, blue=0, pixel=0) 
RED = gtk.gdk.Color(red=65535, green=0, blue=0, pixel=0)


statusToColor = { True:RED,False:GREEN }



class ParkingView(View):
    glade = None
    top = None
    _builder = None
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False
    def set_status(self,status):
        print status
        for park in status:
            self.parkingSign[park].modify_bg(gtk.STATE_NORMAL,statusToColor[status[park]])
    def clicked(self,button):
        st = self.db.get_parking()
        self.set_status(st)
    def __init__(self,status):
        builder = os.path.join("./", "example.glade")
        self.glade_xmlWidgets = []
        View.__init__(self)
        self.db = Database()        
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Parking Spots Availability")
        self.window.connect("delete_event", self.delete_event)
        self.window.set_border_width(200)
        self.box1 = gtk.HBox(False, 10)
        #self.window.add(self.box1)
        self.parkingSign = {}

        print status,type(status)
        for i in status:
            self.parkingSign[i] = gtk.DrawingArea()
            self.parkingSign[i].set_size_request(100,200)
            self.parkingSign[i].modify_bg(gtk.STATE_NORMAL,statusToColor[status[i]])
            self.parkingSign[i].show()
		  
            label = gtk.Label()
            label.show()
            label.set_text("Parking #"+str(i))
            vbox = gtk.VBox(False,0)
            vbox.pack_start(label,True,True,0)
            vbox.pack_start(self.parkingSign[i],True,True,0)
            vbox.show()
            self.box1.pack_start(vbox)

        self.box1.show()

        self.button = gtk.Button('refresh')
        self.box2 = gtk.VBox(False,10)
        self.window.add(self.box2)
        self.box2.pack_start(self.button)
        self.box2.pack_start(self.box1)
        self.box2.show()
        self.button.show()
        #self.button.connect('clicked',self.clicked)               
        self.window.show()

