# mock_data.py
from Animal import Animal
from Atout import Atout
from Capacité import Capacité
from Evenements import Evenement
import Effet
from Nourriture import Nourriture

à_la_mort_boost_aleatoire = Capacité("à_la_mort_boost_aleatoire", Evenement.MORT,lambda animal, equipe=None: Effet.boost_aleatoire(animal, equipe=equipe))
à_la_vente_boost_2_amis = Capacité("à_la_vente_boost_2_amis", Evenement.VENTE,lambda animal, equipe=None: Effet.boost_aleatoire(animal, equipe=equipe, nombre_cibles=2 ,boost_vie=False))
à_la_mort_invoque_zombie = Capacité("à_la_mort_invoque_zombie", Evenement.MORT, lambda  position,animal, equipe=None: Effet.invoque_zombie(position=position, equipe=equipe, zombie=zombie_criquet))
à_la_vente_boost_boutique = Capacité("à_la_vente_boost_boutique", Evenement.VENTE, lambda animal, boutique=None: Effet.boost_boutique(animal, boutique=boutique))
à_lévolution_boost_2_amis = Capacité("à_lévolution_boost_2_amis", Evenement.EVOLUTION, lambda animal, equipe=None: Effet.boost_aleatoire(animal, equipe=equipe, nombre_cibles=2 ))
ami_invoqué_boost_temporaire = Capacité("ami_invoqué_boost_temporaire", Evenement.AMI_INVOQUE, lambda animal, equipe=None: Effet.boost_aleatoire(animal, equipe=equipe, nombre_cibles=1, boost_vie=False))
début_combat_degats_ennemi = Capacité("début_combat_degats_ennemi", Evenement.DEBUT_COMBAT, lambda animal, equipe=None: Effet.degats_ennemi(animal, equipe=equipe, nombre_cible=1))
à_lachat_boost_1_ami = Capacité("à_lachat_boost_1_ami", Evenement.ACHAT,lambda animal, equipe=None: Effet.boost_aleatoire(animal,equipe=equipe,nombre_cibles=1,boost_attaque=False))
à_la_vente_or_supplémentaire = Capacité("à_la_vente_or_supplémentaire", Evenement.VENTE, lambda animal, joueur=None: Effet.or_supplémentaire(animal, joueur=joueur))
à_la_vente_stock_nourriture = Capacité("à_la_vente_stock_nourriture", Evenement.VENTE, lambda animal, boutique=None: Effet.stock_nourriture(animal, boutique=boutique, nourriture=miette))

#invocation d'un zombie
zombie_criquet = Animal("Zombie Criquet", 1, 1, None, 1, 1, 1)
abeille = Animal("Abeille", 1, 1, None, 1, 1, 1)
# Animaux Tier 1
fourmi = Animal("Fourmi", 2, 2, à_la_mort_boost_aleatoire,1, 1, 1)
castor = Animal("Castor", 3, 2, à_la_vente_boost_2_amis,1, 1, 1)
criquet = Animal("Criquet", 1, 3, à_la_mort_invoque_zombie,1, 1, 1)
canard = Animal("Canard", 2, 3, à_la_vente_boost_boutique, 1, 1, 1)
poisson = Animal("Poisson", 2, 3, à_lévolution_boost_2_amis, 1, 1, 1)
cheval = Animal("Cheval", 2, 1, ami_invoqué_boost_temporaire, 1, 1, 1)
moustique = Animal("Moustique", 2, 2, début_combat_degats_ennemi, 1, 1, 1)
loutre = Animal("Loutre", 1, 3, à_lachat_boost_1_ami, 1, 1, 1)
cochon = Animal("Cochon", 4, 1, à_la_vente_or_supplémentaire, 1, 1, 1)
pigeon = Animal("Pigeon", 3, 1, à_la_vente_stock_nourriture, 1, 1, 1)

#Nourriture Tier 1
pomme = Nourriture("Pomme",lambda cible : Effet.boost_cible(pomme,cible), "+1 vie,+1 degat animal", 3, 1)
miel = Nourriture("Miel",lambda cible: setattr(cible, 'atout', Atout("Miel",lambda position, equipe=None : Effet.invoque_zombie(position=position,equipe = equipe,zombie=abeille), trigger=Evenement.MORT)), "Ajoute l'atout miel a l'animal", 3, 1)
miette = Nourriture("Miette de pain",lambda cible: Effet.boost_cible(miette, cible, boost_vie=False), "+1 degat animal", 0, 1)

# Liste des animaux mockés
MOCK_ANIMAUX = [
    loutre, poisson,
    fourmi, castor, criquet, canard,
    cheval, moustique, cochon, pigeon
]
MOCK_NOURRITURE = [
    pomme, miel, miette
]