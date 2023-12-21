import pandas as pd
import random as rd
from constantes_affichages import *
from classe_uni import *


data_lots = pd.read_excel("lots.xlsx")
participants = pd.read_excel("participants.xlsx")
Nom = participants.Nom
Prenom = participants.Prénom
Mail = participants["Adresse email"]
Telephone = participants["Numéro de téléphone"]
montants = participants["Montant"]


def compte_tickets():
    noms = []
    prenoms = []
    mails = []
    telephone = []
    tickets = {}
    for i in range(len(montants)):
        prix = montants[i]
        if prix == 1.5:
            noms.append(Nom[i])
            prenoms.append(Prenom[i])
            mails.append(Mail[i])
            telephone.append(Telephone[i])
        elif prix == 5:
            for knecht in range(5):
                noms.append(Nom[i])
                prenoms.append(Prenom[i])
                mails.append(Mail[i])
                telephone.append(Telephone[i])
        elif prix == 3:
            for knecht in range(2):
                noms.append(Nom[i])
                prenoms.append(Prenom[i])
                mails.append(Mail[i])
                telephone.append(Telephone[i])
        else:
            prix = int(prix)
            for knecht in range((prix%10)*15):
                noms.append(Nom[i])
                prenoms.append(Prenom[i])
                mails.append(Mail[i])
                telephone.append(Telephone[i])
        tickets["noms"] = noms
        tickets["prenoms"] = prenoms
        tickets["mail"] = mails
        tickets["telephone"] = telephone
        data_tickets = pd.DataFrame(tickets)
        data_tickets.to_excel("tickets.xlsx",index=False)

compte_tickets()




