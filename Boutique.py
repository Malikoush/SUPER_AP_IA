from Animal import Animal
from data import MOCK_ANIMAUX, MOCK_NOURRITURE
import random
from Partie import Partie

class Boutique:
  def __init__(self):
   self.animaux = [None] * 5
   self.nourriture = [None] * 2
   self.rang_boutique =1

 
  #tour impaire augmentation de rang des animaux

  #tour 5 augmentation place nourriture+1 boutique +1 animal
  #tour9 augmentation place boutique +1 animal
   
  def raffraichir(self):
    
    animaux_filtrés = [a for a in MOCK_ANIMAUX if not a.rang > self.rang_boutique]
    nourriture_filtrée = [n for n in MOCK_NOURRITURE if not n.rang > self.rang_boutique]

    nb_animaux, nb_nourriture = self.calculer_emplacements()

    choix_animaux = random.choices(animaux_filtrés, k=nb_animaux)
    choix_nourriture = random.choices(nourriture_filtrée, k=nb_nourriture)
    self.animaux = [a.clone() for a in choix_animaux]
    self.nourriture = [n.clone() for n in choix_nourriture]
    print("La boutique a été rafraîchie.")
    self.afficher_animaux()
    self.afficher_nourriture()
        
  def calculer_emplacements(self):
    
    nb_animaux = 3
    nb_nourriture = 1
    if self.rang_boutique >= 3:
        nb_animaux += 1
        nb_nourriture += 1
    if self.rang_boutique >= 5:
        nb_animaux += 1
    return nb_animaux, nb_nourriture
   
  def afficher_animaux(self):
        if not self.animaux:
            print("La boutique est vide.")
        else:
            print("Animaux disponibles dans la boutique:")
            for animal in self.animaux:
                print(f"Nom: {animal.nom}, Dégâts: {animal.degats}, Santé: {animal.santé}, Capacité: {animal.capacité.nom}")

  def afficher_nourriture(self):
        if not self.nourriture:
            print("Aucune nourriture disponible.")
        else:
            print("Nourriture disponible:")
            for nourriture in self.nourriture:
              print(f"Nom: {nourriture.nom}, Description: {nourriture.description}, Prix: {nourriture.prix} or, Rang: {nourriture.rang}")


  def retirer_animal(self, index):
        if index < 0 or index >= len(self.animaux):
          print("Position invalide.")
            
        animal = self.animaux[index]
        self.animaux[index] = None
        return animal
  def retirer_nourriture(self, index):
        if index < 0 or index >= len(self.nourriture):
          print("Position invalide.")
            
        nourriture = self.nourriture[index]
        self.nourriture[index] = None
        return nourriture



  def geler(self,animal):
    pass
