"""Implémentation des tests pour la classe Reserve."""

import pytest
from reserve import Reserve
from carte import Carte


@pytest.mark.parametrize(
    "param, n_joueurs, idx_premier_joueur, n_cartes, erreur, message_erreur",
    [
        (
            [pytest.as_pique, pytest.as_carreau, pytest.neuf_coeur],
            "procrastiner_le_DM_d_IPOO",
            1,
            "14/15",
            ValueError,
            "L'argument 'n_joueurs' doit être un entier compris entre 2 et 5.",
        ),
        (
            [pytest.as_pique, pytest.as_carreau, pytest.neuf_coeur],
            4,
            "procrastiner_le_DM_d_IPOO",
            "14/15",
            ValueError,
            "L'argument 'idx_premier_joueur' doit être un entier positif"
            " strictement inférieur au nombre de joueurs.",
        ),
        (
            [pytest.as_pique, pytest.as_carreau, pytest.neuf_coeur],
            4,
            1,
            "procrastiner_le_DM_d_IPOO",
            ValueError,
            "L'argument 'n_cartes' doit valoir '14/15' ou '13/14'.",
        ),
        (
            [pytest.as_pique, pytest.as_carreau, pytest.neuf_coeur],
            4,
            1,
            13,
            ValueError,
            "L'argument 'n_cartes' doit valoir '14/15' ou '13/14'.",
        ),
        (
            [pytest.as_pique, pytest.as_carreau, pytest.neuf_coeur],
            4,
            1,
            "13/14",
            ValueError,
            "Il n'y a pas assez de cartes dans la réserve.",
        ),
        (
            [pytest.as_pique, pytest.as_carreau, pytest.neuf_coeur],
            4,
            1,
            "14/15",
            ValueError,
            "Il n'y a pas assez de cartes dans la réserve.",
        ),
    ],
)
def test_reserve_distribuer_erreur(
    param, n_joueurs, idx_premier_joueur, n_cartes, erreur, message_erreur
):
    reserve = Reserve(param)
    with pytest.raises(erreur, match=message_erreur):
        reserve.distribuer(n_joueurs, idx_premier_joueur, n_cartes)


@pytest.mark.parametrize(
    "param, n_joueurs, idx_premier_joueur, n_cartes, n_cartes_attendues",
    [
        (
            [
                Carte(valeur, couleur)
                for valeur in Carte.VALEURS()
                for couleur in Carte.COULEURS()
            ]
            * 2,
            3,
            1,
            "14/15",
            [14, 15, 14],
        ),
        (
            [
                Carte(valeur, couleur)
                for valeur in Carte.VALEURS()
                for couleur in Carte.COULEURS()
            ]
            * 2,
            4,
            0,
            "13/14",
            [14, 13, 13, 13],
        ),
    ],
)
def test_reserve_distribuer_resultat(
    param, n_joueurs, idx_premier_joueur, n_cartes, n_cartes_attendues
):
    reserve = Reserve(param)
    mains = reserve.distribuer(n_joueurs, idx_premier_joueur, n_cartes)
    assert [main.__len__() for main in mains] == n_cartes_attendues
