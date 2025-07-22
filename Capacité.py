from Evenements import Evenement

class Capacité:
    def __init__(self, nom, trigger: Evenement, effet, max_activations=None):
        self.nom = nom
        self.trigger = trigger
        self.effet = effet  # Une fonction que tu définiras ailleurs
        self.max_activations = max_activations
        self.activations_restantes = max_activations 
        self._activations_par_animal = {}

    def activer(self, animal=None, **kwargs):
        if animal is None:
            return

        ident = id(animal)

        # Calcul du nombre max d'activations (fixe ou dépendant du niveau)
        max_autorisé = (
            self.max_activations(animal)
            if callable(self.max_activations)
            else self.max_activations
        )

        actuel = self._activations_par_animal.get(ident, 0)

        if max_autorisé is None or actuel < max_autorisé:
            # Exécuter l'effet
            if callable(self.effet):
                self.effet(animal=animal, **kwargs)
            elif isinstance(self.effet, list):
                for f in self.effet:
                    f(animal=animal, **kwargs)

            self._activations_par_animal[ident] = actuel + 1 

    def reset_activations(self):
            """À appeler au début de chaque tour pour réinitialiser les compteurs"""
            self._activations_par_animal.clear()   

