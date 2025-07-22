class Atout:
    def __init__(self, nom, effet, trigger, utilisations=None):
        self.nom = nom
        self.effet = effet  # fonction à appeler
        self.trigger = trigger
        self.utilisations = utilisations  # nombre d'activations possibles

    def activer(self, **kwargs):
        if self.utilisations is None or self.utilisations > 0: 
            self.effet(**kwargs)
           
        if self.utilisations is not None:
         self.utilisations -= 1