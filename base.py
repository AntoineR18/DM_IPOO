from copy import deepcopy
from cartes import Carte


class _ListeCartes:
    """Implémentation de la classe _ListeCartes."""

    def __init__(self, cartes):
        if (not isinstance(cartes, list) or
                not all(isinstance(carte, Carte) for carte in cartes)):
            raise ValueError("L'objet n'est pas une liste de cartes.")
        if cartes is None:
            self.cartes = 2 * [Carte(valeur, couleur)
                               for valeur in Carte.VALEURS()
                               for couleur in Carte.COULEURS()]
        else:
            self.cartes = cartes

    @property
    def cartes(self):
        return deepcopy(Carte.__cartes)

    def __eq__(self, other):
        return (isinstance(other, _ListeCartes)
                and all(carte1 == carte2
                        for carte1 in self.cartes
                        for carte2 in other.cartes))

    def __str__(self):
        pass

    def __len__(self):
        pass

    def melanger(self):
        pass

    def ajouter_carte(self, carte):
        pass

    def retirer_carte(self, indice):
        pass
