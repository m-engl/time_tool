# pre-modeling, outline, trying out layouts...

import tkinter as tk

root = tk.Tk()

categories = {1 : "Math", 2 : "Literature", 3 : "Logic", 4 : "English"}

class Interface(tk.Frame):

    def __init__(self, master, *args, **kwargs):

        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.create_category_set(categories)

    def create_category_set(self, categories):

        x = 0
        y = 0


        for id, catName in categories.items():
            CategoryNameLabel = tk.Label(self, text=catName)
            StartButton = tk.Button(self, text="Start")
            StopButon = tk.Button(self, text="Stop")

            CategoryNameLabel.grid(row=x, column=y)
            StartButton.grid(row=x, column=y+1)
            StopButon.grid(row=x, column=y+2)
            x += 1


main = Interface(root)
main.pack()
root.mainloop()