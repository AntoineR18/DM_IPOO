"""Implémentation des tests pour la classe Combinaison."""

import pytest
from combinaison import Combinaison


# @pytest.mark.parametrize(
#     "cartes, erreur, message_erreur",
#     [
#         (
#             [pytest.as_coeur, pytest.as_pique],
#             TypeError,
#             "L'argument 'cartes' doit être un tuple.",
#         ),
#         (
#             {pytest.as_coeur, pytest.as_pique},
#             TypeError,
#             "L'argument 'cartes' doit être un tuple.",
#         ),
#         (
#             pytest.as_coeur,
#             TypeError,
#             "L'argument 'cartes' doit être un tuple.",
#         ),
#         (
#             {pytest.as_coeur: 1, pytest.as_pique: 2},
#             TypeError,
#             "L'argument 'cartes' doit être un tuple.",
#         ),
#         (
#             (pytest.neuf_pique, "procrastiner_le_DM_d_IPOO", pytest.as_coeur),
#             TypeError,
#             "procrastiner_le_DM_d_IPOO doit être une carte.",
#         ),
#         (
#             (pytest.neuf_pique, "7 de Coeur", pytest.as_coeur),
#             TypeError,
#             "7 de Coeur doit être une carte.",
#         ),
#     ],
# )
# def test_combinaison_init_echec(cartes, erreur, message_erreur):
#     with pytest.raises(erreur, match=re.escape(message_erreur)):
#         Combinaison(cartes)


# @pytest.mark.parametrize()
# def test_combinaison_init_succes():
#     pass


# @pytest.mark.parametrize()
# def test_combinaison_eq():
#     pass


# @pytest.mark.parametrize()
# def test_combinaison_str():
#     pass


# @pytest.mark.parametrize()
# def test_combinaison_len():
#    pass


@pytest.mark.parametrize(
    "combinaison, resultat_attendu",
    [
        (Combinaison((pytest.neuf_trefle, pytest.neuf_coeur, pytest.neuf_pique)), True),
        (Combinaison((pytest.neuf_coeur, pytest.neuf_coeur, pytest.neuf_pique)), False),
        (Combinaison((pytest.neuf_trefle, pytest.neuf_coeur)), False),
        (
            Combinaison((pytest.neuf_trefle, pytest.huit_coeur, pytest.neuf_pique)),
            False,
        ),
    ],
)
def test_combinaison_est_brelan(combinaison, resultat_attendu):
    assert combinaison._Combinaison__est_brelan() == resultat_attendu


@pytest.mark.parametrize(
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
            Combinaison(
                (
                    pytest.neuf_trefle,
                    pytest.neuf_coeur,
                    pytest.neuf_pique,
                )
            ),
            False,
        ),
        (
            Combinaison(
                (
                    pytest.neuf_coeur,
                    pytest.neuf_coeur,
                    pytest.neuf_pique,
                    pytest.neuf_carreau,
                )
            ),
            False,
        ),
        (
            Combinaison((pytest.neuf_trefle, pytest.huit_trefle, pytest.deux_pique)),
            False,
        ),
    ],
)
def test_combinaison_est_carre(combinaison, resultat_attendu):
    assert combinaison._Combinaison__est_carre() == resultat_attendu


@pytest.mark.parametrize(
    "combinaison, resultat_attendu",
    [
        (
            Combinaison(
                (
                    pytest.valet_pique,
                    pytest.dame_pique,
                    pytest.roi_pique,
                    pytest.as_pique,
                )
            ),
            True,
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
            True,
        ),
        (Combinaison((pytest.neuf_trefle, pytest.huit_trefle)), False),
        (
            Combinaison(
                (
                    pytest.deux_coeur,
                    pytest.trois_carreau,
                    pytest.quatre_coeur,
                    pytest.cinq_coeur,
                )
            ),
            False,
        ),
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
def test_combinaison_est_sequence(combinaison, resultat_attendu):
    assert combinaison.est_sequence() == resultat_attendu


@pytest.mark.parametrize(
    "combinaison, resultat_attendu",
    [
        (
            Combinaison(
                (
                    pytest.valet_pique,
                    pytest.dame_pique,
                    pytest.roi_pique,
                    pytest.as_pique,
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
                    pytest.quatre_coeur,
                    pytest.cinq_coeur,
                )
            ),
            True,
        ),
        (
            Combinaison((pytest.neuf_trefle, pytest.neuf_coeur, pytest.neuf_pique)),
            True,
        ),
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
    ],
)
def test_combinaison_est_valide(combinaison, resultat_attendu):
    assert combinaison.est_valide() == resultat_attendu


@pytest.mark.parametrize(
    "combinaison, erreur, message_erreur",
    [
        (
            Combinaison((pytest.neuf_trefle, pytest.huit_trefle)),
            ValueError,
            "La combinaison n'est pas valide.",
        )
    ],
)
def test_combinaison_calcule_nb_points_erreur(combinaison, erreur, message_erreur):
    with pytest.raises(erreur, match=message_erreur):
        combinaison.calcule_nombre_points()


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
                (
                    pytest.cinq_trefle,
                    pytest.cinq_coeur,
                    pytest.cinq_pique,
                    pytest.cinq_carreau,
                )
            ),
            20,
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
            40,
        ),
        (Combinaison((pytest.neuf_trefle, pytest.neuf_coeur, pytest.neuf_pique)), 27),
    ],
)
def test_combinaison_calcule_nb_points_resultat(combinaison, resultat_attendu):
    assert combinaison.calcule_nombre_points() == resultat_attendu
