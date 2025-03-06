from base import _ListeCartes


class Defausse(_ListeCartes):
    """Implémentation de la classe Defausse."""

    def __init__(self, cartes):
        super().__init__(cartes)

    def vider(self, reserve):
        self.__cartes.melanger()
        for carte in self.__cartes:
            reserve.ajouter_carte(carte)
