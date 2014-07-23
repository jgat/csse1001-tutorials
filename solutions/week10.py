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
        # Holds the current state of the preview
        # True => preview on; False => preview off
        self._preview_on = True

    def _toggle_preview(self):
        """Toggle the line preview on/off.
        """

        """
        # The simplest way to think about this problem is to split it into two
        # cases:
        # What to do when the 1) Preview is on; 2) Preview is off.

        if self._preview_on:
            # preview is on, so turn it off
            self._preview_btn.config(text="Preview Off", bg="grey")
            self._preview_on = False
        else:
            # preview is off, so turn it on
            self._preview_btn.config(text="Preview On", bg="green")
            self._preview_on = True

        # We can notice in both cases, we are inverting (i.e. flipping or
        #   toggling) the preview state
        # True => False; False => True

        # This can help us simplify our code in that we can replace the
        # following lines:

        # with self._preview_on = not self._preview_on
        # which we can move outside of the if/else block because it is happening
        # the same in all cases

        # This would simplify to
        """
        if self._preview_on:
            # preview is on, so turn it off
            self._preview_btn.config(text="Preview Off", bg="grey")
        else:
            # preview is off, so turn it on
            self._preview_btn.config(text="Preview On", bg="green")
        self._preview_on = not self._preview_on

        """
        Alternatively, we could toggle the preview state first. To do so, we
        # would also need to swap the if blocks (since the if would be checking
        # for the new state, not the old one), as is shown below:
        
        self._preview_on = not self._preview_on
        if self._preview_on:
            self._preview_btn.config(text="Preview On", bg="green")
        else:
            self._preview_btn.config(text="Preview Off", bg="grey")
        """

    def is_preview_on(self):
        """Return True if the Preview setting is on, otherwise False.
        """
        """
        #We could solve this problem with an if statement:

        if self._preview_on:
            return True
        else:
            return False

        # But we can notice that in both cases we are returning the value of our
        # state flag _preview_on, that is, when it is True, we return True, and
        # otherwise (i.e. it is False), we return False
        # This allows us to simplify it to one line, as shown below:
        """
        return self._preview_on

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
        # this will hold the position of the user's "first" click, in the form
        # of (x, y); if the user has not clicked, or clicks a second time, this
        # should be None
        self._start = None

        # create a line of all the lines that the user has drawn
        self._lines = []

    def evt_motion(self, e):
        """Event handler for Mouse movement on the Canvas
        """
        """
        # We can use the method that we implemented, SettingsFrame.set_position,
        # to take care of setting the label text appropriately.

        # The reason why we define such a method is that it allows us to create
        # a widget that will take care of the "how" of displaying the text (i.e.
        # setting the correct label, etc.), while only having to specify "what"
        # needs to be displayed (i.e. the position).

        """
        self._settings.set_position(e.x, e.y)

        # Draw the preview if it should be drawn.
        # If the preview setting is off, it's possible that there are still
        # preview lines lingering around, so redraw everything anyway.
        if self._start is not None:
            # get rid of everything that is not a completed line (i.e. the user
            # clicked twice)
            self.redraw()
            # if the preview is on, draw a preview for this line
            if self._settings.is_preview_on():
                self._canvas.create_line(self._start, (e.x, e.y))

    def exit(self):
        """Close the application.
        """
        self._master.destroy()

    def clear(self):
        """Delete all lines from the application.
        """
        self._canvas.delete(ALL)
        self._start = None
        self._lines = []

    def evt_click(self, e):
        """Event handler for clicking the canvas: Draw a line
        """
        if self._start is None:
            self._start = (e.x, e.y)
        else:
            self._lines.append((self._start, (e.x, e.y)))
            self._start = None
            self.redraw()

    def redraw(self):
        """Remove all drawings and redraw all lines on the canvas.
        """
        """
        # When we redraw, we are intending to refresh or update the window
        # display. The reason for this is that we only want the lines that the
        # user has completed drawing, but not anything else (i.e. the preview
        # lines).
        """
        self._canvas.delete(ALL)
        for line in self._lines:
            self._canvas.create_line(line)

if __name__ == '__main__':
    root = Tk()
    app = DrawingApp(root)
    root.mainloop()
