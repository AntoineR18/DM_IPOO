from copy import deepcopy
from carte import Carte
import random


class _ListeCartes:
    """
    Implémentation de la classe _ListeCartes.

    Attributes
    ----------
    cartes : list[Carte]

    """

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
        """
        La méthode publique melanger() permet de mélanger les cartes.

        Parameters
        ----------
        self : _ListeCartes

        """
        random.shuffle(self.__cartes)

    def ajouter_carte(self, carte):
        """
        La méthode publique ajouter_carte() permet d'ajouter une carte à la fin
        de la liste de cartes.

        Parameters
        ----------
        self : _ListeCartes
            liste de carte à laquelle on ajoute une carte

        carte : Carte
            carte qu'on ajoute à notre liste de cartes

        """
        if not isinstance(carte, Carte):
            raise TypeError(f"{carte} n'est pas une carte.")
        self.__cartes.append(carte)

    def retirer_carte(self, indice):
        """
        La méthode publique retirer_carte() permet de retirer une carte de la
        liste de cartes et de la renvoyer.

        Parameters
        ----------
        self : _ListeCartes
            liste de cartes dans laquelle on retire une carte

        indice : int
            position de la carte retirée dans la liste de cartes

        """
        if self.__len__() == 0:
            raise ValueError("La liste de cartes est vide.")
        if not (isinstance(indice, int) and indice > 0 and indice < self.__len__()):
            raise ValueError(f"L'indice {indice} n'est pas valide.")
        self.__cartes.pop(indice)
