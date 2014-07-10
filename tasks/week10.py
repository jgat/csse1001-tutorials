from Tkinter import *


class SettingsFrame(Frame):
    """A frame which allows users to change settings of the application

    Settings to change are: whether or not a line preview is shown.
    """
    def __init__(self, parent):
        """Initialise the widget, with its subwidgets

        Constructor: SettingsFrame(<container>)
        """
        Frame.__init__(self, parent)

        self._pos_lbl = Label(self, text="Current Position:")
        self._pos_lbl.pack(side=LEFT)

        self._preview_btn = Button(self, text="Preview On", bg="green",
                                   command=self._toggle_preview)
        self._preview_btn.pack(side=RIGHT)

    def _toggle_preview(self):
        """Toggle the line preview on/off.
        """
        pass  # Replace this with your solution

    def is_preview_on(self):
        """Return True if the Preview setting is on, otherwise False.
        """
        pass  # Replace this with your solution

    def set_position(self, x, y):
        """Change the 'Current Position' label to show new coordinates.
        """
        pass  # Replace this with your solution


class DrawingApp(object):
    """An application for drawing lines.
    """
    def __init__(self, master):
        """Initialise a DrawingApp object, including widget layout.

        Constructor: Drawing(Tk)
        """
        self._master = master
        master.title("Drawing Application")
        master.minsize(500, 375)

        self._canvas = Canvas(master, bd=2, relief=SUNKEN)
        self._canvas.pack(side=TOP, expand=True, fill=BOTH)
        self._canvas.bind('<Motion>', self.evt_motion)
        # More Canvas bindings can be added here

        self._settings = SettingsFrame(master)
        self._settings.pack(side=TOP, fill=X, padx=10, pady=5)

        menubar = Menu(master)
        master.config(menu=menubar)

        filemenu = Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Exit", command=self.exit)

        editmenu = Menu(menubar)
        menubar.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Clear All Lines", command=self.clear)

    def evt_motion(self, e):
        """Event handler for Mouse movement on the Canvas
        """
        print e.x, e.y  # Replace this with your solution

    def exit(self):
        """Close the application.
        """
        self._master.destroy()

    def clear(self):
        """Delete all lines from the application.
        """
        self._canvas.delete(ALL)

if __name__ == '__main__':
    root = Tk()
    app = DrawingApp(root)
    root.mainloop()
