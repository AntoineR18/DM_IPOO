from base import _ListeCartes
from combinaison import Combinaison


class Main(_ListeCartes):
    """
    Implémentation de la classe Main.

    Attributes
    ----------
    cartes : _ListeCartes
        liste des cartes dans la main du joueur

    """

    def __init__(self, cartes):
        super().__init__(cartes)

    def __eq__(self, other):
        return (isinstance(other, Main) and
                all(carte in other.cartes for carte in self.__cartes))

    def piocher(self, reserve):
        """
        Permet de piocher la première carte de la réserve.
        La première carte de la réserve est enlevée de la réserve et ajoutée
        à la fin de la main.

        Parameters
        ----------
        self : Main
            liste des cartes dans la main du joueur à laquelle on ajoute la
            carte piochée

        reserve : Reserve
            liste des cartes dans la réserve à laquelle on enlève la carte piochée

        """
        carte = reserve.retirer_carte(reserve.__len__()-1)
        self.__cartes.ajouter_carte(carte)

    def jeter(self, indice, defausse):
        """
        Permet de jeter une carte de la main dans la défausse.
        La carte correspondant à l'indice est enlevée de la main et est ajoutée
        à la fin de la défausse.

        Parameters
        ----------
        self : Main
            liste des cartes dans la main du joueur à laquelle on retire la carte jetée

        indice : int
            indice de la carte jetée

        defausse : Defausse
            liste des cartes de la défausse à la fin de laquelle on ajoute la
            carte jetée

        """
        if not (indice > 0 and indice < self.__len__()):
            raise ValueError(f"L'indice {indice} doit être un entier positif "
                             "inférieur à la longueur de la main.")
        carte = self.__cartes.retirer_carte(indice)
        defausse.ajouter_carte(carte)

    def poser(self, indices_combinaisons, premiere_pose):
        """
        Permet de poser des combinaisons de cartes.

        Parameters
        ----------
        self : Main
            liste des cartes dans la main du joueur d'où on tire la combinaison à poser

        indices_combinaisons : list[list[int]]
            liste de listes des indices des cartes à poser, chaque liste
            correspond à une combinaison

        premiere_pose : bool
            indique si c'est la première fois que le joueur pose une combinaison

        Returns
        -------
        (list[Combinaison], int)

        """
        occurrences = {}
        combinaisons = []
        points = 0
        for liste in indices_combinaisons:
            combi = Combinaison()
            for i in liste:
                if not (isinstance(i, int) and
                        i >= 0 and i < self.__cartes.__len__()):
                    raise ValueError(f"L'indice {i} doit être un entier positif "
                                     "strictement inférieur au nombre de cartes "
                                     "dans la main.")
                if occurrences[i]:
                    raise ValueError(f"La carte d'indice {i} est posée deux fois.")
                else:
                    occurrences[i] = True
                carte = self.__cartes.retirer_carte(i)
                combi.ajouter_carte(carte)
            if not combi.est_valide():
                raise ValueError(f"La combinaison {combi} n'est pas valide.")
            combinaisons.append(combi)
            points += combi.calcul_nombre_points()
        if premiere_pose:
            if not any(combi.est_sequence() for combi in combinaisons):
                raise ValueError("La première pose doit contenir une séquence.")
            assert points >= 51, "La première pose doit rapporter au moins 51 points."
        return combinaisons, points
