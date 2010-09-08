import gedit
import gtk
from cucumber_table_cleaner_base import CucumberTableCleaner

class CucumberTableCleanerPlugin(gedit.Plugin):
    def activate(self, window):
        self.__accel = gtk.AccelGroup()
        self.__accel.connect_group(124, gtk.gdk.SHIFT_MASK | gtk.gdk.CONTROL_MASK, gtk.ACCEL_VISIBLE, self.key_pressed) # Ctrl + Shift + |
        window.add_accel_group(self.__accel)
        pass

    def key_pressed(self, accel_group, window, keyval, modifier):
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
        window.remove_accel_group(self.__accel)
        pass

"""
    Examples:
    |first_arg|  second_arg  |  please  |  dont  |  hurt  |  me |
    |i|      am      |   just   |   a    | simple | man |
    |bleah|      i       |   drop   |  this  |  shit  |
|indentation|fail|will|crush|you|
"""

