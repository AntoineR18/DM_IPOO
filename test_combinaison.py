"""Implémentation des tests pour la classe Combinaison."""

# ici je pense qu'il faut tester à la fois les erreurs levées et les resultats
# des méthodes

# le principal problème que j'ai est très con, c'est que je suis pas sûre de
# comment noter les cartes
# genre est ce que c'est (roi de pique, as de pique, 2 de pique) ou
# (('2', 'Coeur'), ('3, 'Coeur'), ('4', 'Coeur'))

import re
import pytest
from carte import Carte
from combinaison import Combinaison


# test d'erreur, pas sûre sûre à checker, verifie si combinaison à les bons paramètres
@pytest.mark.parametrize(
    "params, erreur, message_erreur",
    [
        (
            {"cartes": '9'},
            TypeError,
            "L'objet n'est pas une combinaison."
        ),
        (
            {"cartes": ('escalier')},
            TypeError,
            f"{Carte.carte} n'est pas une carte."  # ici il ya un problème
        )
    ]
)
def test_Combinaison_parametres(params, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Combinaison(**params)


# test de __est_brelan(), regarde si la méthode donne le bon resultat_attendu
@pytest.mark.parametrize(  # pas sure sure hein
    "combinaison, resultat_attendu",
    [
        ((('9', 'Trêfle'), ('9', 'Coeur'), ('9', 'Pique')), True),
        ((('9', 'Trêfle'), ('9', 'Trêfle'), ('9', 'Pique')), False)
    ]
)
def test_est_brelan_resultat(combinaison, resultat_attendu):
    assert Combinaison.__est_brelan(combinaison) == resultat_attendu


# test de __est_carre(), regarde si la méthode donne le bon resultat_attendu
@pytest.mark.parametrize(  # pas sure sure hein
    "combinaison, resultat_attendu",
    [
        ((('9', 'Trêfle'), ('9', 'Coeur'), ('9', 'Pique'), ('9', 'Carreau')), True),
        ((('9', 'Trêfle'), ('8', 'Trêfle'), ('2', 'Pique')), False)
    ]
)
def test_est_carre_resultat(combinaison, resultat_attendu):
    assert Combinaison.__est_carre(combinaison) == resultat_attendu


# test de __est_sequence(), regarde si la méthode donne le bon resultat_attendu
@pytest.mark.parametrize(  # pas sure sure hein
    "combinaison, resultat_attendu",
    [
        ((('2', 'Coeur'), ('3', 'Coeur'), ('4', 'Coeur'), ('5', 'Coeur')), True),
        ((('9', 'Trêfle'), ('8', 'Trêfle')), False),
        ((('2', 'Coeur'), ('3', 'Coeur'), ('As', 'Coeur'), ('Roi', 'Coeur')), False),
    ]
)
def test_est_sequence_resultat(combinaison, resultat_attendu):
    assert Combinaison.__est_sequence(combinaison) == resultat_attendu


# test de __est_valide(), regarde si la méthode donne le bon resultat_attendu

@pytest.mark.parametrize(  # pas sure sure hein
    "combinaison, resultat_attendu",
    [
        ((('2', 'Coeur'), ('3', 'Coeur'), ('4', 'Coeur'), ('5', 'Coeur')), True),
        # séquence
        ((('9', 'Trêfle'), ('8', 'Trêfle')), False),
        ((('9', 'Trêfle'), ('9', 'Coeur'), ('9', 'Pique')), True),  # brelan
    ]
)
def test_est_valide_resultat(combinaison, resultat_attendu):
    assert Combinaison.__est_valide(combinaison) == resultat_attendu
