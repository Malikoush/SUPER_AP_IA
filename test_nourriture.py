import data
import Joueur
from Animal import Animal

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

def test_pomme():
    print("\n=== Test de la nourriture Pomme (boost 1 ATQ et 1 VIE) ===")
    cible = data.MOCK_ANIMAUX[0]  # Par exemple, la Loutre
    data.pomme.utiliser(cible=cible)
    assert cible.degats == 2 and cible.santé == 4, "La Pomme n'a pas boosté correctement la cible."
 
def test_miel():
    print("\n=== Test de la nourriture Miel (invoque Abeille à la mort) ===")
    equipe = [data.criquet, data.MOCK_ANIMAUX[1].clone(), None,data.MOCK_ANIMAUX[2].clone(), data.MOCK_ANIMAUX[2].clone()]

    index = equipe.index(data.criquet)
    cible = equipe[0]  # ex: criquet
    data.miel.utiliser(cible=cible)
    assert cible.atout is not None
    assert cible.atout.nom == "Miel"
    print("Miel appliqué avec succès à", cible.nom)
    cible.meur(equipe)  # Simule la mort pour invoquer l'abeille

def test_miette():
    print("\n=== Test de la nourriture Miette (boost 1 VIE) ===")
    cible = data.MOCK_ANIMAUX[0]  # Par exemple, la Loutre
    data.miette.utiliser(cible=cible)
    assert cible.santé == 4, "La Miette n'a pas boosté correctement la cible."

# Lancer les tests un par un
if __name__ == "__main__":
    test_acheter_nourriture()
    test_pomme()
    test_miel()
    test_miette()