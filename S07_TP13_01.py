
# __str__ = __repr__
# __radd__ = __add__

import tkinter as tk


if __name__ == "__main__":
    TITLE = "Test tkinter"
    WIDTH = 800
    HEIGHT = 500
    POS_x = 100
    POS_Y = 50
    myApp = tk.Tk()
    myApp.title(TITLE)
    myApp.geometry(f"{WIDTH}x{HEIGHT}+{POS_x}+{POS_Y}")

    # create a frame
    my_frame = tk.Frame(myApp)
    my_frame.pack()
    # create a Canvas to draw
    canvas = tk.Canvas(my_frame, background='white')
    canvas.pack()

    # crate an exit button
    button = tk.Button(myApp, text="Close", command=myApp.quit)
    button.pack(side=tk.RIGHT)

    # lunch the app
    myApp.mainloop()
