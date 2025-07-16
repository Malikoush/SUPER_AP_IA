from Animal import Animal
from data import MOCK_ANIMAUX, MOCK_NOURRITURE
import random


class Boutique:
  def __init__(self):
   self.animaux = [None] * 5
   self.nourriture = [None] * 2


  
  def raffraichir(self):
    
    animaux_filtrés = [a for a in MOCK_ANIMAUX if not a.rang > 1]
    nourriture_filtrée = [n for n in MOCK_NOURRITURE if not n.rang > 1]
    choix_animaux = random.choices(animaux_filtrés, k=3)
    choix_nourriture = random.choices(nourriture_filtrée, k=2)
    self.animaux = [a.clone() for a in choix_animaux]
    self.nourriture = [n.clone() for n in choix_nourriture]
    print("La boutique a été rafraîchie.")
    self.afficher_animaux()
    self.afficher_nourriture()
        
    
  def afficher_animaux(self):
        if not self.animaux:
            print("La boutique est vide.")
        else:
            print("Animaux disponibles dans la boutique:")
            for animal in self.animaux:
                print(f"Nom: {animal.nom}, Dégâts: {animal.degats}, Santé: {animal.santé}, Capacité: {animal.capacité}")

  def afficher_nourriture(self):
        if not self.nourriture:
            print("Aucune nourriture disponible.")
        else:
            print("Nourriture disponible:")
            for nourriture in MOCK_NOURRITURE:
              print(f"Nom: {nourriture.nom}, Description: {nourriture.description}, Prix: {nourriture.prix} or, Rang: {nourriture.rang}")


  def retirer_animal(self, index):
        if index < 0 or index >= len(self.animaux):
          print("Position invalide.")
            
        animal = self.animaux[index]
        self.animaux[index] = None
        return animal



  def geler(self,animal):
    pass
