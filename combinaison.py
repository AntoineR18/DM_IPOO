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
        n = self.len()
        if n < 3:
            return False
        if len(set([carte.valeur for carte in self.cartes])) != 1:
            return False
        if "As" in self.cartes:
            return ((self.__VALEURS[0:n-1] == self.cartes)
                    or (self.__VALEURS[len(self.__VALEURS)-1-n:
                                       len(self.__VALEURS)-1]))
        else:
            return any(self.__VALEURS[i:i+n] for i in range(1, len(self.__VALEURS)-n))

    def est_valide(self):
        return self.est_brelan() or self.est_carre() or self.est_sequence()

    def calcule_nombre_points(self):
        if not self.est_valide():
            raise ValueError("La combinaison n'est pas valide.")
        points = ({valeur: int(valeur) for valeur in self.__VALEURS[1:10]} +
                  {valeur: 10 for valeur in self.__VALEURS[10:]} + {'As': 10})
        if self.est_brelan():
            return 3*points[self.cartes[0]]
        elif self.est_carre():
            return 4*points[self.cartes[0]]
        else:
            res = 0
            if 'As' in self.cartes and '2' in self.cartes:
                for carte in self.cartes:
                    res += points[carte]
                return res + 1
            else:
                for carte in self.cartes:
                    res += points[carte]
                return res
