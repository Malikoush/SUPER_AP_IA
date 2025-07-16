class Combat:
    def __init__(self,joueur1,joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2

    def commencer(self):
        print(f"Début du combat entre {self.joueur1.nom} et {self.joueur2.nom} !")

        # Copie locale des animaux (pour le combat uniquement)
        equipe1 = [a.clone() for a in self.joueur1.animaux if a is not None]
        equipe2 = [a.clone() for a in self.joueur2.animaux if a is not None]

        index1 = 0
        index2 = 0

        while index1 < len(equipe1) and index2 < len(equipe2):
            animal1 = equipe1[index1]
            animal2 = equipe2[index2]

            print(f"{animal1.nom} (Santé: {animal1.santé}) attaque {animal2.nom} (Santé: {animal2.santé})")

            animal1.subit(animal2.degats)
            animal2.subit(animal1.degats)

            print(f"{animal1.nom} subit {animal2.degats} dégâts.")
            print(f"{animal2.nom} subit {animal1.degats} dégâts.")

            if animal1.santé <= 0:
                #equipe1[animal1] = None
                animal1.meur(equipe1)
                index1 += 1
            if animal2.santé <= 0:
                #equipe2[animal2] = None
                animal2.meur(equipe2)
                index2 += 1

        # Résultat final
        if index1 < len(equipe1) and index2 >= len(equipe2):
            print(f"{self.joueur1.nom} a gagné le combat !")
            self.joueur1.victoire()
            self.joueur2.defaite()
        elif index2 < len(equipe2) and index1 >= len(equipe1):
            print(f"{self.joueur2.nom} a gagné le combat !")
            self.joueur2.victoire()
            self.joueur1.defaite()
        else:
            print("Match nul, les deux joueurs n'ont plus d'animaux.")

