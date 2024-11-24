#!/usr/bin/python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
#import pyxhook

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Configurator")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.ipEntry = Gtk.Entry()
        self.ipEntry.set_text("IP Address")

        self.maskEntry = Gtk.Entry()
        self.maskEntry.set_text("NetMask")

        self.gatewayEntry = Gtk.Entry()
        self.gatewayEntry.set_text("gatewayEntry")

        self.button1 = Gtk.Button(label="Save")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.ipEntry, True, True, 0)
        self.box.pack_start(self.maskEntry, True, True, 0)
        self.box.pack_start(self.gatewayEntry, True, True, 0)
        self.box.pack_start(self.button1, True, True, 0)

        #catch window destroy event and stop it from happening
        self.connect('delete-event', self.on_destroy)
        self.connect('key-press-event', self.on_keypress)

    def on_keypress(self, widget, event):
        global w
        if event.keyval == Gdk.KEY_F5:
            isVisible = w.get_property("visible")
            if (isVisible):
                w.hide()
            else:
                w.show()
        print("Keypress")

    def on_button1_clicked(self, widget):
        print("Hello")

    def on_destroy(self, widget=None, *data):
        print("tried to destroy")
        self.hide()
        return False

w = MyWindow()

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
win.set_keep_above(True)


Gtk.main() 