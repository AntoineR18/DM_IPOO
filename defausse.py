from base import _ListeCartes


class Defausse(_ListeCartes):
    """
    Implémentation de la classe Defausse.

    Attributes
    ----------
    cartes : _ListeCartes
        liste des cartes dans la défausse

    """

    def __init__(self, cartes):
        super().__init__(cartes)

    def vider(self, reserve):
        """
        La méthode publique vider() de la classe Defausse permet de vider la
        défausse et de l'ajouter à la fin de la réserve après l'avoir mélangée.
        Autrement dit, il faut mélanger la défausse avant de la vider à la fin
        de la réserve.

        Parameters
        ----------
        self : _ListeCartes
            défausse que l'on veut vider

        reserve : _ListeCartes
            réserve à la fin de laquelle on ajoute la défausse mélangée pour la vider

        """
        self.melanger()
        for k in range(0, self.__len__()):
            carte = self.retirer_carte(0)
            reserve.ajouter_carte(carte)


if __name__ == "__main__":

    from carte import Carte
    from reserve import Reserve

    defausse = Defausse(
        [Carte("Dame", "Pique"), Carte("4", "Trêfle"), Carte("As", "Pique")]
    )
    reserve = Reserve([Carte("3", "Carreau"), Carte("7", "Pique")])

    # print(defausse.__str__())
    # print(reserve.__str__())
    # defausse.melanger()
    # print(defausse.__str__())
    # carte = defausse.retirer_carte(0)
    # print(defausse.__str__())
    # print(carte.__str__())
    # reserve.ajouter_carte(carte)
    # print(reserve.__str__())

    defausse.vider(reserve)
    print(defausse)
