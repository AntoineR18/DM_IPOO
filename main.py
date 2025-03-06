from base import _ListeCartes
from combinaison import Combinaison


class Main(_ListeCartes):
    """Implémentation de la classe Main."""

    def __init__(self, cartes):
        super().__init__(cartes)

    def __eq__(self, other):
        return (isinstance(other, Main) and
                all(carte in other.cartes for carte in self.__cartes))

    def piocher(self, reserve):
        carte = reserve.retirer_carte(reserve.__len__()-1)
        self.__cartes.ajouter_carte(carte)

    def jeter(self, indice, defausse):
        carte = self.__cartes.retirer_carte(indice)
        defausse.ajouter_carte(carte)

    def poser(self, indices_combinaisons, premiere_pose):
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
