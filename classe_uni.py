import random as rd
from math import sin,cos
couleurs_bis = [(254,6,12),(6,156,51),(13,63,172)]

class Flocon:
    def __init__(self,coord):
        self.coord = coord
        self.vitesse = 20
    def tomber(self):
        x , y = self.coord
        if y+self.vitesse <880:
            self.coord = (x, y+self.vitesse)
            return True
        return False



class Univers:
    def __init__(self,population,heure):
        self.population = population
        self.heure =heure
        self.x_max = 1400
        self.y_max = 900
    def generate_flocon(self,n):
        for i in range(n):
            x = rd.randint(20,self.x_max-20)
            flocon = Flocon((x,20))
            self.population.append(flocon)
    def neige(self):
        cimetiere = []
        for i in range(len(self.population)):
            if isinstance(self.population[i],Flocon):
                flocon = self.population[i]
                if not flocon.tomber():
                    cimetiere.append(i)
        for i in cimetiere:
            self.population.pop(i)

    def generate_confettis(self,coord):
        direction = rd.randint(0,360)
        couleur = couleurs_bis[rd.randint(0,2)]
        return Confetti(coord,couleur,direction)

    def explosion(self,coord,n):
        for i in range(n):
            conf = self.generate_confettis(coord)
            self.population.append(conf)

    def deplacement_conf(self):
        cimetiere = []
        for i in range(len(self.population)):
            if isinstance(self.population[i],Confetti):
                conf = self.population[i]
                if not conf.deplacement():
                    cimetiere.append(i)
        for i in cimetiere:
            self.population.pop(i)

    def generation(self):
        self.heure = self.heure +1
        if self.heure%3==0:
            self.generate_flocon(5)
        self.deplacement_conf()
        self.neige()

class Confetti:
    def __init__(self,coord,couleur,direction):
        self.coord = coord
        self.couleur = couleur
        self.vie = 15
        self.direction = direction
        self.vitesse = 10
    def decompte(self):
        self.vie -=1
    def deplacement(self):
        self.decompte()
        if self.vie ==0 :
            return False
        else:
            x,y = self.coord
            x1 = x + cos(self.direction)*self.vitesse
            y1 = y + sin(self.direction)*self.vitesse
            self.coord = x1,y1
            return True
    

