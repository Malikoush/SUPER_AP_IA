from Evenements import Evenement

class Capacité:
    def __init__(self, nom, trigger: Evenement, effet):
        self.nom = nom
        self.trigger = trigger
        self.effet = effet  # Une fonction que tu définiras ailleurs

    def activer(self, **kwargs):
        if self.effet:
            self.effet(**kwargs)  # Exécute l'effet avec les bons arguments

