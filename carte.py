class Carte:
    """
    Implémentation de la classe Carte.

    Parameters
    ----------
    VALEURS : tuple[str]
        différentes valeurs que peuvent prendre les cartes

    COULEURS : tuple[str]
        différentes couleurs que peuvent prendre les cartes

    valeur : str
        valeur de la carte

    couleur : str
        couleur de la carte

    Examples # A FAIRE PLUS TARD
    --------
    """

    __VALEURS = ('As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame',
                 'Roi')

    __COULEURS = ('Pique', 'Carreau', 'Coeur', 'Trèfle')

    def __init__(self, valeur, couleur):
        if valeur not in Carte.__VALEURS:
            raise ValueError("La valeur de la carte n'existe pas.")
        if couleur not in Carte.__COULEURS:
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
    def VALEURS():
        return Carte.__VALEURS

    @classmethod
    def COULEURS():
        return Carte.__COULEURS

    def __str__(self):
        return f"{self.__valeur} de {self.__couleur.lower()}"

    def __repr__(self):
        return f"Carte('{self.__valeur}', '{self.__couleur}')"

    def __eq__(self, other):
        return (isinstance(other, Carte)
                and self.valeur == other.valeur
                and self.couleur == other.couleur)

    def __hash__(self):
        return hash(self.__repr__())
