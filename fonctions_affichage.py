import pandas as pd
import random as rd
import pygame 

logo = {"WACS": "images\\wacs.png",
        "BDA":"images\\bda.png",
        "FIR":"images\\fir.png",
        "Oliver Wyman" :"images\\oliver.png",
        "Impact": "images\\impact.png",
        "JCS" : "images\\jcs.png",
        "RAID": "images\\raid.png",
        "Viarezo" : "images\\viarezo.png",
        "BDE" : "images\\bde.jpeg",
        "BDS" : "images\\bds.png",
        "Commu's" : "images\\commus.jpg",
        "PICS" : "images\\pics.jpeg"
        }


#taille_logo = (100,100)
x_max = 1440
y_max = 900
coord_logo = (50,200)
coord_logo2 = (x_max-250,200)
coord_phrase = (x_max/2,y_max/2)
coord_titre = (x_max/2,100)
blanc = (255,255,255)
noir = (0,0,0)
rose = (237,61,102)
bleu_clair = (97,228,243)
bleu_fonce = (13,31,126)

def tirage(index_lot):
    participants = pd.read_excel("participants.xlsx")
    data_lots = pd.read_excel("lots.xlsx")
    lot = data_lots.lots[index_lot]
    partenaire = data_lots.partenaire[index_lot]  
    noms = participants.noms
    nombre_participants = len(noms)
    index_gagnant= rd.randint(0,nombre_participants-1)
    gagnant = participants.noms[index_gagnant]
    data_lots.at[index_lot,"gagnants"] = gagnant
    participants = participants.drop(index_gagnant)
    #data_lots.to_excel("lots.xlsx",index=False)
    #participants.to_excel("participants.xlsx",index=False)
    return partenaire,lot,gagnant

def affiche_tout(fenetre,partenaire,lot,gagnant):
    fenetre.fill(blanc)
    affiche_titre(fenetre)
    affiche_logo(fenetre,partenaire)
    affiche_gagnant(fenetre,partenaire,lot,gagnant)
    affiche_wacs(fenetre)
    pygame.display.flip()


def affiche_logo(fenetre,partenaire):
    image = pygame.image.load(logo[partenaire]).convert_alpha()
    l,h = image.get_size()
    taille_logo = (200,(200*h)/l)
    image = pygame.transform.scale(image,taille_logo)
    #image.set_colorkey((255,255,255))
    fenetre.blit(image,coord_logo)
    fenetre.blit(image,coord_logo2)


def affiche_gagnant(fenetre,partenaire,lot,gagnant):
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render("L'heureux gagnant " + lot + " offert par "+ partenaire + " est " + gagnant , True, rose)
    textRect = text.get_rect()
    textRect.center = coord_phrase
    fenetre.blit(text, textRect)

def affiche_titre(fenetre):
    font = pygame.font.Font('freesansbold.ttf', 90)
    text = font.render("Tombola" , True, rose)
    textRect = text.get_rect()
    textRect.center = coord_titre
    fenetre.blit(text, textRect)

def affiche_wacs(fenetre):
    image = pygame.image.load("images\\wacs2.jpeg").convert_alpha()
    fenetre.blit(image,(10,y_max-200))
    fenetre.blit(image,(x_max-200,y_max-200))

