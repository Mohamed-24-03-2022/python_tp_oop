import tkinter as tk

class AppBase(tk.Tk):
    def __init__(self, title, width, height, pos_x, pos_y):
        tk.Tk.__init__(self)
        self.title(title)
        self.geometry(f"{width}x{height}+{pos_x}+{pos_y}")

        self.__f_main = tk.Frame(self)
        self.__f_main.pack()
        
        self.__c_draw = tk.Canvas(self.__f_main, background='white')
        self.__c_draw.pack()

        self.__b_quit = tk.Button(self, text="Close", command=self.quit)
        self.__b_quit.pack(side=tk.RIGHT)



if __name__ == "__main__":
    TITLE = "Test tkinter"
    WIDTH = 800
    HEIGHT = 500
    POS_X = 100
    POS_Y = 50
    myApp = AppBase(TITLE, WIDTH, HEIGHT,POS_X, POS_Y)
    myApp.mainloop()
    # create a frame    
    # create a Canvas to draw
    # crate an exit button
    # lunch the app
    

