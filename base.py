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
            self.__cartes = [
                Carte(valeur, couleur)
                for valeur in Carte.VALEURS()
                for couleur in Carte.COULEURS()
            ] * 2
        else:
            if not isinstance(cartes, list):
                raise ValueError(
                    "L'argument 'cartes' doit être None ou une liste de cartes."
                )
            for carte in cartes:
                if not isinstance(carte, Carte):
                    raise ValueError(
                        "L'argument 'cartes' doit être None ou une liste de cartes."
                    )
            else:
                self.__cartes = cartes

    @property
    def cartes(self):
        return deepcopy(self.__cartes)

    def __eq__(self, other):
        return isinstance(other, _ListeCartes) and self.__cartes == other.__cartes

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
            raise TypeError("L'argument 'carte' doit être une instance de Carte.")
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
            raise Exception(
                "La liste de cartes est vide, aucune carte ne peut être retirée."
            )
        if not (isinstance(indice, int) and indice >= 0 and indice < self.__len__()):
            raise ValueError(
                "L'indice de la carte à retirer n'est pas valide. L'indice doit être"
                f" un entier compris entre 0 et {self.__len__()-1} inclus, mais"
                f" l'indice est {repr(indice)}."
            )
        return self.__cartes.pop(indice)
