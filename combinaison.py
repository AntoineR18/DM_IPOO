from copy import deepcopy
from carte import Carte


class Combinaison:
    """
    Implémentation de la classe Combinaison.

    Attributes
    ----------
    cartes : tuple[Carte]

    """

    def __init__(self, cartes):
        if not isinstance(cartes, tuple):
            raise TypeError("L'argument 'cartes' doit être un tuple.")
        for carte in cartes:
            if not isinstance(carte, Carte):
                raise TypeError(f"{carte} doit être une carte.")
        self.__cartes = cartes

    @property
    def cartes(self):
        return deepcopy(self.__cartes)

    def __eq__(self, other):
        return isinstance(other, Combinaison) and (
            self.__len__() + other.__len__() == 0
            or (
                self.est_valide() and other.est_valide() and self.cartes == other.cartes
            )
        )

    def __str__(self):
        return "(" + ", ".join([f"{carte.__str__()}" for carte in self.__cartes]) + ")"

    def __len__(self):
        return len(self.__cartes)

    def __est_brelan(self):
        """
        La méthode privée est_brelan() détermine si la combinaison est un brelan.
        Une combinaison est un brelan si et seulement si :
        1. la combinaison est constituée de trois cartes,
        2. les trois cartes ont la même valeur, et
        3. les trois cartes ont des couleurs toutes différentes les unes des autres

        Parameters
        ----------
        self : Combinaison
            combinaison de cartes à tester

        Returns
        -------
        bool


        """
        return (
            self.__len__() == 3
            and len(set([carte.valeur for carte in self.__cartes])) == 1
            and len(set([carte.couleur for carte in self.__cartes])) == 3
        )

    def __est_carre(self):
        """
        La méthode privée est_carre() détermine si la combinaison est un carré.
        Une combinaison est un carré si et seulement si :
        1. la combinaison est constituée de quatre cartes,
        2. les quatre cartes ont la même valeur, et
        3. les quatre cartes ont des couleurs toutes différentes les unes des autres.

        Parameters
        ----------
        self : Combinaison
            combinaison de cartes à tester

        Returns
        -------
        bool


        """
        return (
            self.__len__() == 4
            and len(set([carte.valeur for carte in self.__cartes])) == 1
            and len(set([carte.couleur for carte in self.__cartes])) == 4
        )

    def est_sequence(self):
        """
        La méthode publique est_sequence() détermine si la combinaison est une séquence.
        Une combinaison est une séquence si et seulement si :
        1. la combinaison est constituée d'au moins trois cartes,
        2. toutes les cartes ont la même couleur, et
        3. toutes les cartes se suivent

        Parameters
        ----------
        self : Combinaison
            combinaison de cartes à tester

        Returns
        -------
        bool

        """
        n = self.__len__()
        if n < 3:
            return False
        if len(set([carte.couleur for carte in self.__cartes])) != 1:
            return False
        indices_combi = [Carte.VALEURS().index(carte.valeur) for carte in self.__cartes]
        indices_combi.sort()
        return all(
            indices_combi[i] + 1 == indices_combi[i + 1] for i in range(0, n - 1)
        ) or (
            all(indices_combi[i] + 1 == indices_combi[i + 1] for i in range(1, n - 1))
            and indices_combi[0] == 0
        )

    def est_valide(self):
        """
        La méthode publique est_valide() détermine si la combinaison est valide.
        Une combinaison est valide si et seulement si c'est soit un brelan,
        soit un carré, soit une séquence.

        Parameters
        ----------
        self : Combinaison
            combinaison de cartes à tester pour savoir si elle est valide

        Returns
        -------
        bool


        """
        return self.__est_brelan() or self.__est_carre() or self.est_sequence()

    def calcule_nombre_points(self):
        """
        La méthode publique calcule_nombre_points() calcule et renvoie le nombre
        de points d'une combinaison valide.

        Parameters
        ----------
        self : Combinaison
            combinaison de cartes à partir de laquelle on calcule un nombe de points

        Returns
        -------
        int


        """
        if not self.est_valide():
            raise ValueError("La combinaison n'est pas valide.")
        points = (
            {valeur: int(valeur) for valeur in Carte.VALEURS()[1:10]}
            | {valeur: 10 for valeur in Carte.VALEURS()[10:]}
            | {"As": 10}
        )
        valeurs = [carte.valeur for carte in self.__cartes]
        if self.__est_brelan():
            return 3 * points[valeurs[0]]
        elif self.__est_carre():
            return 4 * points[valeurs[0]]
        else:
            if "As" in valeurs and "2" in valeurs:
                valeurs.pop(valeurs.index("As"))
                return sum([points[valeur] for valeur in valeurs]) + 1
            else:
                return sum([points[valeur] for valeur in valeurs])
