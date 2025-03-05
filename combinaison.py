from copy import deepcopy
from carte import Carte


class Combinaison:
    """Implémentation de la classe Combinaison."""

    def __init__(self, cartes):
        if (not isinstance(cartes, tuple) or (not all(isinstance(carte, Carte)
                                              for carte in cartes))):
            raise ValueError("L'objet n'est pas une combinaison.")
        self.cartes = cartes

    @property
    def cartes(self):
        return deepcopy(self.cartes)

    def __eq__(self, autre_objet):
        return (isinstance(autre_objet, Combinaison)
                and (self.len() + autre_objet.len() == 0
                     or (self.est_valide() and autre_objet.est_valide()
                         and self.cartes == autre_objet.cartes)))

    def __str__(self):
        return "(" + ", ".join([f"{carte.str()}" for carte in self.cartes]) + ")"

    def __len__(self):
        return len(self.cartes)

    def est_brelan(self):
        return (self.len() == 3
                and len(set([carte.valeur for carte in self.cartes])) == 1
                and len(set([carte.couleur for carte in self.cartes])) != 3)

    def est_carre(self):
        return (self.len() == 4
                and len(set([carte.valeur for carte in self.cartes])) == 1
                and len(set([carte.couleur for carte in self.cartes])) != 4)

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
