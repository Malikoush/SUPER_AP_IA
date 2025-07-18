from Animal import Animal
from Boutique import Boutique
import Joueur
import data


def test_acheter_nourriture():
    print("\n=== Test : Achat de nourriture ===")

    # Préparation
    joueur = Joueur.Joueur("Alice")
    boutique = joueur.boutique

    # On donne un animal au joueur
    animal = Animal("TestAnimal", 2, 2, None, 1, 1, 1)
    joueur.ajouter_animal(animal, 0)

    boutique.raffraichir() 
   

    # Vérification de départ
    print(f"Avant achat : {joueur.animaux[0].nom} a {joueur.animaux[0].santé} vie et {joueur.animaux[0].degats} attaque.")
    print(f"Gold initial : {joueur.gold}")

    # Test de l’achat de la pomme sur l’animal à la position 0
    success = joueur.acheter_nourriture(boutique, from_index=0, cible=0)

    # Résultats attendus
    print(f"Achat réussi ? {success}")
    print(f"Après achat : {joueur.animaux[0].nom} a {joueur.animaux[0].santé} vie et {joueur.animaux[0].degats} attaque.")
    print(f"Gold restant : {joueur.gold}")
 

def test_geler_animal():
    print("\n=== Test de la capacité de geler un animal ===")
    equipe = [data.MOCK_ANIMAUX[0], data.MOCK_ANIMAUX[1], None, None, None]
    cible = equipe[0]  # Par exemple, le premier animal de l'équipe
    cible.gelé = True  # Simule le gel de l'animal
    boutique = Boutique()
    boutique.animaux = [cible, None, None] 
    boutique.afficher_animaux() # Simule une boutique avec l'animal gelé
    boutique.raffraichir()  # Rafraîchit la boutique pour s'assurer que les effets sont appliqués
  

if __name__ == "__main__":
    test_acheter_nourriture()
    test_geler_animal()