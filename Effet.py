# effets.py
from inspect import _empty
import math
import random
from Animal import Animal
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

def boost_cible(booster, cible, boost_vie=True, boost_attaque=True,valeur_boost_attaque =1,valeur_boost_santé =1,scale_pourcentage=False,No_scale=False, **kwargs):
        if type(booster) is Animal:
             boost = booster.niveau
        else:
            boost = 1
 
        if cible == []:
            print("Aucune cible à booster.")
            return
        if scale_pourcentage:
            gain_attaque = math.floor(valeur_boost_attaque * booster.niveau * 0.5)
            gain_santé = math.floor(valeur_boost_santé * booster.niveau * 0.5)
        elif No_scale:
            gain_attaque = valeur_boost_attaque
            gain_santé =  valeur_boost_santé 
        else:
            gain_attaque = valeur_boost_attaque * booster.niveau
            gain_santé =  valeur_boost_santé * booster.niveau
       
        if boost_attaque:
            for c in cible:
                if c is not None:
                 c.degats += gain_attaque
            
        if boost_vie:
            for c in cible:
                if c is not None:
                    c.santé += gain_santé
        for c in cible:
             if c is not None:
                 print(f"{booster.nom} booste {c.nom} : +{gain_attaque if boost_attaque else 0} ATQ / +{gain_santé if boost_vie else 0} VIE")
   



def boost_boutique(animal, boutique,valeur_boost =1, **kwargs):
    for a in boutique.animaux:
        if a:
            a.santé += valeur_boost * animal.niveau
            print(f"{animal.nom} boost {a.nom} dans la boutique (+1 VIE)")


def invoque_zombie(position, equipe, zombie,joueur,quantité=1, **kwargs):
        zombie.joueur = joueur
        for q in range(quantité):
            Utils.invoquer_animal(equipe, zombie, position)
       
        for animal in equipe:
            if animal is not None:
                print(f"{animal.nom} est à la position {equipe.index(animal)}")


def degats_ennemi(animal, equipe,nombre_cible,degats = 1,**kwargs):
        ennemis = [a for a in equipe if a is not None and a != animal]
        if not ennemis:
            return 
        random.shuffle(ennemis)  
        cibles = ennemis[:nombre_cible * animal.niveau]
        
        for cible in cibles:
            cible.subit(degats)
            print(f"{animal.nom} inflige {degats} dégâts à {cible.nom}")
           

def degats_cible(animal,cibles, degats=1,scale_pourcentage=False,  **kwargs):
        if scale_pourcentage:
            degats = math.floor(degats * animal.niveau * 0.5)
        else:
            degats = degats* animal.niveau
        
        for cible in cibles:
            if cible is not None:
                print(f"{animal.nom} inflige {degats} dégâts à {cible.nom}.")
                cible.subit(degats)
                
            
    
           
        

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

def copie_vie(animal, equipe, **kwargs):
    amie = equipe[0] if equipe else None
    for a in equipe:
        if a is not None:
      
            if a.santé > amie.santé:
                amie = a
           
    if amie:
        gain = math.floor(amie.santé * 0.5 * animal.niveau)
        animal.santé += gain
        print(f"{animal.nom} copie la vie de {amie.nom} et obtient {gain} points de vie supplémentaires.")
    else:
        print(f"{animal.nom} n'a pas trouvé d'ami plus sain pour copier la vie.")
        


