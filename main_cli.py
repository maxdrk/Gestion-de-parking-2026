import cli.tickets.main as ticket
import cli.payment.main as payment


try:
    while True:
        
        choix = int(input("Que voulez-vous faire \n1. Entrer/sortir\n2. Payer\n0. Quitter le programme \nchoix: "))
        if choix == 1:
            ticket.init()
        elif choix == 2:
            payment.init()
        elif choix == 0:
            break
        else:
            print("Erreur veuillez choisir une proposition valable")

except:
    print("Erreur veuillez choisir une proposition valable")            
finally:
    ticket.close()
