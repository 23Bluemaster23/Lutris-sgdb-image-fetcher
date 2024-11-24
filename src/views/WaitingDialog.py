import gi
gi.require_version("Gtk","3.0")

from gi.repository import  Gtk


class WaitingDialog(Gtk.Builder):
    def __init__(self):
        super().__init__()
        self.add_from_file('templates/WaitingDialog.glade')
        self.window = self.get_object('WaitingDialog')
        print(self.window)
        self.window.run()