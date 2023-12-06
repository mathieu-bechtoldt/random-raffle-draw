import random as rd
from math import sin,cos
import math
couleurs_bis = [(237,61,102),(97,228,243),(13,31,126)]

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
        i = 0
        for k in range(n):
            while i in self.population:
                i +=1
            x = rd.randint(20,self.x_max-20)
            flocon = Flocon((x,20))
            self.population[i]=flocon
    def neige(self):
        cimetiere = []
        for id in self.population:
            x = self.population[id]
            if isinstance(x,Flocon):
                if not x.tomber():
                    cimetiere.append(id)
        for i in cimetiere:
            self.population.pop(i)

    def generate_confettis(self,coord):
        direction = rd.randint(0,360)
        inclinaison = rd.randint(0,360)
        vie = rd.randint(8,25)
        couleur = couleurs_bis[rd.randint(0,2)]
        return Confetti(coord,couleur,direction,inclinaison,vie)

    def explosion(self,coord,n,h,l):
        i = 0
        if self.heure %2 == 0:
            for k in range(n):
                while i in self.population:
                    i +=1
                x,y = coord
                x1 = rd.randint(x-l,x+l)
                y1 = rd.randint(y-h,y+h)
                conf = self.generate_confettis((x1,y1))
                self.population[i] = conf
            return True
        else:
            return False

    def deplacement_conf(self):
        cimetiere = []
        for id in self.population:
            x = self.population[id]
            if isinstance(x,Confetti):
                if not x.deplacement():
                    cimetiere.append(id)
        for i in cimetiere:
            self.population.pop(i)

    def generation(self):
        self.heure = self.heure +1
        if self.heure%3==0:
            self.generate_flocon(5)
        self.deplacement_conf()
        self.neige()

class Confetti:
    def __init__(self,coord,couleur,direction,inclinaison,vie):
        self.coord = coord
        self.couleur = couleur
        self.vie = vie
        self.direction = direction
        self.inclinaison = inclinaison
        self.vitesse = 10
    def decompte(self):
        self.vie -=1
    def deplacement(self):
        self.decompte()
        if self.vie ==0 :
            return False
        else:
            x,y = self.coord
            dir = math.radians(self.direction)
            x1 = x + cos(dir)*self.vitesse
            y1 = y + sin(dir)*self.vitesse
            self.coord = x1,y1
            return True
    

