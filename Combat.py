from Evenements import Evenement
import random

class Combat:
    def __init__(self,joueur1,joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2

    def commencer(self):
        print(f"Début du combat entre {self.joueur1.nom} et {self.joueur2.nom} !")
        
          
        # Copie locale des animaux (pour le combat uniquement)
        equipe1 = [a.clone() for a in self.joueur1.animaux if a is not None]
        equipe2 = [a.clone() for a in self.joueur2.animaux if a is not None]
    

        self.activer_debut_combat(equipe1, equipe2)
        index1 = 0
        index2 = 0

        while index1 < len(equipe1) and index2 < len(equipe2):
              # Sauter animaux morts (None)
            while index1 < len(equipe1) and equipe1[index1] is None:
                index1 += 1
            while index2 < len(equipe2) and equipe2[index2] is None:
                index2 += 1

            # Vérifier si fin de combat (plus d’animaux)
            if index1 >= len(equipe1) or index2 >= len(equipe2):
                break
            animal1 = equipe1[index1]
            animal2 = equipe2[index2]

            print(f"{animal1.nom} (Santé: {animal1.santé}) attaque {animal2.nom} (Santé: {animal2.santé})")

            animal1.subit(animal2.degats)
            animal2.subit(animal1.degats)

            print(f"{animal1.nom} subit {animal2.degats} dégâts.")
            print(f"{animal2.nom} subit {animal1.degats} dégâts.")

            if animal1.santé <= 0:
                mort_index = index1
                animal1.meur_combat(equipe1)
                if equipe1[mort_index] is None:
                    index1 += 1

            if animal2.santé <= 0:
                mort_index = index2
                animal2.meur_combat(equipe2)
                if equipe2[mort_index] is None:
                    index2 += 1

        # Résultat final
        if index1 < len(equipe1) and index2 >= len(equipe2):
            print(f"{self.joueur1.nom} a gagné le combat !")
            self.joueur1.victoire()
            self.joueur2.defaite()
            for a in equipe1:
                if a != None :
                    print(f"{a.nom}")
        elif index2 < len(equipe2) and index1 >= len(equipe1):
            print(f"{self.joueur2.nom} a gagné le combat !")
            self.joueur2.victoire()
            self.joueur1.defaite()
            for a in equipe2:
                if a != None :
                    print(f"{a.nom}")
        else:
            print("Match nul, les deux joueurs n'ont plus d'animaux.")

    def activer_debut_combat(self,equipe1, equipe2):
            activations = []

            # Collecter toutes les capacités de début de combat
            for i, animal in enumerate(equipe1):
                if animal.capacité and animal.capacité.trigger == Evenement.DEBUT_COMBAT:
                    activations.append((animal, i, equipe1, equipe2))

            for i, animal in enumerate(equipe2):
                if animal.capacité and animal.capacité.trigger == Evenement.DEBUT_COMBAT:
                    activations.append((animal, i, equipe2, equipe1))
            random.shuffle(activations)
            # Exécuter les activations **après** avoir tout collecté
            for animal, pos, equipe, equipe_enemie in activations:
                animal.capacité.activer(animal=animal, position=pos, equipe=equipe, equipe_enemie=equipe_enemie)
