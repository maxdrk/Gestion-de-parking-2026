import tkinter as tk
from tkinter import messagebox

class GUI:

    def __init__(self):
        self.app = tk.Tk()
        self.app.title("Gestion de parking")
        self.app.geometry("500x500")
        self.Menu()
    def start(self):
        self.app.mainloop()
    def Menu(self):
        self.__frame = tk.Frame(self.app)
        self.__frame.pack(pady=30)
        self.__title = tk.Label(self.__frame,text="Gestion de parking",font=("Arial", 20))
        self.__title.pack(pady=20)
        self.__button_enter = tk.Button( self.__frame,text="Entrée véhicule",width=25,command=lambda :messagebox.showinfo("Indisponible","En cours de développement"))
        self.__button_enter.pack(pady=10)
        self.__button_exit = tk.Button(self.__frame,text="Sortie véhicule",width=25,command= lambda:messagebox.showinfo("Indisponible","En cours de développement"))
        self.__button_exit.pack(pady=10)
        self.__button_status = tk.Button(self.__frame,text="État du parking",width=25,command=lambda:messagebox.showinfo("Indisponible","En cours de développement"))
        self.__button_status.pack(pady=10)
        self.__button_quit =  tk.Button(self.__frame,text="quitter",width=25, command=self.app.quit)
        self.__button_quit.pack(pady=10)