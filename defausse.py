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
        self.__cartes.melanger()
        i = 0
        for carte in self.__cartes:
            reserve.ajouter_carte(carte)
            i += 1
        for k in range(i-1):
            #j'ai rajouté ce truc miteux pour que la défausse soit vidée mais je suis sure que c'est faux
            Defausse.retirer_carte(k)
