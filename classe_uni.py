import random as rd

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
            flocon = self.population[i]
            if not flocon.tomber():
                cimetiere.append(i)
        for i in cimetiere:
            self.population.pop(i)

    def generation(self):
        self.heure = self.heure +1
        if self.heure%3==0:
            self.generate_flocon(5)
        self.neige()

