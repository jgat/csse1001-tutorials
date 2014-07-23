from Tkinter import *
import tkMessageBox


class SampleApp(object):
    def __init__(self, master):
        self._master = master
        master.title("Hello!")
        master.minsize(430, 200)

        self._lbl = Label(master, text="Choose a button")
        # We want the label to stay roughly in the centre when the window is
        # resized, so we use expand, which will claim as much space in all
        # directions as possible. This will keep the label centred, because
        # widgets automatically stay to the centre of all the space that is
        # available to them.
        self._lbl.pack(side=TOP, expand=True)

        # To get the buttons to stay horizontally centred and aligned to the
        # bottom of the window, we created a button frame and align the buttons
        # within it, and apply any alignments we want for the group of buttons
        # collectively to the frame.
        btnframe = Frame(master)
        btnframe.pack(side=TOP)
        # When this button is clicked, the label colour should change to blue.
        btn = Button(btnframe, text="Change to Blue", command=self.change_blue)
        btn.pack(side=LEFT)
        # When this button is clicked, the label colour should change to green.
        btn = Button(btnframe, text="Change to Green",
                     command=self.change_green)
        btn.pack(side=LEFT)

        entryfrm = Frame(master)
        entryfrm.pack(side=TOP, fill=X, padx=10, pady=10)
        Label(entryfrm, text="Change the colour to: ").pack(side=LEFT)
        self._colour_entry = Entry(entryfrm)
        self._colour_entry.pack(side=LEFT, expand=True, fill=X)
        # When this button is clicked, the label colour should change to the
        # colour that the user has entered.
        Button(entryfrm, text="Change it!",
               command=self.change).pack(side=LEFT)

    def change_blue(self):
        """
        Changes the colour of the label to blue.

        change_blue(self) -> None
        """
        self._lbl.config(text="This label is blue", bg="blue")

    def change_green(self):
        """
        Changes the colour of the label to green.

        change_blue(self) -> None
        """
        self._lbl.config(text="This label is green", bg="green")

    def change(self):
        """
        Changes the colour of the label to whatever the user has entered. Shows
        an error box if the user has entered an invalid colour.

        change(self) -> None
        """
        # Get the text that the user has entered in the colour entry.
        col = self._colour_entry.get()
        try:
            # Try to set the colour.
            # Raises a TclError if the colour is invalid
            self._lbl.config(text="This label is " + col, bg=col)
        except TclError:
            # If the user had entered an invalid colour, prompt them.
            tkMessageBox.showerror("Invalid colour",
                                   "'" + col + "' is not a colour!")


if __name__ == "__main__":
    root = Tk()
    app = SampleApp(root)
    root.mainloop()
