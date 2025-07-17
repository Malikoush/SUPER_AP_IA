# effets.py
import random
import Utils


def boost_aleatoire(animal, equipe, boost_vie=True, boost_attaque=True, nombre_cibles=1 ,valeur_boost =1,scale_cible =False,scale_boost=False, **kwargs):
    alliés = [a for a in equipe if a is not None and a != animal]
    random.shuffle(alliés)  # mélange pour rendre l'effet aléatoire
    cibles = alliés[:nombre_cibles]

    for choisi in cibles:
        if boost_attaque:
            boost_degats =valeur_boost * animal.niveau
            choisi.degats += boost_degats
        if boost_vie:
            boost_santé =   valeur_boost * animal.niveau
            choisi.santé += boost_santé
        print(f"{animal.nom} booste {choisi.nom} : +{boost_degats if boost_attaque else 0} ATQ / +{boost_santé if boost_vie else 0} VIE")

def boost_cible(booster, cible, boost_vie=True, boost_attaque=True,valeur_boost =1, **kwargs):
   
        if boost_attaque:
            cible.degats += valeur_boost * booster.niveau
        if boost_vie:
            cible.santé += valeur_boost * booster.niveau
        print(f"{booster.nom} booste {cible.nom} : +{1 if boost_attaque else 0} ATQ / +{1 if boost_vie else 0} VIE")
   

def boost_boutique(animal, boutique,valeur_boost =1, **kwargs):
    for a in boutique.animaux:
        if a:
            a.santé += valeur_boost * animal.niveau
            print(f"{animal.nom} boost {a.nom} dans la boutique (+1 VIE)")


def invoque_zombie(position, equipe, zombie,joueur, **kwargs):
        zombie.joueur = joueur
        Utils.invoquer_animal(equipe, zombie, position)
        for animal in equipe:
            if animal is not None:
                print(f"{animal.nom} est à la position {equipe.index(animal)}")


def degats_ennemi(animal, equipe,nombre_cible, **kwargs):
        ennemis = [a for a in equipe if a is not None and a != animal]
        if not ennemis:
            return 
        random.shuffle(ennemis)  
        cibles = ennemis[:nombre_cible * animal.niveau]
        degats = 1
        for cible in cibles:
            cible.subit(degats)
            print(f"{animal.nom} inflige {degats} dégâts à {cible.nom}")
            if cible.santé <= 0:
                cible.meur_combat(equipe)
        

def or_supplémentaire(animal, joueur, **kwargs):
    if joueur:
        joueur.gold += 1 * animal.niveau
        print(f"{animal.nom} donne 1 or supplémentaire à {joueur.nom}")


def stock_nourriture(animal, boutique,nourriture, **kwargs):
    if boutique:
        boutique.nourriture.append(nourriture)
        print(f"{animal.nom} ajoute 1 nourriture à la boutique")
        
    else:
        print("Aucune boutique disponible pour stocker la nourriture.")