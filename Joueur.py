from Boutique import Boutique
from Evenements import Evenement
import Utils

class Joueur:
  def __init__(self,nom) :
    self.gold= 10
    self.vie = 5
    self.trophée = 0
    self.nom = nom
    self.animaux = [None] * 5 
    self.boutique = Boutique()
    self.adversaire = None 


  def peut_payer(self, prix):
        return self.gold >= prix 

  def payer(self, montant):
    if self.peut_payer(montant):
        self.gold -= montant
        return True
    return False

  def acheter(self, boutique, from_index, to_index):
        prix = 3  # prix fixe ou dynamique
        # Vérification : from_index doit être valide dans la boutique
        if from_index >= len(boutique.animaux):
          print("Indice de boutique invalide.")
          return False

        # Vérification : to_index doit être valide dans self.animaux
        if to_index < 0 or to_index >= len(self.animaux):
          print("Position d'ajout invalide.")
          return False

        if self.animaux[to_index] is not None and self.animaux[to_index].nom == boutique.animaux[from_index].nom:
          self.animaux[to_index].gagne_experience(boutique.animaux[from_index])
          animal = boutique.animaux[from_index]
          boutique.retirer_animal(from_index)
          self.payer(prix)
          print(f"{self.nom} a acheté {animal.nom} pour {prix} gold.")
          return True
        
        if self.animaux[to_index] is not None:
          print("Position de destination déjà occupée.")
          return False

        
        if not self.peut_payer(prix):
          print(f"{self.nom} n'a pas assez d'or pour acheter.")
          return False

        animal = boutique.animaux[from_index]
        boutique.retirer_animal(from_index)
        self.payer(prix)
        self.ajouter_animal(animal,to_index)
        if animal.capacité and animal.capacité.trigger == Evenement.ACHAT:
          index = animal.joueur.animaux.index(animal)
          animal.capacité.activer(animal=animal, position=index, equipe=animal.joueur.animaux)
        print(f"{self.nom} a acheté {animal.nom} pour {prix} gold.")
        return True
  
  def acheter_nourriture(self, boutique, from_index, cible=None):
      if not 0 <= from_index < len(boutique.nourriture):
          print("Indice de nourriture invalide.")
          return False

      nourriture = boutique.nourriture[from_index]

      if not self.peut_payer(nourriture.prix):
          print(f"{self.nom} n'a pas assez d'or pour acheter {nourriture.nom}.")
          return False

      self.payer(nourriture.prix)

      try:
          if nourriture.requiert_cible:
              if cible is None:
                  print(f"{nourriture.nom} nécessite une cible.")
                  return False

              if isinstance(cible, int):
                  animal = self.animaux[cible]
                  if animal is None:
                      print("Aucun animal à cette position.")
                      return False
                  nourriture.utiliser(cible=animal)

              elif isinstance(cible, list):
                  nourriture.utiliser(equipe=cible)

              elif isinstance(cible, Boutique):
                  nourriture.utiliser(boutique=cible)

              else:
                  print("Type de cible non pris en charge.")
                  return False
          else:
              # Nourriture autonome : elle s’utilise sans argument
              nourriture.utiliser()
      except Exception as e:
          print(f"Erreur lors de l'utilisation de la nourriture : {e}")
          return False

      boutique.retirer_nourriture(from_index)
      print(f"{self.nom} a utilisé {nourriture.nom}.")
      return True
    

  def ajouter_animal(self, animal, position):
    animal.joueur = self
    return Utils.invoquer_animal(self.animaux, animal, position)
    

  def retirer_animal(self, position):
    if position < 0 or position >= len(self.animaux):
        print("Position invalide.")
        return None
    animal = self.animaux[position]
    self.animaux[position] = None
    return animal  
  
  def deplacer_animal(self, from_index, to_index):
    if not (0 <= from_index < len(self.animaux)) or not (0 <= to_index < len(self.animaux)):
        print("Position invalide.")
        return False
    if self.animaux[from_index] is None:
        print("Pas d'animal à déplacer.")
        return False
    if self.animaux[to_index] is not None and self.animaux[to_index].nom == self.animaux[from_index].nom:
        self.animaux[to_index].gagne_experience(self.animaux[from_index])
        self.animaux[from_index] = None
        return True
    if self.animaux[to_index] is not None:
        print("Position de destination déjà occupée.")
        return False
    self.animaux[to_index] = self.animaux[from_index]
    self.animaux[from_index] = None
    return True
 
  def vendre(self,index):

    if 0 <= index < len(self.animaux):
        animal = self.animaux[index]
        if animal.capacité and animal.capacité.trigger == Evenement.VENTE:
          index = animal.joueur.animaux.index(animal)
          animal.capacité.activer(animal=animal, position=index, equipe=animal.joueur.animaux)

        self.retirer_animal(index)
        self.gold += animal.niveau  
       
        print(f"{self.nom} a vendu {animal.nom} pour {animal.niveau} gold.")
    else:
        print("Indice invalide.")

  def defaite(self):
        self.vie -= 1
  def victoire(self):
        self.trophée += 1

  def deplacer():
    pass
  
  def finir_tour(self):
    return True