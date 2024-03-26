import tkinter as tk

class Window:
    def __init__(self) -> None:
        self.rowLen = 0
        self.colLen = 0
        self.isComputerFirst = 0

    def showInputFieldsWindow(self):
        master = tk.Tk()
        master.title("Domineering")
        tk.Label(master, text="Unesite broj horizontalnih polja").grid(row=0)
        tk.Label(master, text="Unesite broj vertikalnih polja").grid(row=1)
        tk.Label(master, text="Prvi igra racunar?").grid(row=2)

        horizontalField = tk.Entry(master)
        horizontalField.grid(row=0, column=1)

        verticalField = tk.Entry(master)
        verticalField.grid(row=1, column=1)

        isCompVar = tk.IntVar()

        isComputerField = tk.Checkbutton(master, variable=isCompVar, onvalue=1, offvalue=0)
        isComputerField.grid(row=2, column=1)

        def exit():
            master.destroy()

        def start():
            self.colLen = int(horizontalField.get())
            self.rowLen = int(verticalField.get())
            self.isComputerFirst = bool(isCompVar.get())
            exit()

        buttonStart = tk.Button(master, text="Start", command=start).grid(row=3)

        master.mainloop()

        return (self.rowLen, self.colLen, self.isComputerFirst)


    def showWinner(self, igrac):
        master = tk.Tk()
        master.title("Winner")
        if(igrac):
            tk.Label(master, text="Pobednik je igrac 2").grid(row=0)
        else:
            tk.Label(master, text="Pobednik je igrac 1").grid(row=0)
        master.mainloop()