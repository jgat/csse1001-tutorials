from Tkinter import *

class HelloWorld(Frame):
    """
    HelloWorld class

    A simple example demonstrating how a button, label and spinbox
    work
    """
    def __init__(self, master):
        """
        HelloWorld.__init__(Tk) -> HelloWorld

        Initialise an instance of the HelloWorld class.
        """
        Frame.__init__(self, master)

        master.title('HelloWorld')
        
        self.btn1 = Button(self, text = "Button 1", command = self.hello)
        self.btn1.pack(side = TOP)

        self.lbl = Label(self, text = "I am a label")
        self.lbl.pack(side = TOP)

        self.spn = Spinbox(self, values = ('I', 'am', 'a', 'spinbox'))
        self.spn.pack(side = TOP)

        self.pack()

    def hello(self):
        """
        HelloWorld.hello() -> None

        A callback for btn1.
        """
        print 'Hello!'



if __name__ == '__main__':
    
    root = Tk()
    app = HelloWorld(root)
    root.mainloop()
