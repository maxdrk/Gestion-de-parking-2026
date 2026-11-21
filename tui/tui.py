import math
import os
import sys
from datetime import datetime, timedelta

from textual import events, work
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Center, Vertical
from textual.screen import ModalScreen, Screen
from textual.widgets import DataTable, Input, OptionList, Static
from textual.widgets.option_list import Option

# sql.py et parking.py se trouvent dans le dossier classe/
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "classe"))

from parking import Parking
from sql import SQL


BANNIERE_GRANDE = """\
   █████████  ██████████  █████████  ███████████ █████    ███████    ██████   █████    ██████████   ██████████
  ███░░░░░███░░███░░░░░█ ███░░░░░███░█░░░███░░░█░░███   ███░░░░░███ ░░██████ ░░███    ░░███░░░░███ ░░███░░░░░█
 ███     ░░░  ░███  █ ░ ░███    ░░░ ░   ░███  ░  ░███  ███     ░░███ ░███░███ ░███     ░███   ░░███ ░███  █ ░
░███          ░██████   ░░█████████     ░███     ░███ ░███      ░███ ░███░░███░███     ░███    ░███ ░██████
░███    █████ ░███░░█    ░░░░░░░░███    ░███     ░███ ░███      ░███ ░███ ░░██████     ░███    ░███ ░███░░█
░░███  ░░███  ░███ ░   █ ███    ░███    ░███     ░███ ░░███     ███  ░███  ░░█████     ░███    ███  ░███ ░   █
 ░░█████████  ██████████░░█████████     █████    █████ ░░░███████░   █████  ░░█████    ██████████   ██████████
  ░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░     ░░░░░    ░░░░░    ░░░░░░░    ░░░░░    ░░░░░    ░░░░░░░░░░   ░░░░░░░░░░

            ███████████    █████████   ███████████   █████   ████ █████ ██████   █████   █████████
           ░░███░░░░░███  ███░░░░░███ ░░███░░░░░███ ░░███   ███░ ░░███ ░░██████ ░░███   ███░░░░░███
            ░███    ░███ ░███    ░███  ░███    ░███  ░███  ███    ░███  ░███░███ ░███  ███     ░░░
            ░██████████  ░███████████  ░██████████   ░███████     ░███  ░███░░███░███ ░███
            ░███░░░░░░   ░███░░░░░███  ░███░░░░░███  ░███░░███    ░███  ░███ ░░██████ ░███    █████
            ░███         ░███    ░███  ░███    ░███  ░███ ░░███   ░███  ░███  ░░█████ ░░███  ░░███
            █████        █████   █████ █████   █████ █████ ░░████ █████ █████  ░░█████ ░░█████████
           ░░░░░        ░░░░░   ░░░░░ ░░░░░   ░░░░░ ░░░░░   ░░░░ ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░░
"""

BANNIERE_COMPACTE = """\
█▀▀ █▀▀ ▄▀▀ ▀█▀ ▀█▀ █▀█ █▄░█  █▀▄ █▀▀  █▀█ ▄▀█ █▀█ █░█ ▀█▀ █▄░█ █▀▀
█▄█ ██▄ ▄██ ░█░ ▄█▄ █▄█ █░▀█  █▄▀ ██▄  █▀▀ █▀█ █▀▄ █▀▄ ▄█▄ █░▀█ █▄█
"""


def choisirBanniere(largeur: int, hauteur: int) -> str:
    """Renvoie la plus grande bannière qui tient dans le terminal."""
    if largeur >= 112 and hauteur >= 26:
        return BANNIERE_GRANDE
    if largeur >= 69 and hauteur >= 12:
        return BANNIERE_COMPACTE
    return "GESTION DE PARKING"


class TicketErreur(Exception):
    """Erreur à afficher. info=True : simple information au lieu d'une erreur."""

    def __init__(self, message: str, info: bool = False):
        super().__init__(message)
        self.info = info


class TicketTUI:

    def __init__(self, sql: SQL, parking: Parking):
        self.__sql = sql
        self.__parking = parking

    def enter(self) -> int:
        """Crée un ticket et renvoie son numéro."""
        # <= 0 et pas "not" : verifCapacity() peut renvoyer un nombre négatif
        if self.__parking.verifCapacity() <= 0:
            raise TicketErreur("Parking complet")
        command = self.__sql.Command("INSERT INTO tickets DEFAULT VALUES")
        if isinstance(command, Exception):
            raise TicketErreur(f"Erreur lors de la génération du ticket : {command}")
        return command.lastrowid

    def getId(self, ticketId: int):
        result = self.__sql.Command(
            "SELECT id, heure_entree, heure_sortie FROM tickets WHERE id = ?", (ticketId,)
        )
        if isinstance(result, Exception):
            raise TicketErreur(f"Erreur de base de données : {result}")
        return result.fetchone()

    def sortie(self, ticketId: int) -> str:
        """Clôture un ticket et renvoie l'heure de sortie."""
        ticket = self.getId(ticketId)
        if ticket is None:
            raise TicketErreur("Aucun ticket trouvé pour cet ID.")
        if ticket[2] is not None:
            raise TicketErreur("Ce ticket a déjà été clôturé.", info=True)

        heure_sortie = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = self.__sql.Command(
            "UPDATE tickets SET heure_sortie = ? WHERE id = ?", (heure_sortie, ticketId)
        )
        if isinstance(result, Exception):
            raise TicketErreur(f"Impossible de clôturer le ticket : {result}")
        if result.rowcount == 0:
            raise TicketErreur("Aucun ticket n'a été modifié.")
        return heure_sortie

    def calculerPaiement(self, ticketId: int) -> tuple[timedelta, float]:
        """Vérifie le ticket et renvoie (durée du stationnement, montant à payer)."""
        result = self.__sql.Command(
            "SELECT heure_entree, heure_sortie, paid_ticket FROM tickets WHERE id = ?",
            (ticketId,),
        )
        if isinstance(result, Exception):
            raise TicketErreur(f"Erreur de base de données : {result}")
        ticket = result.fetchone()
        if ticket is None:
            raise TicketErreur("Aucun ticket existant pour cette référence.")

        heure_entree, heure_sortie, paid_ticket = ticket
        if heure_sortie is None:
            raise TicketErreur("Ce ticket est toujours ouvert (véhicule non sorti).", info=True)
        if paid_ticket == 1:
            raise TicketErreur("Le ticket est déjà payé.", info=True)

        entree = datetime.fromisoformat(heure_entree)
        sortie = datetime.fromisoformat(heure_sortie)
        duree = sortie - entree

        minutes_facturables = max(0, duree.total_seconds() / 60 - 30)
        tranches = math.ceil(minutes_facturables / 15)
        total = round(min(tranches * 0.30, 12), 2)
        return duree, total

    def confirmerPaiement(self, ticketId: int) -> None:
        result = self.__sql.Command("UPDATE tickets SET paid_ticket = 1 WHERE id = ?", (ticketId,))
        if isinstance(result, Exception):
            raise TicketErreur(f"Impossible d'enregistrer le paiement : {result}")

    def lister(self) -> list[tuple]:
        """Renvoie tous les tickets : (référence, arrivée, sortie, payé)."""
        result = self.__sql.Command(
            "SELECT id, heure_entree, heure_sortie, paid_ticket FROM tickets ORDER BY id"
        )
        if isinstance(result, Exception):
            raise TicketErreur(f"Erreur de base de données : {result}")
        return result.fetchall()


def formatEuros(montant: float) -> str:
    """Ex. : 1,20 €"""
    return f"{montant:.2f} €".replace(".", ",")


def formatDuree(duree: timedelta) -> str:
    """Ex. : 1 j 2 h 05 min 12 s"""
    secondes = int(duree.total_seconds())
    jours, secondes = divmod(secondes, 86400)
    heures, secondes = divmod(secondes, 3600)
    minutes, secondes = divmod(secondes, 60)
    texte = f"{heures} h {minutes:02d} min {secondes:02d} s"
    return f"{jours} j {texte}" if jours else texte


class MessageModal(ModalScreen[None]):

    BINDINGS = [Binding("enter,escape", "dismiss", "Continuer")]

    def __init__(self, titre: str, message: str):
        super().__init__()
        self.titre = titre
        self.message = message

    def compose(self) -> ComposeResult:
        with Vertical(classes="dialog"):
            yield Static(self.titre, classes="dialog-titre")
            yield Static(self.message, classes="dialog-message", markup=False)
            yield Static("Entrée pour continuer", classes="aide")


class DemandeTicketModal(ModalScreen[int | None]):

    BINDINGS = [Binding("escape", "dismiss(None)", "Annuler")]

    def __init__(self, titre: str, question: str):
        super().__init__()
        self.titre = titre
        self.question = question

    def compose(self) -> ComposeResult:
        with Vertical(classes="dialog"):
            yield Static(self.titre, classes="dialog-titre")
            yield Static(self.question, classes="dialog-message")
            yield Input(placeholder="Numéro du ticket", type="integer", id="numero")
            yield Static("Entrée valider · Échap annuler", classes="aide")

    def on_mount(self) -> None:
        self.query_one("#numero", Input).focus()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        valeur = event.value.strip()
        if not valeur.isdigit():
            self.notify("Veuillez entrer un numéro de ticket valide.", severity="error")
            return
        self.dismiss(int(valeur))


class ConfirmationModal(ModalScreen[bool]):

    BINDINGS = [Binding("escape", "dismiss(False)", "Non")]

    def __init__(self, titre: str, message: str):
        super().__init__()
        self.titre = titre
        self.message = message

    def compose(self) -> ComposeResult:
        with Vertical(classes="dialog"):
            yield Static(self.titre, classes="dialog-titre")
            yield Static(self.message, classes="dialog-message")
            yield OptionList(Option("Oui", id="oui"), Option("Non", id="non"), id="choix")
            yield Static("↑↓ choisir · Entrée valider", classes="aide")

    def on_mount(self) -> None:
        choix = self.query_one("#choix", OptionList)
        choix.highlighted = 0
        choix.focus()

    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        self.dismiss(event.option_id == "oui")


class MenuScreen(Screen):

    BINDINGS = [Binding("q", "app.quit", "Quitter")]

    def compose(self) -> ComposeResult:
        with Vertical(id="accueil"):
            with Center():
                yield Static(id="banniere", markup=False)
            with Center():
                yield OptionList(
                    Option("Entrée / Sortie véhicule", id="entree-sortie"),
                    Option("État du parking", id="etat"),
                    Option("Quitter", id="quitter"),
                    id="menu",
                )
            yield Static("↑↓ naviguer · Entrée valider · q quitter", classes="aide")

    def on_mount(self) -> None:
        self.majBanniere(self.app.size.width, self.app.size.height)
        menu = self.query_one("#menu", OptionList)
        menu.highlighted = 0
        menu.focus()

    def on_resize(self, event: events.Resize) -> None:
        self.majBanniere(event.size.width, event.size.height)

    def majBanniere(self, largeur: int, hauteur: int) -> None:
        self.query_one("#banniere", Static).update(choisirBanniere(largeur, hauteur))

    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        if event.option_id == "entree-sortie":
            self.app.push_screen(EnterExitScreen())
        elif event.option_id == "etat":
            self.app.push_screen(StatusScreen())
        elif event.option_id == "quitter":
            self.app.action_quit()


class EnterExitScreen(Screen):

    BINDINGS = [Binding("escape", "app.pop_screen", "Retour au menu")]

    def compose(self) -> ComposeResult:
        with Vertical(classes="page"):
            yield Static("Gestion des entrées et sorties", classes="titre")
            yield Static(id="places", classes="info")
            yield OptionList(
                Option("Enregistrer une entrée", id="entree"),
                Option("Enregistrer une sortie", id="sortie"),
                Option("Payer un ticket", id="payer"),
                Option("Retour au menu", id="retour"),
                id="actions",
            )
            yield Static("↑↓ naviguer · Entrée valider · Échap retour", classes="aide")

    def on_mount(self) -> None:
        self.majPlaces()
        actions = self.query_one("#actions", OptionList)
        actions.highlighted = 0
        actions.focus()

    def majPlaces(self) -> None:
        places = self.app.parking.verifCapacity()
        texte = "Parking complet" if places <= 0 else f"Places disponibles : {places}"
        self.query_one("#places", Static).update(texte)

    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        if event.option_id == "entree":
            self.entree()
        elif event.option_id == "sortie":
            self.sortie()
        elif event.option_id == "payer":
            self.payer()
        elif event.option_id == "retour":
            self.app.pop_screen()

    def afficherErreur(self, erreur: TicketErreur):
        """Ouvre la fenêtre Info ou Erreur et renvoie un awaitable."""
        titre = "Info" if erreur.info else "Erreur"
        return self.app.push_screen_wait(MessageModal(titre, str(erreur)))

    # @work : les actions tournent dans un worker pour pouvoir attendre
    # la réponse des fenêtres modales avec push_screen_wait.

    @work(exclusive=True)
    async def entree(self) -> None:
        try:
            ticketId = self.app.tickets.enter()
        except TicketErreur as erreur:
            await self.afficherErreur(erreur)
            return
        self.majPlaces()
        await self.app.push_screen_wait(
            MessageModal("Succès", f"Ticket généré avec succès\nNuméro : {ticketId}")
        )

    @work(exclusive=True)
    async def sortie(self) -> None:
        ticketId = await self.app.push_screen_wait(
            DemandeTicketModal("Numéro du ticket", "Quel est le numéro du ticket à clôturer ?")
        )
        if ticketId is None:
            return
        try:
            heure_sortie = self.app.tickets.sortie(ticketId)
        except TicketErreur as erreur:
            await self.afficherErreur(erreur)
            return
        self.majPlaces()
        await self.app.push_screen_wait(
            MessageModal(
                "Succès",
                f"Ticket {ticketId} clôturé avec succès !\nHeure de sortie : {heure_sortie}",
            )
        )

    @work(exclusive=True)
    async def payer(self) -> None:
        ticketId = await self.app.push_screen_wait(
            DemandeTicketModal("Numéro du ticket", "Quel est le numéro du ticket à payer ?")
        )
        if ticketId is None:
            return
        try:
            duree, total = self.app.tickets.calculerPaiement(ticketId)
        except TicketErreur as erreur:
            await self.afficherErreur(erreur)
            return

        confirme = await self.app.push_screen_wait(
            ConfirmationModal(
                "Confirmation",
                f"Ticket n° {ticketId}\n"
                f"Durée du stationnement : {formatDuree(duree)}\n"
                f"Montant à payer : {formatEuros(total)}\n\n"
                "Confirmer le paiement ?",
            )
        )
        if not confirme:
            await self.app.push_screen_wait(MessageModal("Info", "Paiement annulé."))
            return
        try:
            self.app.tickets.confirmerPaiement(ticketId)
        except TicketErreur as erreur:
            await self.afficherErreur(erreur)
            return
        await self.app.push_screen_wait(MessageModal("Succès", "Paiement enregistré !"))


class StatusScreen(Screen):

    INTERVALLE_RAFRAICHISSEMENT = 2  # secondes

    BINDINGS = [
        Binding("r", "rafraichir", "Rafraîchir"),
        Binding("escape", "app.pop_screen", "Retour au menu"),
    ]

    def __init__(self):
        super().__init__()
        self.dernieresLignes = None

    def compose(self) -> ComposeResult:
        with Vertical(classes="page large"):
            yield Static("État du parking", classes="titre")
            yield Static(id="places", classes="info")
            yield DataTable(id="table", cursor_type="row")
            yield Static(id="maj", classes="aide")
            yield Static("↑↓ parcourir · r rafraîchir · Échap retour", classes="aide")

    def on_mount(self) -> None:
        table = self.query_one("#table", DataTable)
        table.add_column("Référence", key="reference")
        table.add_column("Arrivée", key="arrivee")
        table.add_column("Sortie", key="sortie")
        table.add_column("Payé", key="paye")
        self.action_rafraichir()
        self.set_interval(self.INTERVALLE_RAFRAICHISSEMENT, self.action_rafraichir)
        table.focus()

    def action_rafraichir(self) -> None:
        places = self.app.parking.verifCapacity()
        if places <= 0:
            texte = "Parking complet"
        else:
            texte = f"Il reste {places} places de parking disponibles"
        self.query_one("#places", Static).update(texte)

        try:
            lignes = self.app.tickets.lister()
        except TicketErreur as erreur:
            self.notify(str(erreur), severity="error")
            return

        self.query_one("#maj", Static).update(
            f"{len(lignes)} ticket(s) — mis à jour à {datetime.now():%H:%M:%S}"
        )

        # On ne reconstruit le tableau que si les données ont changé,
        # pour ne pas faire sauter la sélection toutes les 2 secondes.
        if lignes == self.dernieresLignes:
            return
        self.dernieresLignes = lignes

        table = self.query_one("#table", DataTable)
        ligneCurseur = table.cursor_row
        table.clear()
        for ticketId, arrivee, sortie, paye in lignes:
            table.add_row(
                str(ticketId),
                arrivee,
                sortie if sortie is not None else "En cours",
                "Payé" if paye == 1 else "Pas payé",
                key=str(ticketId),
            )
        if lignes:
            table.move_cursor(row=min(ligneCurseur, len(lignes) - 1))


class TUI(App):

    TITLE = "Gestion de parking"
    CSS_PATH = "tui.tcss"
    ENABLE_COMMAND_PALETTE = False

    def __init__(self):
        super().__init__()
        self.sql = SQL()
        self.parking = Parking()
        self.tickets = TicketTUI(self.sql, self.parking)

    def get_default_screen(self) -> Screen:
        return MenuScreen()

    def start(self) -> None:
        # mouse=False : navigation uniquement au clavier
        self.run(mouse=False)

    def action_quit(self) -> None:
        self.sql.CloseSql()
        self.exit()


if __name__ == "__main__":
    TUI().start()