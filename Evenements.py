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
    BLESSE = "blessé"
    FIN_TOUR = "fin_du_tour"
    DEBUT_TOUR = "debut_du_tour"
