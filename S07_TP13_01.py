
# __str__ = __repr__
# __radd__ = __add__
import tkinter as tk


def leave(app):
    app.quit()
    app.destroy()


if __name__ == "__main__":
    myApp = tk.Tk()
    myApp.title("My first GUI")
    myApp.geometry("900x200")
    tk.Button(myApp, text="Click me", command=myApp.quit).pack()
    tk.Button(myApp, text="Destroy me", command=myApp.destroy).pack()
    myApp.mainloop()
