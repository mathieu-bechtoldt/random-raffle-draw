import pygame 
from pygame.locals import *
import pandas as pd
from fonctions_affichage import *
from classe_uni import *

data_lots = pd.read_excel("lots.xlsx")
lots = data_lots.lots
nombre_lots = len(lots)
x_max = 1440
y_max = 900

uni = Univers([],0)
pygame.init()
info = pygame.display.Info()
fenetre = pygame.display.set_mode((x_max, y_max))
continuer = True
statut = True
index_lot = 0
fenetre.fill(blanc)
affiche_titre(fenetre)
affiche_wacs(fenetre)
pygame.display.flip()

while continuer and index_lot<nombre_lots:
    for event in pygame.event.get():
        if event.type== QUIT:
            continuer = False
        elif event.type == KEYDOWN and event.key == K_SPACE and statut:
            lot = lots[index_lot]
            partenaire = data_lots.partenaire[index_lot]
            gagnant = tirage(index_lot)
            affiche_tout_gagnant(fenetre,uni,partenaire,lot,gagnant)
            index_lot = index_lot +1
        else:
            partenaire = data_lots.partenaire[index_lot] 
            affiche_tout(fenetre,uni,partenaire)


    
            
            


 