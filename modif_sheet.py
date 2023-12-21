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
test = participants["Tu es..."]


def compte_tickets():
    noms = []
    prenoms = []
    mails = []
    telephone = []
    b =[]
    tickets = {}
    for i in range(len(montants)):
        prix = montants[i]
        if test[i] == "En 1A/2A à CS": 
            boule = 1
        else :
            boule = 0
        if prix == 1.5:
            noms.append(Nom[i])
            prenoms.append(Prenom[i])
            mails.append(Mail[i])
            telephone.append(Telephone[i])
            b.append(boule)
        elif prix == 5:
            for knecht in range(5):
                noms.append(Nom[i])
                prenoms.append(Prenom[i])
                mails.append(Mail[i])
                telephone.append(Telephone[i])
                b.append(boule)
        elif prix == 3:
            for knecht in range(2):
                noms.append(Nom[i])
                prenoms.append(Prenom[i])
                mails.append(Mail[i])
                telephone.append(Telephone[i])
                b.append(boule)
        else:
            prix = int(prix)
            for knecht in range((prix//10)*15):
                noms.append(Nom[i])
                prenoms.append(Prenom[i])
                mails.append(Mail[i])
                telephone.append(Telephone[i])
                b.append(boule)
        tickets["noms"] = noms
        tickets["prenoms"] = prenoms
        tickets["mail"] = mails
        tickets["telephone"] = telephone
        tickets["test"] = b
        data_tickets = pd.DataFrame(tickets)
        data_tickets.to_excel("tickets.xlsx",index=False)

compte_tickets()




