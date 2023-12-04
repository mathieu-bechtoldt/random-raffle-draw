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
pub = True
affichage_pub = False
index_lot = 0
index_partenaire=-1
lot = "gourde"
decompte_lots = 0

clock = pygame.time.Clock() 
gagnant = "snow"

while continuer and index_lot<nombre_lots:
    for event in pygame.event.get():
        if event.type== QUIT:
            continuer = False
        
        elif event.type == KEYDOWN and event.key == K_SPACE and not pub:
            index_lot = index_lot +1
            partenaire = ordre[index_partenaire]
            lot = lots[index_lot]
            decompte_lots -=1
            gagnant = tirage(index_lot)
            affichage_pub = False
            if decompte_lots==0:
                pub = True
            
            

        elif event.type == KEYDOWN and event.key == K_SPACE and pub:
            index_partenaire +=1
            partenaire = ordre[index_partenaire]
            decompte_lots = infos_partenaires[partenaire]["nombre_lots"]
            affichage_pub = True
            pub = not pub
        
    if index_partenaire == -1:
        affiche_init(fenetre,uni)
    else:
        affiche_tout(fenetre,uni,partenaire,lot,gagnant,affichage_pub)
    clock.tick(10)


    
            
            


 