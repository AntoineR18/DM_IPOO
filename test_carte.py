"""Implémentation des tests pour la classe Carte."""

import pytest
from carte import Carte
import re


@pytest.mark.parametrize(
    "params",
    [
        ("procrastiner_le_dm_d_ipoo", "Pique"),
        ("Roi", "galerer sur les test"),
        (7, "Pique"),
    ],
)
def test_cartes_init_echec(params):
    valeur, couleur = params
    with pytest.raises(
        ValueError,
        match=re.escape(
            f"La valeur de la carte doit être dans {Carte.VALEURS()} et sa couleur"
            f" dans {Carte.COULEURS()}."
        ),
    ):
        Carte(valeur, couleur)


@pytest.mark.parametrize(
    "valeur, couleur, carte_attendue",
    [("Roi", "Coeur", Carte("Roi", "Coeur")), ("9", "Pique", pytest.neuf_pique)],
)
def test_cartes_init_succes(valeur, couleur, carte_attendue):
    carte = Carte(valeur, couleur)
    assert carte == carte_attendue


@pytest.mark.parametrize(
    "carte1, carte2, resultat_attendu",
    [
        (("As", "Coeur"), ("As", "Coeur"), True),
        (("Dame", "Pique"), ("Dame", "Pique"), True),
        (("4", "Trêfle"), ("Dame", "Trêfle"), False),
        (("Dame", "Pique"), ("4", "Trêfle"), False),
    ],
)
def test_carte_eq(carte1, carte2, resultat_attendu):
    valeur1, couleur1 = carte1
    valeur2, couleur2 = carte2
    assert (Carte(valeur1, couleur1) == Carte(valeur2, couleur2)) is resultat_attendu


@pytest.mark.parametrize(
    "valeur, couleur, resultat_attendu",
    [
        ("As", "Pique", "As de pique"),
        ("8", "Coeur", "8 de coeur"),
        ("4", "Trêfle", "4 de trêfle"),
    ],
)
def test_carte_str(valeur, couleur, resultat_attendu):
    assert str(Carte(valeur, couleur)) == resultat_attendu


@pytest.mark.parametrize(
    "valeur, couleur, resultat_attendu",
    [
        ("As", "Pique", "Carte('As', 'Pique')"),
        ("8", "Coeur", "Carte('8', 'Coeur')"),
        ("4", "Trêfle", "Carte('4', 'Trêfle')"),
    ],
)
def test_carte_repr(valeur, couleur, resultat_attendu):
    assert repr(Carte(valeur, couleur)) == resultat_attendu


@pytest.mark.parametrize(
    "valeur1, couleur1, valeur2, couleur2, hash_attendu",
    [
        ("As", "Coeur", "As", "Coeur", True),
        ("9", "Pique", "9", "Carreau", False),
        ("8", "Coeur", "Roi", "Trêfle", False),
        ("Roi", "Pique", "Roi", "Pique", True),
    ],
)
def test_carte_hash(valeur1, couleur1, valeur2, couleur2, hash_attendu):
    assert (
        hash(Carte(valeur1, couleur1)) == hash(Carte(valeur2, couleur2))
    ) == hash_attendu

    if hash_attendu:
        assert hash(Carte(valeur1, couleur1)) == hash(Carte(valeur2, couleur2))
    else:
        assert hash(Carte(valeur1, couleur1)) != hash(Carte(valeur2, couleur2))
