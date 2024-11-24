import gi
gi.require_version("Gtk","3.0")

from gi.repository import Gtk
from controllers.Config import ConfigController

class SettingWindow(Gtk.Builder):
    def __init__(self):
        super().__init__()
        self.add_from_file('templates/SettingsWindow.glade')
        self.window = self.get_object('SettingsWindow')
        
        handlers = {
            'on_accept_button_clicked':self.save_settings_and_close,
            'on_api_key_entry_changed': self.active_apply_button,
            'on_icon_entry_changed': self.active_apply_button,
            'on_covertart_entry_changed': self.active_apply_button,
            'on_banner_entry_changed': self.active_apply_button,
            'on_db_entry_changed': self.active_apply_button,
            'on_icon_button_clicked':self.choose_folder,
            'on_coverart_button_clicked':self.choose_folder,
            'on_banner_button_clicked':self.choose_folder,
            'on_db_button_clicked':self.choose_file,
            'on_apply_button_clicked':self.save_settings_and_stay
        }
        self.connect_signals(handlers)
        self.api_entry:Gtk.Entry = self.get_object('api_key_entry')
        self.icon_entry:Gtk.Entry = self.get_object('icon_entry')
        self.covertart_entry:Gtk.Entry = self.get_object('covertart_entry')
        self.banner_entry:Gtk.Entry = self.get_object('banner_entry')
        self.db_entry:Gtk.Entry = self.get_object('db_entry')
        self.apply_button:Gtk.Button = self.get_object('apply_button')
        self.setup_form()
        
        self.window.show_all()
        
    def setup_form(self):
        self.api_entry.set_text(ConfigController.get_config('FETCHING','api_key'))
        self.icon_entry.set_text(ConfigController.get_config('LOCATIONS','icon'))
        self.covertart_entry.set_text(ConfigController.get_config('LOCATIONS','coverart'))
        self.banner_entry.set_text(ConfigController.get_config('LOCATIONS','banner'))
        self.db_entry.set_text(ConfigController.get_config('LOCATIONS','db'))
        self.apply_button.set_sensitive(False)
    def save_settings(self):
        ConfigController.set_config('FETCHING','api_key',self.api_entry.get_text())
        ConfigController.set_config('LOCATIONS','icon',self.icon_entry.get_text())
        ConfigController.set_config('LOCATIONS','coverart',self.covertart_entry.get_text())
        ConfigController.set_config('LOCATIONS','banner',self.banner_entry.get_text())
        ConfigController.set_config('LOCATIONS','db',self.db_entry.get_text())
        
        ConfigController.write_config()
        
    def save_settings_and_close(self,widget):
        self.save_settings()
        self.window.close()
    def save_settings_and_stay(self,widget):
        self.save_settings()
        self.apply_button.set_sensitive(False)
    def active_apply_button(self,widget):
        self.apply_button.set_sensitive(True)
    def choose_folder(self,widget):
        dialog_b = FolderChooser()
        widget_name = Gtk.Buildable.get_name(widget)
        response = dialog_b.dialog.run()
        if response == Gtk.ResponseType.OK:
            match widget_name:
                case 'icon_button':
                    self.icon_entry.set_text(str(dialog_b.dialog.get_current_folder()))
                case 'coverart_button':
                    self.covertart_entry.set_text(str(dialog_b.dialog.get_current_folder()))
                case 'banner_button':
                    self.banner_entry.set_text(str(dialog_b.dialog.get_current_folder()))
        dialog_b.dialog.destroy()

    def choose_file(self,widget):
        dialog_b = FileChooser()
        
        response =dialog_b.dialog.run()

        if response == Gtk.ResponseType.OK:
            self.db_entry.set_text(str(dialog_b.dialog.get_filename()))
        
        dialog_b.dialog.destroy()

class FolderChooser(Gtk.Builder):
    def __init__(self):
        super().__init__()
        self.add_objects_from_file('templates/FileChooser.glade',['FolderChooser'])
        
        self.dialog = self.get_object('FolderChooser')

class FileChooser(Gtk.Builder):
    def __init__(self):
        super().__init__()
        self.add_objects_from_file('templates/FileChooser.glade',['FileChooser','db_filter'])
        
        self.dialog = self.get_object('FileChooser')