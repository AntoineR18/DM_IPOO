"""Implémentation des tests pour la classe Main."""

# import pytest
# from main import Main
# from reserve import Reserve
# from base import _ListeCartes


# ---- A FAIRE ----


# @pytest.mark.parametrize(
#     "main1, main2, resultat_attendu",
#     [
#         (_ListeCartes([pytest.as_coeur]), _ListeCartes([pytest.as_coeur]), True),
#         (
#             _ListeCartes([pytest.as_coeur, pytest.six_pique]),
#             _ListeCartes([pytest.as_coeur, pytest.six_pique]),
#             True,
#         ),
#         (
#             _ListeCartes([pytest.as_coeur, pytest.six_pique, pytest.trois_carreau]),
#             _ListeCartes([pytest.as_coeur, pytest.six_pique, pytest.trois_carreau]),
#             True,
#         ),
#         (_ListeCartes([pytest.as_coeur]), _ListeCartes([]), False),
#         (_ListeCartes([pytest.as_coeur]), _ListeCartes([pytest.as_trefle]), False),
#         (
#             _ListeCartes([pytest.as_coeur, pytest.six_pique, pytest.trois_carreau]),
#             _ListeCartes([pytest.as_coeur, pytest.trois_carreau, pytest.six_pique]),
#             True,
#         ),
#     ],
# )
# def test_main_eq(main1, main2, resultat_attendu):
#     if resultat_attendu:
#         assert (Main(main1) == Main(main2)) is resultat_attendu


# @pytest.mark.parametrize(
#     "param, reserve, carte_attendue, main_attendue, reserve_attendue",
#     [
#         (
#             [],
#             Reserve([pytest.sept_carreau, pytest.neuf_pique, pytest.huit_carreau]),
#             pytest.sept_carreau,
#             [pytest.sept_carreau],
#             Reserve([pytest.neuf_pique]),
#         ),
#     ],
# )
# def test_main_piocher(
#   param, reserve, carte_attendue, main_attendue, reserve_attendue):
#     main = Main(param)
#     main.piocher(reserve)
#     assert main.cartes == main_attendue
#     assert reserve == reserve_attendue


# @pytest.mark.parametrize()
# def test_main_jeter_erreur():
#     pass


# @pytest.mark.parametrize()
# def test_main_jeter_resultat():
#     pass


# @pytest.mark.parametrize()
# def test_main_poser_erreur():
#     pass


# @pytest.mark.parametrize()
# def test_main_poser_resultat():
#     pass

# -----------------
