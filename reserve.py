from base import _ListeCartes
from main import Main


class Reserve(_ListeCartes):
    """Implémentation de la classe Reserve."""

    def __init__(self, cartes):
        super().__init__(cartes)

    def distribuer(self, n_joueurs, idx_premier_joueur, n_cartes):
        if not (isinstance(n_joueurs, int) and
                n_joueurs >= 2 and n_joueurs <= 5):
            raise ValueError(f"{n_joueurs} doit être un entier compris entre 2 et 5.")
        if not (isinstance(idx_premier_joueur, int) and
                idx_premier_joueur >= 0 and idx_premier_joueur < 5):
            raise ValueError(f"{idx_premier_joueur} doit être un entier positif "
                             "strictement inférieur au nombre de joueurs.")
        if n_cartes not in ["14/15", "13/14"]:
            raise ValueError(f"{n_cartes} doit valoir '14/15' ou '13/14'.")
        if self.__cartes.__len__() < n_cartes:
            raise ValueError("Il n'y a pas assez de cartes dans la réserve.")
        if n_cartes == "14/15":
            n = 14
        else:
            n = 13
        mains = [Main() for i in range(0, n_joueurs)]
        while mains[idx_premier_joueur].__len__() < n:
            i = idx_premier_joueur
            while i < n_joueurs:
                mains[i].piocher(self.__cartes)
                i += 1
            i = 0
            while i < idx_premier_joueur:
                mains[i].piocher(self.__cartes)
                i += 1
        mains[idx_premier_joueur].piocher(self.__cartes)
        return mains
