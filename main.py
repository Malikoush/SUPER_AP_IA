from Animal import Animal
from Joueur import Joueur
from Boutique import Boutique
from Combat import Combat
from Partie import Partie

joueur1 = Joueur("Alice")
joueur2 = Joueur("Bob")

partie = Partie(joueur1, joueur2)
partie.lancer()



