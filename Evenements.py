from enum import Enum

class Evenement(Enum):
    MORT = "mort"
    VENTE = "vente"
    ACHAT = "achat"
    DEBUT_COMBAT = "debut_combat"
    INVOCATION = "invocation"
    AMI_INVOQUE = "ami_invoque"
    EVOLUTION = "evolution"
    AMI_DEVANT_ATTAQUE = "ami_devant_attaque"
    AMI_DEVANT_MEUR = "ami_devant_attaque"
    AMI_MANGE = "ami_mange"
    BLESSE = "blessé"  # a rajouter event 
    FIN_TOUR = "fin_du_tour"
    DEBUT_TOUR = "debut_du_tour"
    ATTAQUE = "après_attaque" # a rajouter
    TUE = "tue_enemie"  # a rajouter
