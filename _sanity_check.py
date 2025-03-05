"""Implémentation de vérifications basiques sur le code."""


from inspect import ismethod

from base import _ListeCartes
from carte import Carte
from combinaison import Combinaison
from defausse import Defausse
from main import Main
from reserve import Reserve


def sanity_check():
    # Instances
    carte = Carte("3", "Carreau")
    combinaison = Combinaison((Carte("3", "Carreau"), Carte("2", "Carreau")))
    liste_cartes = _ListeCartes([Carte("3", "Coeur"), Carte("2", "Pique")])

    # Carte - attributs d'instance
    carte_instance_attr = ("_Carte__valeur", "_Carte__couleur")
    for attribut in carte_instance_attr:
        assert hasattr(carte, attribut) and not callable(
            getattr(carte, attribut)
        ), f"La classe Carte n'a pas l'attribut d'instance {attribut}."

    # Carte - propriétés
    carte_prop = ("valeur", "couleur")
    for proriete in carte_prop:
        assert isinstance(
            getattr(Carte, proriete), property
        ), f"L'attribut {proriete} de la classe Carte n'est pas une propriété."

    # Carte - attributs de classe
    carte_classe_attr = ("_Carte__VALEURS", "_Carte__COULEURS")
    for attribut in carte_classe_attr:
        assert hasattr(Carte, attribut) and not callable(
            getattr(Carte, attribut)
        ), f"La classe Carte n'a pas l'attribut de classe {attribut}."

    # Carte - méthodes de classe
    carte_classe_meth = ("VALEURS", "COULEURS")
    for methode in carte_classe_meth:
        assert ismethod(getattr(Carte, methode)), (
            f"La méthode {methode} de la classe Carte n'est pas une méthode de "
            f"classe."
        )

    # Cartes - méthodes redéfinies
    carte_meth_redef = ("__init__", "__str__", "__repr__", "__eq__", "__hash__")
    for methode in carte_meth_redef:
        assert hasattr(Carte, methode) and getattr(Carte, methode) is not getattr(
            object, methode
        ), f"La classe Carte ne redéfinit pas la méthode {methode}."

    # Combinaison - attribut
    assert hasattr(combinaison, "cartes") and not callable(
        getattr(combinaison, "cartes")
    ), "La classe Combinaison n'a pas l'attribut cartes."

    # Combinaison - propriété
    assert isinstance(
        getattr(Combinaison, "cartes"), property
    ), "L'attribut cartes de la classe Combinaison n'est pas une propriété."

    # Combinaison - méthodes nouvelles
    combinaison_meth = (
        "__len__",
        "_Combinaison__est_brelan",
        "_Combinaison__est_carre",
        "est_sequence",
        "est_valide",
        "calcule_nombre_points",
    )
    for methode in combinaison_meth:
        assert hasattr(Combinaison, methode) and callable(
            getattr(Combinaison, methode)
        ), f"La classe Combinaison n'a pas la méthode {methode}."

    # Combinaison - méthodes redéfinies
    combinaison_meth_redef = ("__init__", "__eq__", "__str__")
    for methode in combinaison_meth_redef:
        assert hasattr(Combinaison, methode) and getattr(
            Combinaison, methode
        ) is not getattr(
            object, methode
        ), f"La classe Combinaison ne redéfinit pas la méthode {methode}."

    # _ListeCartes - attribut
    assert hasattr(liste_cartes, "cartes") and not callable(
        getattr(combinaison, "cartes")
    ), "La classe Combinaison n'a pas l'attribut cartes."

    # _ListeCartes - propriété
    assert isinstance(
        getattr(Combinaison, "cartes"), property
    ), "L'attribut cartes de la classe Combinaison n'est pas une propriété."

    # _ListeCartes - methodes nouvelles
    liste_cartes_meth = (
        "__len__",
        "melanger",
        "ajouter_carte",
        "retirer_carte",
    )
    for methode in liste_cartes_meth:
        assert hasattr(_ListeCartes, methode) and callable(
            getattr(_ListeCartes, methode)
        ), f"La classe _ListeCartes n'a pas la méthode {methode}."

    # _ListeCartes - méthodes redéfinies
    liste_cartes_meth_redef = ("__init__", "__eq__", "__str__")
    for methode in liste_cartes_meth_redef:
        assert hasattr(_ListeCartes, methode) and getattr(
            _ListeCartes, methode
        ) is not getattr(
            object, methode
        ), f"La classe _ListeCartes ne redéfinit pas la méthode {methode}."

    # Main - héritage
    assert issubclass(
        Main, _ListeCartes
    ), "La classe Main n'hérite pas de la classe _ListeCartes."

    # Main - méthodes nouvelles
    main_meth = ("piocher", "jeter", "poser")
    for methode in main_meth:
        assert hasattr(Main, methode) and callable(
            getattr(Main, methode)
        ), f"La classe Main n'a pas lé méthode {methode}."

    # Main - méthodes redéfinies
    main_meth_redef = ("__init__", "__eq__")
    for methode in main_meth_redef:
        assert hasattr(Main, methode) and getattr(Main, methode) is not getattr(
            _ListeCartes, methode
        ), f"La classe Main ne redéfinit pas la méthode {methode}."

    # Reserve - héritage
    assert issubclass(
        Reserve, _ListeCartes
    ), "La classe Reserve n'hérite pas de la classe _ListeCartes."

    # Reserve - méthode nouvelle
    assert hasattr(Reserve, "distribuer") and callable(
        getattr(Reserve, "distribuer")
    ), "La classe Reserve n'a pas la méthode distribuer."

    # Reserve - méthode redéfinie
    assert hasattr(Reserve, methode) and getattr(Reserve, "__init__") is not getattr(
        _ListeCartes, "__init__"
    ), "La classe Reserve ne redéfinit pas la méthode __init__."

    # Defausse - héritage
    assert issubclass(
        Defausse, _ListeCartes
    ), "La classe Defausse n'hérite pas de la classe _ListeCartes."

    # Défausse - méthode nouvelle
    assert hasattr(Defausse, "vider") and callable(
        getattr(Defausse, "vider")
    ), "La classe Defausse n'a pas la méthode vider."

    # Défausse - méthode redéfinie
    assert hasattr(Defausse, methode) and getattr(Defausse, "__init__") is not getattr(
        _ListeCartes, "__init__"
    ), "La classe Défausse ne redéfinit pas la méthode __init__."


if __name__ == "__main__":
    sanity_check()
