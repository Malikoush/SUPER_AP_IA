from Combat import Combat

class Partie:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.tour = 1

    def lancer(self):
        while  self.joueur1.vie > 0 and self.joueur2.vie > 0:
            print(f"\n=== Tour {self.tour} ===\n")
            self.phase_achat(self.joueur1)
            self.phase_achat(self.joueur2)


            self.phase_combat()

            self.tour += 1
            self.joueur1.boutique.rang_boutique = min(6, (self.tour + 1) // 2)
            self.joueur2.boutique.rang_boutique = min(6, (self.tour + 1) // 2)

        
        self.fin_de_partie()

    def phase_achat(self, joueur):
        print(f"\n--- Phase d'achat pour {joueur.nom} ---")
        joueur.gold = 10
        joueur.boutique.raffraichir()

        while joueur.peut_payer(3) and joueur.boutique.animaux:
            animal_boutique = joueur.boutique.animaux[0]

            # Vérifie que l'animal de la boutique n'est pas vide
            if animal_boutique is None:
                print("Premier slot de la boutique vide.")
                break
            if not any(animal is None or (animal is not None and animal.nom == animal_boutique.nom) for animal in joueur.animaux):
                break

            print(f"\n{joueur.nom} | Or restant : {joueur.gold}")
            print("État de l'équipe :")
            for i, animal in enumerate(joueur.animaux):
                print(f"  Position {i}: {'Vide' if animal is None else f'{animal.nom} (Exp : {animal.experience} | Niv: {animal.niveau})'}")

            # Cherche une position pour poser ou fusionner
            position_cible = None
            for i, animal in enumerate(joueur.animaux):
                if animal is None or animal.nom == animal_boutique.nom:
                    print(f"animal : {animal.nom if animal is not None else 'Vide'} animal_boutique : {animal_boutique.nom}  ")
                    position_cible = i
                    break

            if position_cible is not None:
                joueur.acheter(joueur.boutique, 0, position_cible)
            else:
                print("Aucune position disponible pour poser ou fusionner cet animal.")
                break

    def phase_combat(self):
        print("\n--- Phase de combat ---")
        combat = Combat(self.joueur1, self.joueur2)
        combat.commencer()
        

    def fin_de_partie(self):
        print("\n=== Fin de la partie ===")
        if self.joueur1.vie <= 0 and self.joueur2.vie <= 0:
            print("Match nul.")
        elif self.joueur1.vie <= 0:
            print(f"{self.joueur2.nom} remporte la partie ! en {self.tour} tours")
        elif self.joueur2.vie <= 0:
            print(f"{self.joueur1.nom} remporte la partie ! en {self.tour} tours")
        else:
            print("Partie terminée sans vainqueur (limite de tours atteinte).")
