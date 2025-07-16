import data
from Boutique import Boutique
from Effet import boost_aleatoire, boost_boutique, invoque_zombie
from Evenements import Evenement
from Joueur import Joueur

# Exemple de test manuel
def test_capacite_fourmi():
    print("\n=== Test de la capacité de la Fourmi (à la mort : boost aléatoire) ===")
    equipe = [data.fourmi, data.MOCK_ANIMAUX[1], data.MOCK_ANIMAUX[2], None, None]

    # Simule la mort
    index = equipe.index(data.fourmi)
    equipe[index] = None
    if data.fourmi.capacité.trigger == Evenement.MORT:
        data.fourmi.capacité.activer(animal=data.fourmi, equipe=equipe)

def test_capacite_castor():
    print("\n=== Test de la capacité du Castor (à la vente : boost 2 amis) ===")
    equipe = [data.castor, data.MOCK_ANIMAUX[1], data.MOCK_ANIMAUX[2], None, None]

    if data.castor.capacité.trigger == Evenement.VENTE:
        data.castor.capacité.activer(animal=data.castor, equipe=equipe)

def test_capacite_criquet():
    print("\n=== Test de la capacité du Criquet (à la mort : invoquer zombie) ===")
    equipe = [data.criquet, data.MOCK_ANIMAUX[1].clone(), data.MOCK_ANIMAUX[2].clone(), None, None]

    index = equipe.index(data.criquet)
    equipe[index] = None
    if data.criquet.capacité.trigger == Evenement.MORT:
        data.criquet.capacité.activer(animal=data.criquet, position=index, equipe=equipe)

def test_capacite_canard():
    print("\n=== Test de la capacité du Canard (à la vente : boost boutique) ===")
    boutique = Boutique()
    boutique.animaux = [data.MOCK_ANIMAUX[0], None, data.MOCK_ANIMAUX[3]]
    if data.canard.capacité.trigger == Evenement.VENTE:
        data.canard.capacité.activer(animal=data.canard, boutique=boutique)

def test_capacite_poisson():
    print("\n=== Test de la capacité du Poisson (à l'évolution : boost 2 amis) ===")
    equipe = [data.poisson, data.MOCK_ANIMAUX[1], data.MOCK_ANIMAUX[2], None, None]

    if data.poisson.capacité.trigger == Evenement.EVOLUTION:
        data.poisson.capacité.activer(animal=data.poisson, equipe=equipe)

def test_capacite_cheval():
    print("\n=== Test de la capacité du Cheval (ami invoqué : boost temporaire) ===")
    equipe = [data.MOCK_ANIMAUX[0], data.cheval, data.MOCK_ANIMAUX[2], None, None]

    if data.cheval.capacité.trigger == Evenement.AMI_INVOQUE:
        data.cheval.capacité.activer(animal=data.cheval, equipe=equipe)

def test_capacite_moustique():
    print("\n=== Test de la capacité du Moustique (début combat : dégâts ennemi) ===")
    equipe = [data.MOCK_ANIMAUX[0], data.moustique, data.MOCK_ANIMAUX[2], None, None]

    if data.moustique.capacité.trigger == Evenement.DEBUT_COMBAT:
        data.moustique.capacité.activer(animal=data.moustique, equipe=equipe)

def test_capacite_loutre():
    print("\n=== Test de la capacité de la Loutre (à l'achat : boost 1 ami) ===")
    boutique = Boutique()
    boutique.animaux = [data.loutre, data.MOCK_ANIMAUX[1], None]
    equipe = [data.MOCK_ANIMAUX[0], data.moustique, data.MOCK_ANIMAUX[2], None, None]
    
    joueur = Joueur("Alice")
    joueur.acheter(boutique,0, 0)

    if data.loutre.capacité.trigger == Evenement.ACHAT:
        data.loutre.capacité.activer(animal=data.loutre, equipe=equipe)

def test_capacite_cochon():
    print("\n=== Test de la capacité du Cochon (à la vente : or supplémentaire) ===")
    equipe = [data.cochon, data.MOCK_ANIMAUX[1], data.MOCK_ANIMAUX[2], None, None]
    joueur = Joueur("Alice")
    joueur.ajouter_animal(data.cochon,0)
    joueur.vendre(0)

    if data.cochon.capacité.trigger == Evenement.VENTE:
        data.cochon.capacité.activer(animal=data.cochon, joueur=joueur)
        print(f"Or du joueur après vente : {joueur.gold}")

def test_capacite_pigeon():
    print("\n=== Test de la capacité du Pigeon (à la vente : stock nourriture) ===")
    boutique = Boutique()
    boutique.nourriture = [data.pomme, data.miel]
    equipe = [data.pigeon, data.MOCK_ANIMAUX[1], data.MOCK_ANIMAUX[2], None, None]

    if data.pigeon.capacité.trigger == Evenement.VENTE:
        data.pigeon.capacité.activer(animal=data.pigeon, boutique=boutique)
        print("Nourriture dans la boutique après vente :")
        boutique.afficher_nourriture()
        boutique.raffraichir() 

# Lancer les tests un par un
if __name__ == "__main__":
    test_capacite_fourmi()
    test_capacite_castor()
    test_capacite_criquet()
    test_capacite_canard()
    test_capacite_poisson()
    test_capacite_moustique()
    test_capacite_cheval()
    test_capacite_loutre()
    test_capacite_cochon()
    test_capacite_pigeon()
