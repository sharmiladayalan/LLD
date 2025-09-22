from abc import ABC,abstractmethod

class Button(ABC):
    @abstractmethod
    def close_button(self):
        pass
    @abstractmethod
    def max_button(self):
        pass
#concrete
class Windowosbutton(Button):
    def close_button(self):
        print("windows close button")

    def max_button(self):
        print("windows max button")


class Macosbutton(Button):
    def close_button(self):
        print("MAC close button")

    def max_button(self):
        print("MAC max button")


#creator interface
class Dilogwindow(ABC):
    @abstractmethod
    def render_dialog_window(self):
        pass

#concrete creators
class WindowosDialog(Dilogwindow):
    def render_dialog_window(self):
        window_button=Windowosbutton()
        window_button.close_button()
        window_button.max_button()


class MacosDialog(Dilogwindow):
    def render_dialog_window(self):
        mac_close_button = Macosbutton()
        mac_close_button .close_button()
        mac_close_button.max_button()

#factory classes
class Dialogfactory(ABC):
    @abstractmethod
    def render_dialog(self):
        pass

class WindowOSDialogfactory(Dialogfactory):
    def render_dialog(self):
        return WindowosDialog()

class MacOSDialogfactory(Dialogfactory):
    def render_dialog(self):
        return MacosDialog()

#clint code
def render_dialog_window(dialog_window:Dialogfactory):
    dialog_window:Dilogwindow=dialog_window.render_dialog()
    dialog_window.render_dialog_window()


windows_dialog_factory=WindowOSDialogfactory()
render_dialog_window(windows_dialog_factory)


mac_dialog_factory=MacOSDialogfactory()
render_dialog_window(mac_dialog_factory)