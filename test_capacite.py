import data
from Boutique import Boutique
from Effet import boost_aleatoire, boost_boutique, invoque_zombie
from Evenements import Evenement
from Joueur import Joueur

# Exemple de test manuel
def test_capacite_fourmi():
    print("\n=== Test de la capacité de la Fourmi (à la mort : boost aléatoire) ===")
    equipe = [data.fourmi, data.MOCK_ANIMAUX[1].clone(), data.MOCK_ANIMAUX[2].clone(), None, None]

    # Simule la mort
   
    index = equipe.index(data.fourmi)
    equipe[index] = None

    if data.fourmi.capacité.trigger == Evenement.MORT:
        data.fourmi.capacité.activer(animal=data.fourmi, equipe=equipe)

def test_capacite_castor():
    print("\n=== Test de la capacité du Castor (à la vente : boost 2 amis) ===")
    equipe = [data.castor, data.MOCK_ANIMAUX[1].clone(), data.MOCK_ANIMAUX[2].clone(), None, None]

    if data.castor.capacité.trigger == Evenement.VENTE:
        data.castor.capacité.activer(animal=data.castor, equipe=equipe)

def test_capacite_criquet():
    print("\n=== Test de la capacité du Criquet (à la mort : invoquer zombie) ===")
    equipe = [data.criquet, data.MOCK_ANIMAUX[1].clone(), data.MOCK_ANIMAUX[2].clone(), None, None]
    joueur = Joueur("Alice")
    joueur.animaux= equipe
    equipe[0].joueur = joueur
    equipe[0].meur()
    

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
    equipe_enemie = [data.MOCK_ANIMAUX[0], data.moustique.clone(), data.MOCK_ANIMAUX[2], None, None]
    data.moustique.evolue()
    if data.moustique.capacité.trigger == Evenement.DEBUT_COMBAT:
        data.moustique.capacité.activer(animal=data.moustique, equipe=equipe,equipe_enemie=equipe_enemie)

def test_capacite_loutre():
    print("\n=== Test de la capacité de la Loutre (à l'achat : boost 1 ami) ===")
    boutique = Boutique()
    boutique.animaux = [data.loutre, data.MOCK_ANIMAUX[1], None]
    equipe = [data.MOCK_ANIMAUX[0].clone(), data.moustique.clone(), data.MOCK_ANIMAUX[2].clone(), None, None]
    
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

def test_capacite_flamant_rose():
    print("\n=== Test de la capacité du Flamant Rose (à la mort : boost 2 amis derrière) ===")
    equipe = [data.flamant_rose, None, data.MOCK_ANIMAUX[1].clone(), data.MOCK_ANIMAUX[2].clone(), None]

    index = equipe.index(data.flamant_rose)
    equipe[index] = None
    if data.flamant_rose.capacité.trigger == Evenement.MORT:
        data.flamant_rose.capacité.activer(animal=data.flamant_rose,position=index, equipe=equipe)

def test_capacite_crabe():
    print("\n=== Test de la capacité du Crabe (au début combat : copie vie ami plus sain) ===")
    equipe = [data.crabe, data.MOCK_ANIMAUX[1].clone(), data.MOCK_ANIMAUX[2].clone(), None, None]
   

    if data.crabe.capacité.trigger == Evenement.DEBUT_COMBAT:
        data.crabe.capacité.activer(animal=data.crabe, equipe=equipe)

def test_capacite_hérisson():
    print("\n=== Test de la capacité du Hérisson (à la mort : dégâts à tous) ===")
    equipe = [data.hérisson.clone(), data.MOCK_ANIMAUX[1].clone(), data.MOCK_ANIMAUX[2].clone(), None, None]
    equipe_enemie = [data.MOCK_ANIMAUX[0].clone(), data.moustique.clone(), data.MOCK_ANIMAUX[2].clone(), None, None]
    joueur = Joueur("Alice")
    joueur2 = Joueur("Bob")
    
    for i in range(len(equipe)):
        if equipe[i] is not None:
            equipe[i].joueur = joueur
    for i in range(len(equipe_enemie)):
        if equipe_enemie[i] is not None:
            equipe_enemie[i].joueur = joueur2
    joueur.animaux = equipe
    joueur2.animaux = equipe_enemie
    joueur.adversaire = joueur2
    joueur2.adversaire = joueur
   

    equipe[0].meur_combat(joueur.animaux)  # Simule la mort du hérisson
  

def test_capacite_kangourou():
    print("\n=== Test de la capacité du Kangourou (ami devant attaque gagne stat) ===")
    equipe = [data.kangourou, data.MOCK_ANIMAUX[1].clone(), data.MOCK_ANIMAUX[2].clone(), None, None]

    if data.kangourou.capacité.trigger == Evenement.AMI_DEVANT_ATTAQUE:
        data.kangourou.capacité.activer(animal=data.kangourou, equipe=equipe)

def test_capacite_paon():
    print("\n=== Test de la capacité du Paon (quand blessé : gagne attaque) ===")
    equipe = [data.paon, data.MOCK_ANIMAUX[1].clone(), data.MOCK_ANIMAUX[2].clone(), None, None]

    if data.paon.capacité.trigger == Evenement.BLESSE:
        data.paon.capacité.activer(animal=data.paon, equipe=equipe)

def test_capacite_rat():
    print("\n=== Test de la capacité du Rat (à la mort : invoque rat sale) ===")
    equipe = [data.rat, data.MOCK_ANIMAUX[1].clone(), data.MOCK_ANIMAUX[2].clone(), None, None]
    equipe_enemie = [data.MOCK_ANIMAUX[0].clone(), data.moustique.clone(), data.MOCK_ANIMAUX[2],None, None]
    joueur = Joueur("Alice")
    joueur2 = Joueur("Bob")
    equipe[0].joueur = joueur
    joueur.animaux = equipe
    joueur.adversaire = joueur2
    joueur.adversaire.animaux = equipe_enemie
    joueur.animaux

    equipe[0].meur_combat(joueur.animaux)

def test_capacite_escargot():
    print("\n=== Test de la capacité de l'escargot (fin du tour :si defaite  boost santé equipe) ===")
    equipe = [data.escargot, data.MOCK_ANIMAUX[1].clone(), data.MOCK_ANIMAUX[2].clone(), None, None]

    if data.escargot.capacité.trigger == Evenement.FIN_TOUR:
        data.escargot.capacité.activer(animal=data.escargot, equipe=equipe)

def test_capacite_araigné():
    print("\n=== Test de la capacité de l'araigné (mort : invoque un animal tier 3) ===")
    equipe = [data.araignée.clone(), data.MOCK_ANIMAUX[1].clone(), data.MOCK_ANIMAUX[2].clone(), None, None]
    joueur = Joueur("Alice")
    joueur.animaux = equipe 
    equipe[0].joueur = joueur

    equipe[0].meur_combat(equipe)

def test_capacite_cygne():
    print("\n=== Test de la capacité ddu cygne(mdebut du tour : gagne de l'or) ===")
    equipe = [data.cygne, data.MOCK_ANIMAUX[1], data.MOCK_ANIMAUX[2], None, None]
    joueur = Joueur("Alice")
    joueur.animaux = equipe
    equipe[0].joueur = joueur

    if data.cygne.capacité.trigger == Evenement.DEBUT_TOUR:
        data.cygne.capacité.activer(animal=data.cygne)
        print(f"Or du joueur debut du tour : {joueur.gold}")

def test_capacite_ver():
    print("\n=== Test de la capacité du Ver (début du tour : stocke une pomme) ===")
    boutique = Boutique()
    joueur = Joueur("Alice")
    joueur.boutique = boutique
    vero = data.ver.clone()
    vero.evolue()
    
    if vero.capacité.trigger == Evenement.DEBUT_TOUR:
        boutique.raffraichir()  
        boutique.afficher_nourriture()
        vero.capacité.activer(boutique=boutique, animal=vero)
       
        
        boutique.afficher_nourriture()
        
def test_capacite_blaireau():
    print("\n=== Test de la capacité du Blaireau (à la mort : dégâts aux ennemis) ===")
    equipe = [ data.blaireau.clone(),data.MOCK_ANIMAUX[1].clone(), data.MOCK_ANIMAUX[1].clone(), data.MOCK_ANIMAUX[2].clone(), None, None]
    equipe_enemie = [data.MOCK_ANIMAUX[0].clone(), data.moustique.clone(), data.MOCK_ANIMAUX[2].clone(), None, None]
    joueur = Joueur("Alice")
    joueur2 = Joueur("Bob")
    
    for i in range(len(equipe)):
        if equipe[i] is not None:
            equipe[i].joueur = joueur
    for i in range(len(equipe_enemie)):
        if equipe_enemie[i] is not None:
            equipe_enemie[i].joueur = joueur2
    joueur.animaux = equipe
    joueur2.animaux = equipe_enemie
    joueur.adversaire = joueur2
    joueur2.adversaire = joueur

    equipe[0].meur_combat(joueur.animaux)  # Simule la mort du blaireau
    

def test_capacite_chameau():
    print("\n=== Test de la capacité du chameau(blessé: boost amis deriere) ===")
    chammeau = data.chameau.clone()
    
    equipe = [chammeau, data.MOCK_ANIMAUX[1].clone(), data.MOCK_ANIMAUX[2].clone(), None, None]
    index = equipe.index(chammeau)
    if chammeau.capacité.trigger == Evenement.BLESSE:
        chammeau.capacité.activer(animal=chammeau,position = index,equipe =equipe)

def test_capacite_dodo():
    print("\n=== Test de la capacité du Dodo (début combat : donne attaque à l'ami devant) ===")
    dodo = data.dodo.clone()
    equipe = [data.MOCK_ANIMAUX[1].clone(), dodo ,data.MOCK_ANIMAUX[2].clone(),  None, None]
    index = equipe.index(dodo) 

    if dodo.capacité.trigger == Evenement.DEBUT_COMBAT:
        dodo.capacité.activer(animal=dodo, equipe=equipe, position=index)

def test_capacite_chien():
    print("\n=== Test de la capacité du Chien (ami invoquer : gagne attaque et vie) ===")
    chien = data.chien.clone()
    equipe = [data.MOCK_ANIMAUX[1].clone(), chien,data.MOCK_ANIMAUX[2].clone(),  None, None]
    joueur = Joueur("Alice")
    joueur.animaux = equipe
    joueur.ajouter_animal(data.MOCK_ANIMAUX[1].clone(),0)
    joueur.ajouter_animal(data.MOCK_ANIMAUX[1].clone(),0)
    joueur.ajouter_animal(data.MOCK_ANIMAUX[1].clone(),0)

def test_capacite_dauphin():
        print("\n=== Test de la capacité du dauphin (debut combat : attaque le plus faible) ===")
        dauphin = data.dauphin.clone()
        equipe = [data.MOCK_ANIMAUX[1].clone(), dauphin ,data.MOCK_ANIMAUX[2].clone(),  None, None]
        equipe_enemie = [data.MOCK_ANIMAUX[0].clone(), data.moustique.clone(), data.MOCK_ANIMAUX[2].clone(), None, None]
        joueur = Joueur("Alice")
        joueur2 = Joueur("Bob")
        
        for i in range(len(equipe)):
            if equipe[i] is not None:
                equipe[i].joueur = joueur
        for i in range(len(equipe_enemie)):
            if equipe_enemie[i] is not None:
                equipe_enemie[i].joueur = joueur2
        joueur.animaux = equipe
        joueur2.animaux = equipe_enemie
        joueur.adversaire = joueur2
        joueur2.adversaire = joueur
        index = equipe.index(dauphin) 

        if dauphin.capacité.trigger == Evenement.DEBUT_COMBAT:
            dauphin.capacité.activer(animal=dauphin, equipe_enemie=equipe_enemie)

def test_capacite_elephant():
        print("\n=== Test de la capacité de l'éléphant  (après attaque : blesse amis derriere) ===")
        éléphant  = data.éléphant .clone()
        equipe = [data.MOCK_ANIMAUX[1].clone(), éléphant  ,data.MOCK_ANIMAUX[2].clone(),  None, None]
        equipe_enemie = [data.MOCK_ANIMAUX[0].clone(), data.moustique.clone(), data.MOCK_ANIMAUX[2].clone(), None, None]
        joueur = Joueur("Alice")
        joueur2 = Joueur("Bob")
        
        for i in range(len(equipe)):
            if equipe[i] is not None:
                equipe[i].joueur = joueur
        for i in range(len(equipe_enemie)):
            if equipe_enemie[i] is not None:
                equipe_enemie[i].joueur = joueur2
        joueur.animaux = equipe
        joueur2.animaux = equipe_enemie
        joueur.adversaire = joueur2
        joueur2.adversaire = joueur
        index = equipe.index(éléphant ) 

        if éléphant .capacité.trigger == Evenement.ATTAQUE:
            éléphant .capacité.activer(animal=éléphant , equipe=equipe, position = index)

def test_capacite_girafe():
    print("\n=== Test de la capacité du girafe (fin tour : donne attaque,santé à l'ami devant) ===")
    girafe = data.girafe.clone()
    equipe = [data.MOCK_ANIMAUX[1].clone(), girafe ,data.MOCK_ANIMAUX[2].clone(),  None, None]
    index = equipe.index(girafe) 

    if girafe.capacité.trigger == Evenement.FIN_TOUR:
        girafe.capacité.activer(animal=girafe, equipe=equipe, position=index)

def test_capacite_boeuf():
    print("\n=== Test de la capacité du boeuf (amis devant meur : d gagne pasteque et attaque) ===")
    boeuf = data.boeuf.clone()
    equipe = [data.MOCK_ANIMAUX[1].clone(), boeuf ,data.MOCK_ANIMAUX[2].clone(),  None, None]
    index = equipe.index(boeuf) 

    if boeuf.capacité.trigger == Evenement.AMI_DEVANT_MEUR:
        boeuf.capacité.activer(animal=boeuf, equipe=equipe, position=index)
    
    equipe[0].attaque(boeuf)
    equipe[0].attaque(boeuf)
    boeuf.capacité.reset_activations()
    boeuf.capacité.activer(animal=boeuf, equipe=equipe, position=index)
    equipe[0].attaque(boeuf)

def test_capacite_lapin():
    print("\n=== Test de la capacité du lapin (amis mange : gagne vie) ===")
    lapin = data.lapin.clone()
    equipe = [data.MOCK_ANIMAUX[1].clone(), lapin ,data.MOCK_ANIMAUX[2].clone(),  None, None]
    index = equipe.index(lapin) 

    if lapin.capacité.trigger == Evenement.AMI_MANGE:
        lapin.capacité.activer(animal=lapin, equipe=equipe, position=index)
        lapin.capacité.activer(animal=lapin, equipe=equipe, position=index)
        lapin.capacité.activer(animal=lapin, equipe=equipe, position=index)
        lapin.capacité.activer(animal=lapin, equipe=equipe, position=index)
        lapin.evolue()
        lapin.capacité.activer(animal=lapin, equipe=equipe, position=index)
    
    
    lapin.capacité.reset_activations()
    lapin.capacité.activer(animal=lapin, equipe=equipe, position=index)

def test_capacite_mouton():
    print("\n=== Test de la capacité du mouton (à la mort : invoque 2 béliers) ===")
    mouton = data.mouton.clone()
    equipe = [data.MOCK_ANIMAUX[1].clone(), mouton ,data.MOCK_ANIMAUX[2].clone(),  None, None]
    joueur = Joueur("Alice")
    joueur.animaux = equipe 
    equipe[1].joueur = joueur

    equipe[1].meur_combat(equipe)    


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
    test_capacite_flamant_rose()
    test_capacite_crabe()
    test_capacite_hérisson()
    test_capacite_kangourou()
    test_capacite_paon()
    test_capacite_rat()
    test_capacite_escargot()
    test_capacite_araigné()
    test_capacite_cygne()
    test_capacite_ver()
    test_capacite_blaireau()
    test_capacite_chameau()
    test_capacite_dodo()
    test_capacite_chien()
    test_capacite_dauphin()
    test_capacite_elephant()
    test_capacite_girafe()
    test_capacite_boeuf()
    test_capacite_lapin()
    test_capacite_mouton()