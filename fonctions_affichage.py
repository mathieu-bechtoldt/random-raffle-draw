import pandas as pd
import random as rd
import pygame 
import math
from constantes_affichages import *
from classe_uni import *



tickets = pd.read_excel("tickets.xlsx")
data_lots = pd.read_excel("lots.xlsx")

def tirage(index_lot):
    tickets = pd.read_excel("tickets.xlsx")
    data_lots = pd.read_excel("lots.xlsx")
    if data_lots.at[index_lot,"gagnants"]=="Personne":
        lot = data_lots.lots[index_lot]
        partenaire = data_lots.partenaire[index_lot]  
        noms = tickets.noms
        boule = tickets.test
        nombre_participants = len(noms)
        index_gagnant= rd.randint(0,nombre_participants-1)
        while boule[index_gagnant] == 0 and (index_lot in lots_cs):
            index_gagnant= rd.randint(0,nombre_participants-1)
        gagnant = tickets.noms[index_gagnant]
        prenom = tickets.prenoms[index_gagnant]
        mail = tickets.mail[index_gagnant]
        telephone = tickets.telephone[index_gagnant]
        data_lots.at[index_lot,"gagnants"] = gagnant
        data_lots.at[index_lot,"prenoms"] = prenom
        data_lots.at[index_lot,"mail"] = mail
        data_lots.at[index_lot,"telephone"] = telephone
        tickets = tickets.drop(index_gagnant)
        data_lots.to_excel("lots.xlsx",index=False)
        tickets.to_excel("tickets.xlsx",index=False)
        return str(prenom) + " " + str(gagnant)
    else:
        p = str(data_lots.at[index_lot,"prenoms"])
        n = str(data_lots.at[index_lot,"gagnants"])
        return p + " " + n

def affiche_tout(fenetre,univers,partenaire,lot,gagnant,pub,index_lot):
    fenetre.fill(blanc)
    for id in univers.population:
        x = univers.population[id]
        if isinstance(x,Flocon):
            affiche_flocon(fenetre,x)
        elif isinstance(x,Confetti):
            affiche_confetti(fenetre,x)
    affiche_banniere(fenetre)
    affiche_logo(fenetre,partenaire)
    affiche_wacs(fenetre)
    if pub :
        affiche_pub(fenetre,partenaire)
        affiche_phrase_lots(fenetre,partenaire)
        affiche_lots(fenetre,partenaire)
    else :
        affiche_gagnant(fenetre,gagnant)
        affiche_phrase_gagnant(fenetre,partenaire,lot)
        affiche_lot(fenetre,index_lot)
    pygame.display.flip()

def affiche_init(fenetre,univers):
    fenetre.fill(blanc)    
    for id in univers.population:
        x = univers.population[id]
        if isinstance(x,Flocon):
            affiche_flocon(fenetre,x)
        elif isinstance(x,Confetti):
            affiche_confetti(fenetre,x)
    #affiche_banniere(fenetre)
    affiche_affiche(fenetre)
    affiche_wacs(fenetre)
    #affiche_debut(fenetre)
    pygame.display.flip()



def affiche_debut(fenetre):
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render("Début du tirage au sort", True, bleu_fonce)
    textRect = text.get_rect()
    textRect.center = coord_pub
    fenetre.blit(text, textRect)

def affiche_phrase_gagnant(fenetre,partenaire,lot):
    font = pygame.font.Font('freesansbold.ttf', 35)
    text = font.render("L'heureux gagnant " + lot + " offert par "+ partenaire + " est " , True, rose)
    textRect = text.get_rect()
    textRect.center = coord_pub
    fenetre.blit(text, textRect)

def affiche_gagnant(fenetre,gagnant):
    font = pygame.font.Font('freesansbold.ttf', 60)
    text = font.render(gagnant , True, bleu_fonce)
    textRect = text.get_rect()
    textRect.center = coord_gagnant
    fenetre.blit(text, textRect)

def affiche_lot(fenetre,index_lot):
    image = pygame.image.load(images_lots[index_lot][0]).convert_alpha()
    l,h = image.get_size()
    f = images_lots[index_lot][1]
    y = (f*h)/l
    taille_logo = (f,y)
    image = pygame.transform.scale(image,taille_logo)
    #image.set_colorkey((255,255,255))
    fenetre.blit(image,(x_max/2-f/2,900-y-30))

def affiche_pub(fenetre,partenaire):
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render(infos_partenaires[partenaire]["pub"], True, bleu_fonce)
    #text = font.render("PUB", True, bleu_fonce)
    textRect = text.get_rect()
    textRect.center = coord_pub
    fenetre.blit(text, textRect)


def affiche_phrase_lots(fenetre,partenaire):
    font = pygame.font.Font('freesansbold.ttf', 35)
    text = font.render(infos_partenaires[partenaire]["phrases_lots"], True, rose)
    #text = font.render("Lots offerts", True, rose)
    textRect = text.get_rect()
    textRect.center = coord_pub
    fenetre.blit(text, textRect)

def affiche_lots(fenetre,partenaire):
    image = pygame.image.load(infos_partenaires[partenaire]["images_lots"]).convert_alpha()
    l,h = image.get_size()
    f = infos_partenaires[partenaire]["t_lots"]
    y = (f*h)/l
    taille_logo = (f,y)
    image = pygame.transform.scale(image,taille_logo)
    #image.set_colorkey((255,255,255))
    fenetre.blit(image,(x_max/2-f/2,900-y-50))

def affiche_flocon(fenetre,flocon):
    image = pygame.image.load("images\\flocon.jpg").convert_alpha()
    image = pygame.transform.scale(image,taille_flocon)
    #image.set_colorkey((255,255,255))
    #pygame.draw.circle(fenetre, bleu_clair,flocon.coord ,10)
    fenetre.blit(image,flocon.coord)

def affiche_confetti(fenetre,confetti):
    x,y = confetti.coord
    angle = confetti.inclinaison
    angle = math.radians(angle)
    l , h  = rd.randint(3,8), rd.randint(15,25)
    pygame.draw.line(fenetre,confetti.couleur,(x,y),(x+cos(angle)*h,y+h*sin(angle)),l)
    #surface = pygame.Surface((100,100))
    #pygame.draw.rect(surface, confetti.couleur, (50, 50, l, h))
    #surface = pygame.transform.rotate(surface, angle)
    #fenetre.blit(surface, (x,y))



def affiche_logo(fenetre,partenaire):
    image = pygame.image.load(infos_partenaires[partenaire]["logo"]).convert_alpha()
    l,h = image.get_size()
    taille_logo = (200,(200*h)/l)
    image = pygame.transform.scale(image,taille_logo)
    #image.set_colorkey((255,255,255))
    fenetre.blit(image,coord_logo)
    fenetre.blit(image,coord_logo2)


"""
def affiche_titre(fenetre):
    font = pygame.font.Font('freesansbold.ttf', 90)
    text = font.render("Tombola" , True, rose)
    textRect = text.get_rect()
    textRect.center = coord_titre
    fenetre.blit(text, textRect)

"""
def affiche_banniere(fenetre):
    image = pygame.image.load("images\\Bannière.png").convert_alpha()
    l,h = image.get_size()
    taille_logo = (600,(600*h)/l)
    l , h = taille_logo
    image = pygame.transform.scale(image,taille_logo)
    fenetre.blit(image,(x_max/2-l/2,10))



def affiche_wacs(fenetre):
    image = pygame.image.load("images\\wacs2.jpeg").convert_alpha()
    fenetre.blit(image,(60,y_max-250))
    fenetre.blit(image,(x_max-250,y_max-250))

def affiche_affiche(fenetre):
    image = pygame.image.load("images\\affiche.jpg").convert_alpha()
    l,h = image.get_size()
    taille_logo = (635,(635*h)/l)
    l , h = taille_logo
    image = pygame.transform.scale(image,taille_logo)
    fenetre.blit(image,(x_max/2-l/2,0))