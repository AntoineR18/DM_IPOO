from copy import deepcopy
from carte import Carte


class Combinaison:
    """Implémentation de la classe Combinaison."""

    def __init__(self, cartes):
        if not isinstance(cartes, tuple):
            raise TypeError("L'objet n'est pas une combinaison.")
        for carte in cartes:
            if not isinstance(carte, Carte):
                raise TypeError(f"{carte} n'est pas une carte.")
        self.__cartes = cartes

    @property
    def cartes(self):
        return deepcopy(self.__cartes)

    def __eq__(self, other):
        return (isinstance(other, Combinaison)
                and (self.__len__() + other.__len__() == 0
                     or (self.est_valide() and other.est_valide()
                         and self.cartes == other.cartes)))

    def __str__(self):
        return "(" + ", ".join([f"{carte.__str__()}" for carte in self.__cartes]) + ")"

    def __len__(self):
        return len(self.__cartes)

    def __est_brelan(self):
        return (self.__len__() == 3
                and len(set([carte.valeur for carte in self.__cartes])) == 1
                and len(set([carte.couleur for carte in self.__cartes])) != 3)

    def __est_carre(self):
        return (self.__len__() == 4
                and len(set([carte.valeur for carte in self.__cartes])) == 1
                and len(set([carte.couleur for carte in self.__cartes])) != 4)

    def est_sequence(self):
        n = self.__len__()
        if n < 3:
            return False
        if len(set([carte.valeur for carte in self.__cartes])) != 1:
            return False
        if "As" in self.__cartes:
            return ((Carte.VALEURS()[0:n] == self.__cartes)
                    or (Carte.VALEURS()[len(Carte.VALEURS())-n:]) == self.__cartes)
        else:
            return any(Carte.VALEURS()[i:i+n] == self.__cartes
                       for i in range(1, len(Carte.VALEURS())-n))

    def est_valide(self):
        return self.__est_brelan() or self.__est_carre() or self.est_sequence()

    def calcule_nombre_points(self):
        if not self.est_valide():
            raise ValueError("La combinaison n'est pas valide.")
        points = ({valeur: int(valeur) for valeur in Carte.VALEURS()[1:10]} +
                  {valeur: 10 for valeur in Carte.VALEURS()[10:]} + {'As': 10})
        if self.__est_brelan():
            return 3*points[self.__cartes[0]]
        elif self.__est_carre():
            return 4*points[self.__cartes[0]]
        else:
            res = 0
            if 'As' in self.__cartes and '2' in self.__cartes:
                for carte in self.__cartes:
                    if carte.valeur == 'As':
                        res += 1
                    res += points[carte]
                return res
            else:
                for carte in self.__cartes:
                    res += points[carte]
                return res
