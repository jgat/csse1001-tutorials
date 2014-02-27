from Tkinter import *


class SettingsFrame(Frame):
    """A frame which allows users to change settings of the application

    Settings to change include line width (thickness), and whether or not a
    line preview is shown.
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
        self._preview = True

    def _toggle_preview(self):
        """Toggle the line preview on/off.
        """
        self._preview = not self._preview
        if self._preview:
            self._preview_btn.config(text="Preview On", bg="green")
        else:
            self._preview_btn.config(text="Preview Off", bg="grey")

    def is_preview_on(self):
        """Return True if the Preview setting is on, otherwise False.
        """
        return self._preview

    def set_position(self, x, y):
        """Change the 'Current Position' label to show new coordinates.
        """
        self._pos_lbl.config(text="Current Position: ({}, {})".format(x, y))


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

        self._canvas.bind('<Button-1>', self.evt_click)
        self._start = None
        # self._lines = []
        self._preview_line = None

    def evt_motion(self, e):
        """Event handler for Mouse movement on the Canvas
        """
        self._settings.set_position(e.x, e.y)

        # Delete and redraw the preview if it should be drawn.
        self._canvas.delete(self._preview_line)
        if self._start is not None and self._settings.is_preview_on():
                self._preview_line = self._canvas.create_line((self._start,
                                                               (e.x, e.y)))

        # Alternative: delete everything and redraw_all
        # If the preview setting is off, it's possible that there are still
        # preview lines lingering around, so redraw everything anyway.

        # if self._start is not None:
        #    self.redraw()
        #    if self._settings.is_preview_on():
        #        self._canvas.create_line(self._start, (e.x, e.y))

    def exit(self):
        """Close the application.
        """
        self._master.destroy()

    def clear(self):
        """Delete all lines from the application.
        """
        self._canvas.delete(ALL)
        self._start = None
        # self._lines = []

    def evt_click(self, e):
        """Event handler for clicking the canvas: Draw a line
        """
        if self._start is None:
            self._start = (e.x, e.y)
            # Begin the preview line
            if self._settings.is_preview_on():
                self._preview_line = self._canvas.create_line(self._start,
                                                              self._start)
        else:
            # self._lines.append((self._start, (e.x, e.y)))
            # self.redraw()

            # Change the preview line so the current line is final.
            self._preview_line = None
            self._start = None

    # This method is only necessary if using the "delete everything" strategy.
    def redraw(self):
        """Remove all drawings and redraw all lines on the canvas.
        """
        self._canvas.delete(ALL)
        for line in self._lines:
            self._canvas.create_line(line)

if __name__ == '__main__':
    root = Tk()
    app = DrawingApp(root)
    root.mainloop()
