import Capacité
from Evenements import Evenement


class Animal:
  compteur_id = 0  # identifiant global

  def __init__(self, nom, degats, santé, capacité,experience, niveau, rang):
        self.nom = nom
        self.degats = degats
        self.santé = santé
        self.capacité = capacité
        self.experience = experience
        self.niveau = niveau
        self.rang = rang
        self.atout = None

        Animal.compteur_id += 1
        self.id = Animal.compteur_id  # identifiant unique

  def clone(self):
        copie = Animal(self.nom, self.degats, self.santé, self.capacité,self.experience, self.niveau, self.rang)
        return copie

  def attaque(self,cible):
     print(f"{self.nom} attaque {cible.nom} est lui fait {self.degats} degats.")
     cible.subit(self.degats)
  
  def subit(self, degats):
    self.santé= max(0, self.santé - degats)
    
  def gagne_experience(self,from_animal):
    self.experience += from_animal.experience
    self.degats += 1
    self.santé += 1
    print(f"{self.nom} gagne de l'expérience il a {self.experience} experience!")
    if self.experience == 3:
        self.evolue()
        print(f"{self.nom} a été promu au niveau {self.niveau} !")
    if self.experience == 6:
        self.evolue()
        print(f"{self.nom} a été promu au niveau {self.niveau} !")

  def evolue(self):
    self.niveau += 1

  def meur(self, equipe):
    index = equipe.index(self)
    equipe[index] = None
    print(f"{self.nom} est mort !")
    if  self.capacité.trigger == Evenement.MORT:
            self.capacité.activer(animal=self, position=index, equipe=equipe)
            if self.atout.trigger == Evenement.MORT:
              self.atout.activer(position=index, equipe=equipe)
