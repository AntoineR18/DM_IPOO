"""Implémentation des tests pour la classe Combinaison."""

# ici je pense qu'il faut tester à la fois les erreurs levées et les resultats
# des méthodes

# le principal problème que j'ai est très con, c'est que je suis pas sûre de
# comment noter les cartes
# genre est ce que c'est (roi de pique, as de pique, 2 de pique) ou
# (('2', 'Coeur'), ('3, 'Coeur'), ('4', 'Coeur'))

import re
import pytest
from combinaison import Combinaison


# test d'erreur de l'initialisation de la classe Combinaison
# est d'erreur, pas sûre sûre à checker, verifie si combinaison à les bons paramètres
@pytest.mark.parametrize(
    "cartes, erreur, message_erreur",
    [
        (
            [pytest.as_coeur, pytest.as_pique],
            TypeError,
            "L'argument 'cartes' doit être un tuple.",
        ),
        (
            {pytest.as_coeur, pytest.as_pique},
            TypeError,
            "L'argument 'cartes' doit être un tuple.",
        ),
        (
            pytest.as_coeur,
            TypeError,
            "L'argument 'cartes' doit être un tuple.",
        ),
        (
            {pytest.as_coeur: 1, pytest.as_pique: 2},
            TypeError,
            "L'argument 'cartes' doit être un tuple.",
        ),
        (
            (pytest.neuf_pique, "procrastiner_le_DM_d_IPOO", pytest.as_coeur),
            TypeError,
            "procrastiner_le_DM_d_IPOO doit être une carte.",
        ),
        (
            (pytest.neuf_pique, "7 de Coeur", pytest.as_coeur),
            TypeError,
            "7 de Coeur doit être une carte.",
        ),
    ],
)
def test_combinaison_init_echec(cartes, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Combinaison(cartes)


def test_combinaison_init_succes():
    pass


# test de __est_brelan(), regarde si la méthode donne le bon resultat_attendu
@pytest.mark.parametrize(
    "combinaison, resultat_attendu",
    [
        (Combinaison((pytest.neuf_trefle, pytest.neuf_coeur, pytest.neuf_pique)), True),
        (
            Combinaison((pytest.neuf_trefle, pytest.huit_coeur, pytest.neuf_pique)),
            False,
        ),
    ],
)
def test_Combinaison_est_brelan_resultat(combinaison, resultat_attendu):
    assert Combinaison.est_brelan(combinaison) == resultat_attendu


# test de __est_carre(), regarde si la méthode donne le bon resultat_attendu
@pytest.mark.parametrize(  # pas sure sure hein
    "combinaison, resultat_attendu",
    [
        (
            Combinaison(
                (
                    pytest.neuf_trefle,
                    pytest.neuf_coeur,
                    pytest.neuf_pique,
                    pytest.neuf_carreau,
                )
            ),
            True,
        ),
        (
            Combinaison((pytest.neuf_trefle, pytest.huit_trefle, pytest.deux_pique)),
            False,
        ),
    ],
)
def test_Combinaison_est_carre_resultat(combinaison, resultat_attendu):
    assert Combinaison.est_carre(combinaison) == resultat_attendu


# test de __est_sequence(), regarde si la méthode donne le bon resultat_attendu
@pytest.mark.parametrize(  # pas sure sure hein
    "combinaison, resultat_attendu",
    [
        (
            Combinaison(
                (
                    pytest.deux_coeur,
                    pytest.trois_coeur,
                    pytest.quatre_coeur,
                    pytest.cinq_coeur,
                )
            ),
            True,
        ),
        (Combinaison((pytest.neuf_trefle, pytest.huit_trefle)), False),
        (
            Combinaison(
                (
                    pytest.deux_coeur,
                    pytest.trois_coeur,
                    pytest.as_coeur,
                    pytest.roi_coeur,
                )
            ),
            False,
        ),
    ],
)
def test_Combinaison_est_sequence_resultat(combinaison, resultat_attendu):
    assert Combinaison.est_sequence(combinaison) == resultat_attendu


# test de __est_valide(), regarde si la méthode donne le bon resultat_attendu


@pytest.mark.parametrize(  # pas sure sure hein
    "combinaison, resultat_attendu",
    [
        (
            Combinaison(
                (
                    pytest.deux_coeur,
                    pytest.trois_coeur,
                    pytest.quatre_coeur,
                    pytest.cinq_coeur,
                )
            ),
            True,
        ),
        # séquence
        (Combinaison((pytest.neuf_trefle, pytest.huit_trefle)), False),
        (
            Combinaison((pytest.neuf_trefle, pytest.neuf_coeur, pytest.neuf_pique)),
            True,
        ),  # brelan
    ],
)
def test_Combinaison_est_valide_resultat(combinaison, resultat_attendu):
    assert Combinaison.est_valide(combinaison) == resultat_attendu


# test de calcule_nombre_point(), regarde  si la méthode lève les bonnes erreurs
@pytest.mark.parametrize(
    "self, erreur, message_erreur",
    [
        (
            Combinaison((pytest.neuf_trefle, pytest.huit_trefle)),
            ValueError,
            "La combinaison n'est pas valide.",
        )
    ],
)
def test_Combinaison_calcule_nb_points_parametres(self, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Combinaison.calcule_nombre_points(**self)


# test de calcule_nombre_point(), regardesi la mèthode donne les bons résultats
@pytest.mark.parametrize(
    "combinaison, resultat_attendu",
    [
        (
            Combinaison(
                (
                    pytest.deux_coeur,
                    pytest.trois_coeur,
                    pytest.quatre_coeur,
                    pytest.as_coeur,
                )
            ),
            10,
        ),
        (
            Combinaison(
                (pytest.as_trefle, pytest.as_coeur, pytest.as_pique, pytest.as_carreau)
            ),
            44,
        ),
        (
            Combinaison(
                (
                    pytest.deux_coeur,
                    pytest.trois_coeur,
                    pytest.quatre_coeur,
                    pytest.cinq_coeur,
                )
            ),
            14,
        ),
        (
            Combinaison(
                (
                    pytest.valet_pique,
                    pytest.dame_pique,
                    pytest.roi_pique,
                    pytest.as_pique,
                )
            ),
            41,
        ),
        (Combinaison((pytest.neuf_trefle, pytest.neuf_coeur, pytest.neuf_pique)), 27),
    ],
)
def test_Combinaison_calcule_nb_points_resultat(combinaison, resultat_attendu):
    assert Combinaison.calcule_nombre_points(combinaison) == resultat_attendu
