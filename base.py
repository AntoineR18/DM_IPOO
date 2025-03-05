from copy import deepcopy
from cartes import Carte
import random


class _ListeCartes:
    """Implémentation de la classe _ListeCartes."""

    def __init__(self, cartes):
        if cartes is None:
            self.cartes = 2 * [Carte(valeur, couleur)
                               for valeur in Carte.VALEURS()
                               for couleur in Carte.COULEURS()]
        if not isinstance(cartes, list):
            raise TypeError("L'objet n'est pas une liste de cartes.")
        for carte in cartes:
            if not isinstance(carte, Carte):
                raise TypeError(f"{carte} n'est pas une carte.")
        else:
            self.__cartes = cartes

    @property
    def cartes(self):
        return deepcopy(self.__cartes)

    def __eq__(self, other):
        return (isinstance(other, _ListeCartes)
                and all(carte1 == carte2
                        for carte1 in self.__cartes
                        for carte2 in other.__cartes))

    def __str__(self):
        return "[" + ", ".join(carte.__str__() for carte in self.__cartes) + "]"

    def __len__(self):
        return len(self.__cartes)

    def melanger(self):
        random.shuffle(self.__cartes)

    def ajouter_carte(self, carte):
        if not isinstance(carte, Carte):
            raise TypeError(f"{carte} n'est pas une carte.")
        self.__cartes.append(carte)

    def retirer_carte(self, indice):
        if self.__len__() == 0:
            raise ValueError("La liste de cartes est vide.")
        if not (isinstance(indice, int) and indice > 0 and indice < self.__len__()):
            raise ValueError(f"L'indice {indice} n'est pas valide.")
        self.__cartes.pop(indice)
