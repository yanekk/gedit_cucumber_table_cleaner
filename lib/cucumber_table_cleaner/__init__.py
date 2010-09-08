import gedit
import gtk
from cucumber_table_cleaner_base import CucumberTableCleaner

class CucumberTableCleanerPlugin(gedit.Plugin):
    def activate(self, window):
        window.connect("key-press-event", self.key_pressed)
        pass

    def key_pressed(self, window, event):
        if (event.state & gtk.gdk.CONTROL_MASK) and (event.state & gtk.gdk.SHIFT_MASK) and (event.keyval == 124): # Ctrl + Shift + |
            try:
                document = window.get_active_document()
                from_marker, to_marker = document.get_selection_bounds()

                from_marker.backward_line()
                from_marker.forward_line() # dirty hack to go to the beggining of line

                to_marker.forward_line()
                #to_marker.backward_line()

                cleaned = CucumberTableCleaner.clean(from_marker.get_slice(to_marker))
                document.delete(from_marker, to_marker)
                document.insert(from_marker, cleaned)

            except ValueError:
                pass # no selection set

        return False
        pass

    def deactivate(self, window):
        pass
    def update_ui(self, window):
        pass

"""
    Examples:
    |first_arg|  second_arg  |  please  |  dont  |  hurt  |  me |
    |i|      am      |   just   |   a    | simple | man |
    |bleah|      i       |   drop   |  this  |  shit  |
|indentation|fail|will|crush|you|
"""

