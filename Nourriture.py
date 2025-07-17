class Nourriture:
    def __init__(self, nom, effet, description, prix=3, rang=1, requiert_cible=True):
        self.nom = nom
        self.effet = effet
        self.description = description
        self.prix = prix
        self.rang = rang
        self.requiert_cible = requiert_cible

    def utiliser(self,  **kwargs):
        if self.effet:
            self.effet(**kwargs)

    def clone(self):
            copie = Nourriture(self.nom, self.effet,self.description, self.prix, self.rang, self.requiert_cible)
            return copie
   