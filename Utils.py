def invoquer_animal(equipe, animal, position=None):
    if position is not None:
        if position < 0 or position >= len(equipe):
            print("Position invalide.")
            return False
        if equipe[position] is not None:
            if not decaler_equipe(equipe, position):
                print(f"Equipe pleine invocation de {animal.nom} impossible.")
                return False
            
        equipe[position] = animal
        return True
    else:
        for i in range(len(equipe)):
            if equipe[i] is None:
                equipe[i] = animal
                return True
        print("Pas de place libre.")
        return False

def decaler_droite(equipe, position_cible):
    taille = len(equipe)
    # Cherche une case libre à droite
    libre = None
    for i in range(position_cible + 1, taille):
        if equipe[i] is None:
            libre = i
            break
    if libre is None:
        return False  # Pas de place libre à droite

    # Décale en chaîne vers la droite
    for i in range(libre, position_cible, -1):
        equipe[i] = equipe[i-1]
    equipe[position_cible] = None
    return True

def decaler_gauche(equipe, position_cible):
    # Cherche une case libre à gauche
    libre = None
    for i in range(position_cible - 1, -1, -1):
        if equipe[i] is None:
            libre = i
            break
    if libre is None:
        return False  # Pas de place libre à gauche

    # Décale en chaîne vers la gauche
    for i in range(libre, position_cible):
        equipe[i] = equipe[i+1]
    equipe[position_cible] = None
    return True

def decaler_equipe(equipe, position_cible):
    if decaler_droite(equipe, position_cible):
        return True
    if decaler_gauche(equipe, position_cible):
        return True
    return False
