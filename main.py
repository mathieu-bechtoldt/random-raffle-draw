import pygame 
from pygame.locals import *
import pandas as pd
from fonctions_affichage import *
from classe_uni import *

data_lots = pd.read_excel("lots.xlsx")
lots = data_lots.lots
nombre_lots = len(images_lots)
x_max = 1440
y_max = 900

uni = Univers({},0)
pygame.init() 
info = pygame.display.Info()
fenetre = pygame.display.set_mode((x_max, y_max))
continuer = True
confettis = 0
pub = True
affichage_pub = False
index_lot = 0
index_partenaire=-1
lot = "gourde"
decompte_lots = 0

clock = pygame.time.Clock() 
gagnant = "snow"

while continuer :
    for event in pygame.event.get():
        if event.type== QUIT:
            continuer = False
        
        elif event.type == KEYDOWN and event.key == K_SPACE and not pub:
            index_lot = index_lot +1
            partenaire = ordre[index_partenaire]
            lot = lots[index_lot]
            decompte_lots -=1
            #uni.explosion(coord_gagnant,50)
            confettis = 5
            gagnant = tirage(index_lot)
            
            affichage_pub = False

            if decompte_lots==0:
                pub = True
            
        elif event.type == KEYDOWN and event.key == K_SPACE and pub:
            index_partenaire +=1
            partenaire = ordre[index_partenaire]
            decompte_lots = infos_partenaires[partenaire]["nombre_lots"]
            affichage_pub = True
            pub = False

        elif event.type == KEYDOWN and event.key == K_LEFT :
            if pub :
                pub = False
                index_lot-=1
                if infos_partenaires[partenaire]["nombre_lots"]>1:
                    gagnant = tirage(index_lot)
                    lot = lots[index_lot]
                    affichage_pub = False
                    decompte_lots+=1
                else:
                    affichage_pub = True
                    gagnant = tirage(index_lot)
                    lot = lots[index_lot]
                    decompte_lots+=1
            else:
                n = infos_partenaires[partenaire]["nombre_lots"]
                if affichage_pub :
                    index_partenaire-=1
                    pub = True
                    affichage_pub = False
                    partenaire = ordre[index_partenaire]
                    decompte_lots = 0
                
                elif (n-decompte_lots)==1:
                    index_lot -=1
                    decompte_lots+=1
                    affichage_pub = True
                    lot = lots[index_lot]
                    gagnant = tirage(index_lot)
                else :
                    index_lot -=1
                    lot = lots[index_lot]
                    gagnant = tirage(index_lot)
                    decompte_lots +=1
                    affichage_pub = False


    if index_partenaire == -1:
        uni.generation()
        affiche_init(fenetre,uni)
    else:
        uni.generation()
        if confettis >0:
            if uni.explosion(coord_gagnant,20,20,50):
                confettis -=1
        affiche_tout(fenetre,uni,partenaire,lot,gagnant,affichage_pub,index_lot)
    clock.tick(10)


    
            
            


 