import tkinter as tk
from classe.sql import SQL 
from gui.ticket import Ticket
from tkinter import messagebox
from classe.parking import Parking
from tkinter import ttk
from pandastable import Table

class GUI:

    def __init__(self):
        self.app = tk.Tk()
        self.app.title("Gestion de parking")
        self.app.geometry("500x500")
        self.current_page = None
        self.sql =  SQL()
        self.parking = Parking()
        self.ticket = Ticket()
        self.dataframe = self.ticket.toPandas()
        self.StatusPage()
        self.showPage(self.__status_frame)

    def start(self):
        self.app.mainloop()

    def showPage(self, page):

        if self.current_page is not None:
            self.current_page.pack_forget()

        if page == self.__status_frame:
            self.app.geometry("900x600")
            self.refreshTable()
            page.pack(fill="both", expand=True, padx=20, pady=20)

        else:
            self.app.geometry("500x500")
            page.pack(pady=30)

        self.current_page = page


    def refreshTable(self):
        self.dataframe = self.ticket.toPandas()
        self.__status_label.config(
            text=f"Il reste {self.parking.verifCapacity()} places disponibles"
        )

        for widget in self.__table_frame.winfo_children():
            widget.destroy()

        colonnes = list(self.dataframe.columns)
        self.tableau = ttk.Treeview(
            self.__table_frame,
            columns=colonnes,
            show="headings"
        )
        self.tableau.bind("<<TreeviewSelect>>", self.onSelect)

        for colonne in colonnes:
            self.tableau.heading(colonne, text=colonne)
            self.tableau.column(colonne, anchor="center", width=150)

        for ligne in self.dataframe.itertuples(index=False, name=None):
            self.tableau.insert("", "end", values=ligne)

        self.tableau.pack(fill="both", expand=True)
    def backMenu(self):
        self.showPage(self.__frame)


    def quitApp(self):
        self.sql.CloseSql()
        self.app.quit()

    def StatusPage(self):
        self.__status_frame = tk.Frame(self.app)
        self.__title = tk.Label(self.__status_frame,text="Tableau de bord - Parking",font=("Arial", 18))
        self.__title.pack(pady=15)
        self.__status_label = tk.Label( self.__status_frame,text="",font=("Arial", 12, "bold"))
        self.__status_label.pack(pady=10)
        self.__actions_frame = tk.Frame(self.__status_frame)
        self.__actions_frame.pack(fill="x", padx=20, pady=10)
        tk.Button(self.__actions_frame,text="+ Nouvelle entrée",width=18,command=self.enter).pack(side="left", padx=5)
        tk.Button(self.__actions_frame,text="Enregistrer sortie",width=18,command=self.sortiSelection).pack(side="left", padx=5)
        tk.Button(self.__actions_frame,text="Payer ticket",width=18,command=self.payerSelection).pack(side="left", padx=5)
        tk.Button(self.__actions_frame,text="Actualiser",width=12,command=self.refreshTable).pack(side="left", padx=5)
        self.__table_frame = tk.Frame(self.__status_frame)
        self.__table_frame.pack(fill="both", expand=True, padx=20, pady=10)
        tk.Button(self.__status_frame,text="Quitter",command=self.quitApp).pack(pady=10)

    def enter(self):
        self.ticket.enter()
        self.refreshTable()    

    def onSelect(self,event):
        selection = self.tableau.selection()
        if selection:
            item_id = selection[0]
            self.valeurs = self.tableau.item(item_id, "values")
            self.ticket_id_selectionne = int(self.valeurs[0])

    def sortiSelection(self):
        ticket_id = self.idTicketSelectionne()
        if ticket_id is not None:
            self.ticket.sortie(ticket_id)
            self.refreshTable()

    def payerSelection(self):
        ticket_id = self.idTicketSelectionne()
        if ticket_id is not None:
            self.ticket.payer(ticket_id)
            self.refreshTable()

    def idTicketSelectionne(self):
        selection = self.tableau.selection()
        if not selection:
            messagebox.showinfo("Sélection requise", "Cliquez d'abord sur un ticket dans le tableau.")
            return None
        valeurs = self.tableau.item(selection[0], "values")
        return int(valeurs[0])



