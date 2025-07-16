import data


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
    test_pomme()
    test_miel()
    test_miette()