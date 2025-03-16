"""Implémentation des tests pour la classe Main."""

import pytest
from main import Main
from reserve import Reserve
from defausse import Defausse
from combinaison import Combinaison
import re


@pytest.mark.parametrize(
    "main1, main2, resultat_attendu",
    [
        ([pytest.as_coeur], [pytest.as_coeur], True),
        (
            [
                pytest.as_coeur,
                pytest.six_pique,
            ],
            [
                pytest.as_coeur,
                pytest.six_pique,
            ],
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
            True,
        ),
    ],
)
def test_main_eq(main1, main2, resultat_attendu):
    if resultat_attendu:
        assert (Main(main1).__eq__(Main(main2))) is resultat_attendu


@pytest.mark.parametrize(
    "main, reserve, erreur, msg_erreur",
    [
        (
            Main([pytest.huit_pique]),
            Reserve([]),
            ValueError,
            "La réserve est vide, impossible de piocher une carte.",
        )
    ],
)
def test_main_piocher_erreur(main, reserve, erreur, msg_erreur):
    with pytest.raises(
        ValueError, match="La réserve est vide, impossible de piocher une carte."
    ):
        main.piocher(reserve)


@pytest.mark.parametrize(
    "param, reserve, main_attendue, reserve_attendue",
    [
        (
            [],
            Reserve([pytest.sept_carreau, pytest.neuf_pique, pytest.huit_carreau]),
            [pytest.sept_carreau],
            Reserve([pytest.neuf_pique, pytest.huit_carreau]),
        ),
        (
            [pytest.quatre_trefle],
            Reserve([pytest.sept_carreau, pytest.neuf_pique, pytest.huit_carreau]),
            [pytest.quatre_trefle, pytest.sept_carreau],
            Reserve([pytest.neuf_pique, pytest.huit_carreau]),
        ),
    ],
)
def test_main_piocher_resultat(param, reserve, main_attendue, reserve_attendue):
    main = Main(param)
    carte = reserve.cartes[0]
    main.piocher(reserve)
    assert carte == main.cartes[-1]
    assert main.cartes == main_attendue
    assert reserve == reserve_attendue


@pytest.mark.parametrize(
    "param, indice, defausse, erreur, message_erreur",
    [
        (
            [pytest.as_coeur, pytest.six_pique, pytest.trois_carreau],
            15,
            [pytest.dame_pique, pytest.cinq_carreau],
            ValueError,
            "L'indice doit être un entier positif inférieur à la longueur de la main.",
        ),
        (
            [pytest.as_coeur, pytest.six_pique, pytest.trois_carreau],
            0,
            [pytest.dame_pique, pytest.cinq_carreau],
            ValueError,
            "L'indice doit être un entier positif inférieur à la longueur de la main.",
        ),
    ],
)
def test_main_jeter_erreur(param, indice, defausse, erreur, message_erreur):
    main = Main(param)
    with pytest.raises(erreur, match=message_erreur):
        main.jeter(indice, defausse)


@pytest.mark.parametrize(
    "main, indice, defausse, main_attendue, defausse_attendue",
    [
        (
            Main(
                [
                    pytest.deux_carreau,
                    pytest.huit_trefle,
                    pytest.six_pique,
                    pytest.dame_pique,
                ]
            ),
            1,
            Defausse([]),
            Main(
                [
                    pytest.deux_carreau,
                    pytest.six_pique,
                    pytest.dame_pique,
                ]
            ),
            Defausse([pytest.huit_trefle]),
        ),
        (
            Main([pytest.deux_carreau, pytest.huit_trefle, pytest.six_pique]),
            1,
            Defausse([pytest.roi_coeur]),
            Main([pytest.deux_carreau, pytest.six_pique]),
            Defausse([pytest.roi_coeur, pytest.huit_trefle]),
        ),
    ],
)
def test_main_jeter_resultat(main, indice, defausse, main_attendue, defausse_attendue):
    main.jeter(indice, defausse)
    assert main == main_attendue
    assert defausse == defausse_attendue


@pytest.mark.parametrize(
    "main, indices_combinaisons, premiere_pose, erreur, msg_erreur",
    [
        (
            [
                pytest.roi_coeur,
                pytest.roi_pique,
                pytest.roi_trefle,
                pytest.valet_carreau,
                pytest.roi_carreau,
                pytest.dame_carreau,
            ],
            [[0, 1, 2, 4], [3, 4, 5]],
            True,
            ValueError,
            "La carte Roi de carreau ne peut être posée qu'une seule fois.",
        ),
        (
            [
                pytest.roi_coeur,
                pytest.roi_pique,
                pytest.roi_trefle,
                pytest.valet_carreau,
                pytest.roi_carreau,
                pytest.dame_carreau,
            ],
            [[0, 1, 2, 4], [3, 4, 5]],
            False,
            ValueError,
            "La carte Roi de carreau ne peut être posée qu'une seule fois.",
        ),
        (
            [
                pytest.roi_coeur,
                pytest.roi_pique,
                pytest.roi_trefle,
                pytest.as_carreau,
                pytest.roi_carreau,
                pytest.dame_carreau,
            ],
            [[0, 1, 8], [3, 4, 5]],
            True,
            ValueError,
            "L'indice 8 doit être un entier positif strictement inférieur au nombre de"
            " cartes dans la main.",
        ),
        (
            [
                pytest.roi_coeur,
                pytest.roi_pique,
                pytest.roi_trefle,
                pytest.as_carreau,
                pytest.roi_carreau,
                pytest.dame_carreau,
            ],
            [[0, 1], [3, 4, 5]],
            True,
            ValueError,
            "La combinaison (Roi de coeur, Roi de pique) n'est pas valide.",
        ),
        (
            [
                pytest.roi_coeur,
                pytest.roi_pique,
                pytest.roi_trefle,
                pytest.as_carreau,
                pytest.as_coeur,
                pytest.as_trefle,
            ],
            [[0, 1, 2], [3, 4, 5]],
            True,
            ValueError,
            "La première pose doit contenir au moins une séquence.",
        ),
        (
            [
                pytest.roi_coeur,
                pytest.roi_pique,
                pytest.roi_trefle,
                pytest.as_carreau,
                pytest.deux_carreau,
                pytest.trois_carreau,
            ],
            [[0, 1, 2], [3, 4, 5]],
            True,
            ValueError,
            "La première pose doit rapporter au moins 51 points.",
        ),
    ],
)
def test_main_poser_erreur(
    main, indices_combinaisons, premiere_pose, erreur, msg_erreur
):
    with pytest.raises(erreur, match=re.escape(msg_erreur)):
        Main(main).poser(indices_combinaisons, premiere_pose)


@pytest.mark.parametrize(
    "main, indices_combi, premiere_pose, main_attendue, combinaisons_attendues,"
    "points_attendus",
    [
        (
            Main(
                [
                    pytest.roi_coeur,
                    pytest.roi_pique,
                    pytest.neuf_pique,
                    pytest.roi_trefle,
                    pytest.valet_carreau,
                    pytest.cinq_coeur,
                    pytest.roi_carreau,
                    pytest.dame_carreau,
                    pytest.deux_pique,
                ]
            ),
            [[0, 1, 3], [4, 6, 7]],
            True,
            Main([pytest.neuf_pique, pytest.cinq_coeur, pytest.deux_pique]),
            [
                Combinaison(
                    (
                        pytest.roi_coeur,
                        pytest.roi_pique,
                        pytest.roi_trefle,
                    )
                ),
                Combinaison(
                    (
                        pytest.valet_carreau,
                        pytest.roi_carreau,
                        pytest.dame_carreau,
                    )
                ),
            ],
            60,
        ),
        (
            Main(
                [
                    pytest.roi_coeur,
                    pytest.roi_pique,
                    pytest.neuf_pique,
                    pytest.roi_trefle,
                    pytest.valet_carreau,
                    pytest.cinq_coeur,
                    pytest.roi_carreau,
                    pytest.dame_carreau,
                    pytest.deux_pique,
                ]
            ),
            [[0, 1, 3]],
            False,
            Main(
                [
                    pytest.neuf_pique,
                    pytest.valet_carreau,
                    pytest.cinq_coeur,
                    pytest.roi_carreau,
                    pytest.dame_carreau,
                    pytest.deux_pique,
                ]
            ),
            [
                Combinaison(
                    (
                        pytest.roi_coeur,
                        pytest.roi_pique,
                        pytest.roi_trefle,
                    )
                ),
            ],
            30,
        ),
    ],
)
def test_main_poser_resultat(
    main,
    indices_combi,
    premiere_pose,
    main_attendue,
    combinaisons_attendues,
    points_attendus,
):
    combinaisons, points = main.poser(indices_combi, premiere_pose)
    assert main == main_attendue
    assert combinaisons == combinaisons_attendues
    assert points == points_attendus
