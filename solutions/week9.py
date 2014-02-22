from Tkinter import *
import tkMessageBox


class SampleApp(object):
    def __init__(self, master):
        self._master = master
        master.title("Hello!")
        master.minsize(430, 200)

        self._lbl = Label(master, text="Choose a button")
        self._lbl.pack(side=TOP, expand=True)

        btnframe = Frame(master)
        btnframe.pack(side=TOP)
        btn = Button(btnframe, text="Change to Blue", command=self.click_blue)
        btn.pack(side=LEFT)
        btn = Button(btnframe, text="Change to Green", command=self.click_green)
        btn.pack(side=LEFT)

        entryfrm = Frame(master)
        entryfrm.pack(side=TOP, fill=X, padx=10, pady=10)
        Label(entryfrm, text="Change the colour to: ").pack(side=LEFT)
        self._colour_entry = Entry(entryfrm)
        self._colour_entry.pack(side=LEFT, expand=True, fill=X)
        Button(entryfrm, text="Change it!",
               command=self.change).pack(side=LEFT)

    def click_blue(self):
        self._lbl.config(text="This label is blue", bg="blue")

    def click_green(self):
        self._lbl.config(text="This label is green", bg="green")

    def change(self):
        col = self._colour_entry.get()
        try:
            self._lbl.config(text="This label is " + col, bg=col)
        except TclError:
            tkMessageBox.showerror("Invalid colour",
                                   "'" + col + "' is not a colour!")


if __name__ == "__main__":
    root = Tk()
    app = SampleApp(root)
    root.mainloop()
