class Atout:
    def __init__(self, nom,effet, trigger):
        self.nom = nom
        self.effet = effet
        self.trigger = trigger

    def activer(self, **kwargs):
        self.effet(**kwargs)