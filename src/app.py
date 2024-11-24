import gi
gi.require_version("Gtk","3.0")

from gi.repository import Gtk,Gdk
from views.MainWindow import MainWindow

if __name__ == "__main__":
    win = MainWindow()
    style_provider = Gtk.CssProvider()
    style_provider.load_from_path('./styles/styles.css')
    Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(),style_provider,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    
    Gtk.main()