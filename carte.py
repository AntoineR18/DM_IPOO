class Carte:
    """Implémentation de la classe Carte.

    Parameters
    ----------
    Examples
    --------
    """

    __VALEURS = ('As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame',
                 'Roi')

    __COULEURS = ('Pique', 'Carreau', 'Coeur', 'Trêfle')

    def __init__(self, valeur, couleur):
        if valeur not in self.__VALEURS:
            raise ValueError("La valeur de la carte n'existe pas.")
        if couleur not in self.__COULEURS:
            raise ValueError("La couleur de la carte n'existe pas.")
        self.__valeur = valeur
        self.__couleur = couleur

    @property
    def valeur(self):
        return self.__valeur

    @property
    def couleur(self):
        return self.__couleur

    @classmethod
    def VALEURS(self):
        print(self.__VALEURS)

    @classmethod
    def COULEURS(self):
        print(self.__COULEURS)

    def __str__(self):
        return f"{self.__valeur} de {self.__couleur.lower()}"

    def __repr__(self):
        return f"Carte('{self.__valeur}', '{self.__couleur}')"

    def __eq__(self, autre_objet):
        return (isinstance(autre_objet, Carte)
                and self.valeur == autre_objet.valeur
                and self.couleur == autre_objet.couleur)

    def __hash__(self):
        return hash(self.__repr__())
