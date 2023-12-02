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
action = True
pub = True
tirage = False
index_lot = -1
index_partenaire=-1
lot = ""
decompte_lots = 0
fenetre.fill(blanc)
affiche_titre(fenetre)
affiche_wacs(fenetre)
pygame.display.flip()
clock = pygame.time.Clock() 
gagnant = "snow"

while continuer and index_lot<nombre_lots:
    for event in pygame.event.get():
        if event.type== QUIT:
            continuer = False
        
        elif event.type == KEYDOWN and event.key == K_SPACE and action and not pub and tirage:
            index_lot = index_lot +1
            partenaire = data_lots.partenaire[index_lot]
            decompte_lots = infos_partenaires[partenaire]["nombre_lots"] -1
            lot = lots[index_lot]
            gagnant = tirage(index_lot)
            affiche_tout(fenetre,uni,partenaire,lot,gagnant,pub)
            if decompte_lots==0:
                tirage = False
            action= not action

        elif event.type == KEYDOWN and event.key == K_SPACE and action and pub:
            index_partenaire +=1
            partenaire = ordre[index_partenaire]
            affiche_tout(fenetre,uni,partenaire,lot,gagnant,pub)
            action = not action

        elif event.type == KEYDOWN and event.key == K_SPACE and not action and tirage:
            action = not action
        
        elif event.type == KEYDOWN and event.key == K_SPACE and not action:


        elif index_partenaire == -1:
            affiche_init(fenetre,uni)

        else: 
            affiche_tout(fenetre,uni,partenaire,lot,gagnant,pub)
    clock.tick(15)


    
            
            


 