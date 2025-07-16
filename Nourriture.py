class Nourriture:
    def __init__(self, nom, effet, description, prix=3, rang=1):
        self.nom = nom
        self.effet = effet
        self.description = description
        self.prix = prix
        self.rang = rang

    def utiliser(self,  **kwargs):
        if self.effet:
            self.effet(**kwargs)

    def clone(self):
            copie = Nourriture(self.nom, self.effet, self.prix, self.rang)
            return copie
   