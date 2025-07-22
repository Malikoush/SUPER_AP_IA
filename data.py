# mock_data.py
import random
from Animal import Animal
from Atout import Atout
from Capacité import Capacité
from Evenements import Evenement
import Effet
from Nourriture import Nourriture

# Atout
miel_atout = Atout("Miel", lambda position, equipe=None: Effet.invoque_zombie(position=position, equipe=equipe, zombie=abeille, joueur=None), trigger=Evenement.MORT)
pasteque_atout = Atout("Pastèque", lambda animal: Effet.bouclier_degats(animal), trigger=Evenement.BLESSE,utilisations=1)

#Capacité tier 1
à_la_mort_boost_aleatoire = Capacité("à_la_mort_boost_aleatoire", Evenement.MORT,lambda animal, equipe=None,position=None,**kwargs: Effet.boost_aleatoire(animal, equipe=equipe,scale_boost=True))
à_la_vente_boost_2_amis = Capacité("à_la_vente_boost_2_amis", Evenement.VENTE,lambda animal, equipe=None,position=None: Effet.boost_aleatoire(animal, equipe=equipe, nombre_cibles=2 ,boost_vie=False,scale_boost=True))
à_la_mort_invoque_zombie = Capacité("à_la_mort_invoque_zombie", Evenement.MORT, lambda  position,animal, equipe=None,**kwargs: Effet.invoque_zombie(position=position, equipe=equipe, zombie=generer_zombie_criquet(animal.niveau),joueur =animal.joueur))
à_la_vente_boost_boutique = Capacité("à_la_vente_boost_boutique", Evenement.VENTE, lambda animal, boutique=None,position=None: Effet.boost_boutique(animal, boutique=boutique))
à_lévolution_boost_2_amis = Capacité("à_lévolution_boost_2_amis", Evenement.EVOLUTION, lambda animal, equipe=None,position=None: Effet.boost_aleatoire(animal, equipe=equipe, nombre_cibles=2 ,scale_boost=True))
ami_invoqué_boost_temporaire = Capacité("ami_invoqué_boost_temporaire", Evenement.AMI_INVOQUE, lambda animal, equipe=None,position=None: Effet.boost_aleatoire(animal, equipe=equipe, nombre_cibles=1, boost_vie=False,scale_boost=True))
début_combat_degats_ennemi = Capacité("début_combat_degats_ennemi", Evenement.DEBUT_COMBAT, lambda animal, equipe=None,equipe_enemie =None,position=None: Effet.degats_ennemi(animal, equipe=equipe_enemie, nombre_cible=animal.niveau))
à_lachat_boost_1_ami = Capacité("à_lachat_boost_1_ami", Evenement.ACHAT,lambda animal, equipe=None,position=None: Effet.boost_aleatoire(animal,equipe=equipe,nombre_cibles=1,boost_attaque=False,scale_cible=True))
à_la_vente_or_supplémentaire = Capacité("à_la_vente_or_supplémentaire", Evenement.VENTE, lambda animal, joueur=None,position=None,equipe=None: Effet.or_supplémentaire(animal, joueur=joueur))
à_la_vente_stock_nourriture = Capacité("à_la_vente_stock_nourriture", Evenement.VENTE, lambda animal, boutique=None,position=None: Effet.stock_nourriture(animal, boutique=boutique, nourriture=miette))

# Capacité tier 2
au_debut_combat_copie_vie_ami_plus_sain = Capacité("au_debut_combat_copie_vie_ami_plus_sain", Evenement.DEBUT_COMBAT, lambda animal, equipe=None,position=None: Effet.copie_vie(animal, equipe=equipe))
à_la_mort_booste_2_amis_derrière = Capacité(
    "à_la_mort_booste_2_amis_derrière",
    Evenement.MORT,
    lambda animal, equipe=None, position=None: Effet.boost_cible(
        animal,
       cible=[
            equipe[i] for i in range(position + 1, len(equipe))
            if equipe[i] is not None
        ][:2]
    )
)
à_la_mort_degats_a_tous = Capacité("à_la_mort_degats_2_a_tous", Evenement.MORT, lambda animal, equipe=None,equipe_enemie=None, position=None,**kwargs: Effet.degats_cible(animal,cibles= equipe_enemie+equipe, degats=2))
ami_devant_attaque_gagne_stat = Capacité("ami_devant_attaque_gagne_stat", Evenement.AMI_DEVANT_ATTAQUE, lambda animal, equipe=None, position=None: Effet.boost_cible(animal, equipe=equipe, cible= [animal]))
quand_blessé_gagne_attaque = Capacité("quand_blessé_gagne_attaque", Evenement.BLESSE, lambda animal, equipe=None, position=None: Effet.boost_cible(animal, equipe=equipe, cible=[animal], boost_attaque=True))
à_la_mort_invoque_rat_sale = Capacité("à_la_mort_invoque_rat_sale", Evenement.MORT, lambda position, animal, equipe=None,equipe_enemie = None: Effet.invoque_zombie(position=0, equipe=equipe_enemie, zombie=Animal("Rat Sale", 1, 1, None, 1, 1, 1), joueur=animal.joueur.adversaire))
fin_de_tour_si_perdu_gagne_vie_aux_amis = Capacité("fin_de_tour_si_perdu_gagne_vie_aux_amis",Evenement.FIN_TOUR, lambda animal,equipe, **kwargs: Effet.boost_cible(animal,equipe = equipe,cible = equipe,boost_attaque=False))
à_la_mort_invoque_pet_tier3 = Capacité(" à_la_mort_invoque_pet_tier3",Evenement.MORT,lambda animal, position,equipe =None,**kwargs  : Effet.invoque_zombie(equipe=equipe,position=position,zombie= genere_tier_3(animal.niveau),joueur=animal.joueur))
au_debut_tour_gagne_or = Capacité("au_debut_tour_gagne_or", Evenement.DEBUT_TOUR, lambda animal, **kwargs: Effet.or_supplémentaire(animal =animal, joueur=animal.joueur))
au_debut_tour_stocke_pomme = Capacité("au_debut_tour_stocke_pomme", Evenement.DEBUT_TOUR,lambda boutique,animal, **kwargs: Effet.stock_nourriture(animal,boutique = boutique,nourriture= generer_ver_pomme(animal.niveau)))

#Capacité tier 3
à_la_mort_degats_aux_voisins = Capacité(
    "à_la_mort_degats_aux_voisins",
    Evenement.MORT,
    lambda animal, equipe=None, equipe_enemie=None, position=None: (
        lambda merged, pos: Effet.degats_cible(
            animal,
            cibles=[
                c for c in (
                    [a for a in merged[pos+1:] if a is not None][:1] +
                    [a for a in merged[:pos][::-1] if a is not None][:1]
                )
            ],
            degats=animal.degats,scale_pourcentage=True
        )
    )(
        # Fusion des équipes, équipe inversée à gauche, position recalculée
        merged = list(reversed(equipe)) + equipe_enemie,
        pos = len(equipe) - 1 - position
    )
)

quand_blessé_boost_ami_derrière = Capacité("quand_blessé_boost_ami_derrière",Evenement.BLESSE, 
        lambda animal, equipe=None, position=None: Effet.boost_cible(
        animal,
       cible=[
            equipe[i] for i in range(position + 1, len(equipe))
            if equipe[i] is not None
        ][:1]
    ))

début_combat_donne_attaque_ami_devant = Capacité("début_combat_donne_attaque_ami_devant",Evenement.DEBUT_COMBAT,
         lambda animal, equipe=None, position=None: Effet.boost_cible(
        animal,
       cible=[
            equipe[i] for i in range(position -1,position)
            if equipe[i] is not None and equipe[i] != animal
        ][:1],scale_pourcentage=True,valeur_boost_attaque=animal.degats,boost_vie=False))

ami_invoqué_gain_temporaire = Capacité("ami_invoqué_gain_temporaire", Evenement.AMI_INVOQUE,
         lambda animal, equipe=None, position=None: Effet.boost_cible(
        animal,
       cible=[animal]
        ,valeur_boost_attaque=2,scale_boost=True))

début_combat_degats_ennemi_le_plus_faible = Capacité("début_combat_degats_ennemi_le_plus_faible",Evenement.DEBUT_COMBAT,
                                                     lambda animal,equipe_enemie=None, equipe=None :Effet.degats_cible(
                                                      animal, 
                                                      cibles= [ min(
                                                                  [a for a in equipe_enemie if a is not None],
                                                                    key=lambda x: x.santé
                                                                        )
                                                      ],
                                                    degats=4

                                                     )
                                                     )

après_attaque_blesse_ami_derrière = Capacité("après_attaque_blesse_ami_derrière",Evenement.ATTAQUE,
                                               lambda animal, equipe=None, position=None: Effet.degats_cible(
        animal,
       cibles=[
            equipe[i] for i in range(position + 1, len(equipe))
            if equipe[i] is not None
        ][:1]
    )
                                                  


)

fin_de_tour_boost_ami_devant = Capacité("fin_de_tour_boost_ami_devant",Evenement.FIN_TOUR,
                                        lambda animal, equipe=None, position=None: Effet.boost_cible(
        animal,
       cible=[
            equipe[i] for i in range(position -1,position)
            if equipe[i] is not None and equipe[i] != animal
        ][:1]))

ami_devant_meurt_gain_melon_et_attaque = Capacité("ami_devant_meurt_gain_melon_et_attaque",Evenement.AMI_DEVANT_MEUR,[
    lambda animal, equipe=None, position=None: Effet.boost_cible(animal,cible=[animal],boost_vie=False,No_scale=True),
    lambda animal,**kwargs: setattr(animal, 'atout',pasteque_atout)
],
 max_activations=lambda animal: animal.niveau )

ami_mange_nourriture_gain_vie = Capacité("ami_mange_nourriture_gain_vie",Evenement.AMI_MANGE,
    lambda animal, equipe=None, position=None,**kwargs: Effet.boost_cible(animal,cible=[animal],boost_attaque=False), max_activations=4)

à_la_mort_invoque_2_béliers = Capacité("à_la_mort_invoque_2_béliers", Evenement.MORT,
        lambda position, animal, equipe=None, **kwargs: Effet.invoque_zombie(
        position=position, 
        equipe=equipe, 
        zombie=generer_zombie_belier(animal.niveau), 
        joueur=animal.joueur,
        quantité=2,
        nombre=2
    )
)

# Capacité tier 4
fin_de_tour_si_ami_niveau_3_gain_stats = Capacité("fin_de_tour_si_ami_niveau_3_gain_stats", Evenement.FIN_TOUR,
    lambda animal, equipe=None, position=None: Effet.boost_cible(
        animal,
        cibles = [animal] if any(a for a in equipe if a is not None and a.niveau >= 3) else [] ,
        valeur_boost_santé=2
    )
)

quand_blessé_degats_ennemi_aleatoire= Capacité("quand_blessé_degats_ennemi_aleatoire", Evenement.BLESSE,lambda animal, equipe=None, position=None, equipe_enemie=None: Effet.degats_ennemi(animal, equipe=equipe_enemie, nombre_cible=1,degats=3 * animal.niveau))
élimine_ennemi_gain_stats = Capacité("élimine_ennemi_gain_stats", Evenement.TUE, lambda animal, equipe=None, position=None, equipe_enemie=None: Effet.boost_cible( 
    animal,
    cibles = [animal] ,
    valeur_boost_santé=3, valeur_boost_attaque=3
))

#invocation d'un zombie
def generer_zombie_criquet(niveau):
    return Animal("Zombie Criquet", niveau, niveau, None, 1, 1, 1)
def generer_zombie_belier(niveau):
    return Animal("Bélier", niveau * 2,  niveau *2, None, 1, 1, 1)
def genere_tier_3(niveaux):
    tier3_animaux = [a for a in MOCK_ANIMAUX if a.rang == 3] 
    random_zombie = random.choice(tier3_animaux).clone()
    random_zombie.degats = 2* niveaux
    random_zombie.santé = 2 * niveaux
    return random_zombie
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

# Animaux Tier 2
crabe = Animal("Crabe", 4, 1, au_debut_combat_copie_vie_ami_plus_sain, 1, 1, 2)
flamant_rose = Animal("Flamant Rose", 3, 2, à_la_mort_booste_2_amis_derrière, 1, 1, 2)
hérisson = Animal("Hérisson", 4, 2, à_la_mort_degats_a_tous, 1, 1, 2)
kangourou = Animal("Kangourou", 2, 3, ami_devant_attaque_gagne_stat, 1, 1, 2)
paon = Animal("Paon", 2, 5, quand_blessé_gagne_attaque, 1, 1, 2)
rat = Animal("Rat", 3, 6, à_la_mort_invoque_rat_sale, 1, 1, 2)
escargot = Animal("Escargot", 2, 2, fin_de_tour_si_perdu_gagne_vie_aux_amis, 1, 1, 2)
araignée = Animal("Araignée", 2, 2, à_la_mort_invoque_pet_tier3, 1, 1, 2)
cygne = Animal("Cygne", 1, 2, au_debut_tour_gagne_or, 1, 1, 2)
ver = Animal("Ver", 1, 3, au_debut_tour_stocke_pomme, 1, 1, 2)

# Animaux Tier 3
blaireau = Animal("Blaireau", 6, 3, à_la_mort_degats_aux_voisins, 1, 1, 3)
chameau = Animal("Chameau", 3, 4, quand_blessé_boost_ami_derrière, 1, 1, 3)
dodo = Animal("Dodo", 4, 2, début_combat_donne_attaque_ami_devant, 1, 1, 3)
chien = Animal("Chien", 3, 2, ami_invoqué_gain_temporaire, 1, 1, 3)
dauphin = Animal("Dauphin", 4, 3, début_combat_degats_ennemi_le_plus_faible, 1, 1, 3)
éléphant = Animal("Éléphant", 3, 7, après_attaque_blesse_ami_derrière, 1, 1, 3)
girafe = Animal("Girafe", 1, 2, fin_de_tour_boost_ami_devant, 1, 1, 3)
boeuf = Animal("Bœuf", 1, 3, ami_devant_meurt_gain_melon_et_attaque, 1, 1, 3)
lapin = Animal("Lapin", 1, 2, ami_mange_nourriture_gain_vie, 1, 1, 3)
mouton = Animal("Mouton", 2, 2, à_la_mort_invoque_2_béliers, 1, 1, 3)

# Animaux Tier 4
bison = Animal("Bison", 4, 4, fin_de_tour_si_ami_niveau_3_gain_stats, 1, 1, 4)
poisson_globe = Animal("Poisson-globe", 3, 6, quand_blessé_degats_ennemi_aleatoire, 1, 1, 4)
#cerf = Animal("Cerf", 2, 2, à_la_mort_invoque_bus_avec_piment, 1, 1, 4)
hippopotame = Animal("Hippopotame", 4, 5, élimine_ennemi_gain_stats, 1, 1, 4)
#perroquet = Animal("Perroquet", 4, 2, fin_de_tour_copie_capacité_ami_devant, 1, 1, 4)
#pingouin = Animal("Pingouin", 1, 3, fin_de_tour_boost_amis_niveau_2_plus, 1, 1, 4)
#moufette = Animal("Moufette", 3, 5, début_combat_reduit_vie_ennemi_plus_sain, 1, 1, 4)
#écureuil = Animal("Écureuil", 2, 5, début_tour_reduction_prix_nourriture, 1, 1, 4)
#tortue = Animal("Tortue", 2, 5, à_la_mort_donne_melon_ami_derrière, 1, 1, 4)
#baleine = Animal("Baleine", 3, 7, début_combat_gobe_ami_devant_le_relâche_après_mort, 1, 1, 4)

# Animaux Tier 5
#tatou = Animal("Tatou", 2, 6, début_combat_boost_vie_tous_les_amis, 1, 1, 5)
#vache = Animal("Vache", 4, 6, à_lachat_remplace_nourriture_par_lait, 1, 1, 5)
#crocodile = Animal("Crocodile", 8, 4, début_combat_degats_dernier_ennemi, 1, 1, 5)
#singe = Animal("Singe", 1, 2, fin_de_tour_boost_ami_en_tête, 1, 1, 5)
#rhinocéros = Animal("Rhinocéros", 6, 9, élimine_ennemi_degats_premier_ennemi, 1, 1, 5)
#coq = Animal("Coq", 6, 4, à_la_mort_invoque_poussins, 1, 1, 5)
#scorpion = Animal("Scorpion", 1, 1, invoqué_gagne_cacahuète, 1, 1, 5)
#phoque = Animal("Phoque", 3, 8, mange_donne_attaque_aleatoire_aux_amis, 1, 1, 5)
#requin = Animal("Requin", 2, 2, ami_meurt_gagne_stats, 1, 1, 5)
#dinde = Animal("Dinde", 3, 4, ami_invoqué_gagne_stats, 1, 1, 5)

# Animaux Tier 6
#sanglier = Animal("Sanglier", 10, 6, avant_attaque_gagne_stats, 1, 1, 6)
#chat = Animal("Chat", 4, 5, nourriture_effet_multiplié, 1, 1, 6)
#dragon = Animal("Dragon", 6, 8, achat_ami_tier1_boost_equipe, 1, 1, 6)
#mouche = Animal("Mouche", 5, 5, ami_meurt_invoque_mouche_zombie, 1, 1, 6)
#gorille = Animal("Gorille", 7, 10, quand_blessé_gagne_noix_de_coco, 1, 1, 6)
#léopard = Animal("Léopard", 10, 4, début_combat_degats_aleatoires_selon_attaque, 1, 1, 6)
#mammouth = Animal("Mammouth", 4, 12, à_la_mort_boost_toute_léquipe, 1, 1, 6)
#serpent = Animal("Serpent", 6, 6, ami_devant_attaque_degats_ennemi_aleatoire, 1, 1, 6)
#tigre = Animal("Tigre", 6, 4, ami_devant_répète_capacité, 1, 1, 6)
#ours = Animal("Ours", 5, 4, 4_amis_blessés_degats_a_tous_les_ennemis, 1, 1, 6)


def generer_ver_pomme(niveau):
     nom = "Pomme" if niveau == 1 else "Super Pomme" if niveau == 2 else "Ultra Pomme"
     description = f"+{niveau} vie, +{niveau} dégât animal"
     return  Nourriture(nom,lambda cible : Effet.boost_cible(pomme,[cible],valeur_boost=niveau), description, 2, 1)


#Nourriture Tier 1
pomme = Nourriture("Pomme",lambda cible : Effet.boost_cible(pomme,[cible]), "+1 vie,+1 degat animal", 3, 1)
miel = Nourriture("Miel",lambda cible: setattr(cible, 'atout',miel_atout), "Ajoute l'atout miel a l'animal", 3, 1)
pasteque = Nourriture("Pasteque",lambda cible: setattr(cible, 'atout',pasteque_atout), "Ajoute l'atout pasteque a l'animal", 3, 6)
miette = Nourriture("Miette de pain",lambda cible: Effet.boost_cible(miette, [cible], boost_vie=False), "+1 degat animal", 0, 100)


# Liste des animaux mockés
MOCK_ANIMAUX = [
    # Tier 1
    loutre, poisson,
    fourmi, castor, criquet, canard,
    cheval, moustique, cochon, pigeon,

    # Tier 2
    crabe, flamant_rose, hérisson, kangourou, paon,
    rat, escargot,

     # Tier 3
    blaireau, chameau, dodo, chien, dauphin,
    éléphant, girafe, boeuf, lapin, mouton,

    # # Tier 4
    # bison, poisson_globe, cerf, hippopotame, perroquet,
    # pingouin, moufette, écureuil, tortue, baleine,

    # # Tier 5
    # tatou, vache, crocodile, singe, rhinocéros,
    # coq, scorpion, phoque, requin, dinde,

    # # Tier 6
    # sanglier, chat, dragon, mouche, gorille,
    # léopard, mammouth, serpent, tigre, ours,
    
]
MOCK_NOURRITURE = [
    pomme, miel, miette
]