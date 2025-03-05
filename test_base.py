"""Implémentation des tests pour la classe _ListeCartes."""


from copy import copy

import pytest

from base import _ListeCartes
from carte import Carte


@pytest.mark.parametrize(
    "param",
    [
        pytest.as_coeur,
        (pytest.as_coeur, pytest.six_pique),
        {pytest.as_coeur, pytest.six_pique},
        {pytest.as_coeur: 1, pytest.six_pique: 2},
        ["As de coeur", "3 de trêfle"],
        ["As de coeur", pytest.as_coeur],
    ],
)
def test_liste_cartes_init_echec(param):
    with pytest.raises(
        ValueError, match="L'argument 'cartes' doit être None ou une liste de cartes."
    ):
        _ListeCartes(param)


@pytest.mark.parametrize(
    "param, resultat_attendu",
    [
        ([], []),
        ([pytest.as_coeur], [pytest.as_coeur]),
        ([pytest.as_coeur, pytest.six_pique], [pytest.as_coeur, pytest.six_pique]),
        (
            [pytest.trois_trefle, pytest.cinq_carreau, Carte("7", "Pique")],
            [pytest.trois_trefle, pytest.cinq_carreau, Carte("7", "Pique")],
        ),
        (
            None,
            [
                Carte(valeur, couleur)
                for valeur in Carte.VALEURS()
                for couleur in Carte.COULEURS()
            ]
            * 2,
        ),
    ],
)
def test_liste_cartes_init_succes(param, resultat_attendu):
    assert _ListeCartes(param)._ListeCartes__cartes == resultat_attendu


@pytest.mark.parametrize(
    "param1, param2, resultat_attendu",
    [
        ([], [], True),
        ([pytest.as_coeur], [pytest.as_coeur], True),
        (
            [pytest.as_coeur, pytest.six_pique],
            [pytest.as_coeur, pytest.six_pique],
            True,
        ),
        (
            [pytest.as_coeur, pytest.six_pique, pytest.trois_carreau],
            [pytest.as_coeur, pytest.six_pique, pytest.trois_carreau],
            True,
        ),
        ([pytest.as_coeur], [], False),
        ([pytest.as_coeur], [pytest.as_trefle], False),
        (
            [pytest.as_coeur, pytest.six_pique, pytest.trois_carreau],
            [pytest.as_coeur, pytest.trois_carreau, pytest.six_pique],
            False,
        ),
    ],
)
def test_liste_cartes_eq(param1, param2, resultat_attendu):
    if resultat_attendu:
        assert (_ListeCartes(param1) == _ListeCartes(param2)) is resultat_attendu
    else:
        assert (_ListeCartes(param1) == param2) is resultat_attendu


@pytest.mark.parametrize(
    "param, resultat_attendu",
    [
        ([], "[]"),
        ([pytest.as_coeur], "[As de coeur]"),
        ([pytest.as_coeur, pytest.six_pique], "[As de coeur, 6 de pique]"),
        (
            [pytest.as_coeur, pytest.six_pique, pytest.trois_carreau],
            "[As de coeur, 6 de pique, 3 de carreau]",
        ),
    ],
)
def test_liste_cartes_str(param, resultat_attendu):
    assert str(_ListeCartes(param)) == resultat_attendu


@pytest.mark.parametrize(
    "param, resultat_attendu",
    [
        ([], 0),
        ([pytest.as_coeur], 1),
        ([pytest.as_coeur, pytest.six_pique], 2),
        ([pytest.as_coeur, pytest.six_pique, pytest.trois_carreau], 3),
    ],
)
def test_liste_cartes_len(param, resultat_attendu):
    assert len(_ListeCartes(param)) == resultat_attendu


@pytest.mark.parametrize("n_runs", range(10))
def test_liste_cartes_melanger(n_runs):
    # Il y a deux jeux de 52 cartes différentes.
    # Le nombre de permutations possibles est égal à 104! / (2^52), soit environ
    # 2.286841104292143e+150
    # La probabilité qu'un jeu après mélange soit égal au jeu avant mélange est donc
    # l'inverse, soit environ 4.3728442615585e-151.
    # Les chances que cela se produise sont donc infiniment faibles.
    deux_jeux_de_cartes = [
        Carte(valeur, couleur)
        for valeur in Carte.VALEURS()
        for couleur in Carte.COULEURS()
    ] + [
        Carte(valeur, couleur)
        for valeur in Carte.VALEURS()
        for couleur in Carte.COULEURS()
    ]

    cartes_non_melangees = copy(deux_jeux_de_cartes)

    jeu = _ListeCartes(deux_jeux_de_cartes)
    jeu.melanger()

    assert jeu.cartes != cartes_non_melangees


@pytest.mark.parametrize(
    "carte", ["As de pique", 3, (4, "Coeur"), ("6", "Carreau"), ({Carte("2", "Coeur")})]
)
def test_liste_cartes_ajouter_carte_erreur(carte):
    liste_cartes = _ListeCartes([pytest.as_trefle, pytest.dame_carreau])
    with pytest.raises(
        TypeError, match="L'argument 'carte' doit être une instance de Carte."
    ):
        liste_cartes.ajouter_carte(carte)


@pytest.mark.parametrize(
    "param, carte, resultat_attendu",
    [
        ([], pytest.dix_pique, [pytest.dix_pique]),
        ([pytest.as_coeur], pytest.six_pique, [pytest.as_coeur, pytest.six_pique]),
        (
            [pytest.as_coeur, pytest.trois_carreau],
            pytest.roi_trefle,
            [pytest.as_coeur, pytest.trois_carreau, pytest.roi_trefle],
        ),
        (
            [pytest.dame_pique, pytest.quatre_trefle, pytest.as_pique],
            pytest.roi_coeur,
            [
                pytest.dame_pique,
                pytest.quatre_trefle,
                pytest.as_pique,
                pytest.roi_coeur,
            ],
        ),
    ],
)
def test_liste_cartes_ajouter_carte_resultat(param, carte, resultat_attendu):
    liste_cartes = _ListeCartes(param)
    liste_id_cartes_old = [id(carte) for carte in liste_cartes._ListeCartes__cartes]
    liste_cartes.ajouter_carte(carte)
    liste_id_cartes_new = [id(carte) for carte in liste_cartes._ListeCartes__cartes]
    assert liste_cartes.cartes == resultat_attendu
    assert liste_id_cartes_old + [id(carte)] == liste_id_cartes_new


@pytest.mark.parametrize(
    "param, indice, erreur, erreur_msg",
    [
        (
            [],
            0,
            Exception,
            "La liste de cartes est vide, aucune carte ne peut être retirée.",
        ),
        (
            [],
            1,
            Exception,
            "La liste de cartes est vide, aucune carte ne peut être retirée.",
        ),
        (
            [pytest.as_coeur],
            1,
            ValueError,
            "L'indice de la carte à retirer n'est pas valide. L'indice doit être un "
            "entier compris entre 0 et 0 inclus, mais l'indice est 1.",
        ),
        (
            [pytest.as_coeur],
            "1",
            ValueError,
            "L'indice de la carte à retirer n'est pas valide. L'indice doit être un "
            "entier compris entre 0 et 0 inclus, mais l'indice est '1'.",
        ),
        (
            [pytest.as_coeur, pytest.roi_pique, pytest.deux_trefle],
            3,
            ValueError,
            "L'indice de la carte à retirer n'est pas valide. L'indice doit être un "
            "entier compris entre 0 et 2 inclus, mais l'indice est 3.",
        ),
    ],
)
def test_liste_cartes_retirer_carte_erreur(param, indice, erreur, erreur_msg):
    liste_cartes = _ListeCartes(param)
    with pytest.raises(erreur, match=erreur_msg):
        liste_cartes.retirer_carte(indice)


@pytest.mark.parametrize(
    "param, indice, carte_attendue, cartes_attendues",
    [
        ([pytest.as_coeur], 0, pytest.as_coeur, []),
        (
            [pytest.as_coeur, pytest.trois_carreau],
            0,
            pytest.as_coeur,
            [pytest.trois_carreau],
        ),
        (
            [pytest.as_coeur, pytest.trois_carreau],
            1,
            pytest.trois_carreau,
            [pytest.as_coeur],
        ),
        (
            [pytest.dame_pique, pytest.quatre_trefle, pytest.as_pique],
            0,
            pytest.dame_pique,
            [pytest.quatre_trefle, pytest.as_pique],
        ),
        (
            [pytest.dame_pique, pytest.quatre_trefle, pytest.as_pique],
            1,
            pytest.quatre_trefle,
            [pytest.dame_pique, pytest.as_pique],
        ),
        (
            [pytest.dame_pique, pytest.quatre_trefle, pytest.as_pique],
            2,
            pytest.as_pique,
            [pytest.dame_pique, pytest.quatre_trefle],
        ),
    ],
)
def test_liste_cartes_retirer_carte_resultat(
    param, indice, carte_attendue, cartes_attendues
):
    liste_cartes = _ListeCartes(param)
    liste_id_cartes_old = [id(carte) for carte in liste_cartes._ListeCartes__cartes]
    carte_retiree = liste_cartes.retirer_carte(indice)
    liste_id_cartes_new = [id(carte) for carte in liste_cartes._ListeCartes__cartes]
    assert carte_retiree == carte_attendue
    assert liste_cartes.cartes == cartes_attendues
    assert liste_id_cartes_old == (
        liste_id_cartes_new[:indice]
        + [id(carte_retiree)]
        + liste_id_cartes_new[indice:]
    )
