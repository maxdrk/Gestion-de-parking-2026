
import tkinter as tk
from ticket import Ticket
from tkinter import messagebox


class GUI:

    def __init__(self):
        self.app = tk.Tk()
        self.app.title("Gestion de parking")
        self.app.geometry("500x500")
        self.current_page = None
        self.ticket = Ticket()
        self.Menu()
        self.EnterExit()
        self.StatusPage()
        self.showPage(self.__frame)

    def start(self):
        self.app.mainloop()

    def showPage(self, page):
        if self.current_page is not None:
            self.current_page.pack_forget()

        page.pack(pady=30)
        self.current_page = page

    def backMenu(self):
        self.showPage(self.__frame)


    def Menu(self):

        self.__frame = tk.Frame(self.app)
        self.__title = tk.Label(self.__frame,text="Gestion de parking",font=("Arial", 20))
        self.__title.pack(pady=20)
        self.__button_enter = tk.Button(self.__frame,text="Entrée / Sortie véhicule",width=25,command=lambda: self.showPage(self.__enterExit))
        self.__button_enter.pack(pady=10)
        self.__button_status = tk.Button(self.__frame,text="État du parking", width=25,command=lambda: self.showPage(self.__status_frame) )
        self.__button_status.pack(pady=10)
        self.__button_quit = tk.Button(self.__frame, text="Quitter",width=25,command=self.app.destroy)
        self.__button_quit.pack(pady=10)


    def EnterExit(self):
        self.__enterExit = tk.Frame(self.app)
        self.__title = tk.Label(self.__enterExit,text="Gestion des entrées et sorties",font=("Arial", 18))
        self.__title.pack(pady=20)
        self.__button_enter = tk.Button(self.__enterExit,text="Enregistrer une entrée",width=25,command=self.ticket.enter)
        self.__button_enter.pack(pady=10)
        self.__button_exit = tk.Button(self.__enterExit,text="Enregistrer une sortie",width=25,command=self.ticket.sortie)
        self.__button_exit.pack(pady=10)
        self.__button_pay = tk.Button(self.__enterExit,text="Payer le ticket",width=25,command=lambda:messagebox.showinfo("","En développement"))
        self.__button_pay.pack(pady=20)
        self.__button_back = tk.Button(self.__enterExit,text="Retour au menu",command=self.backMenu)
        self.__button_back.pack(pady=20)

    def StatusPage(self):
        self.__status_frame = tk.Frame(self.app)
        self.__title = tk.Label(self.__status_frame,text="État du parking",font=("Arial", 18))
        self.__title.pack(pady=20)
        self.__status_label = tk.Label(self.__status_frame,text="En Développement")
        self.__status_label.pack(pady=10)
        self.__button_back = tk.Button(self.__status_frame,text="Retour au menu",command=self.backMenu)
        self.__button_back.pack(pady=20)




