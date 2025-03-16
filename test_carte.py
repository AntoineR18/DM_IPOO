"""Implémentation des tests pour la classe Carte."""

# ici il faut un test qui vérifie que ça soulève bien des erreurs quand les valeurs
# et les couleurs des cartes existent pas

# je dirais du coup que ça sert à rien de faire des test qui vérifie que les méthodes
# donnent les résultats qu'on attend, mais plutôt juste un test qui check si ça
# soulève les erreurs

import re
import pytest
from carte import Carte

# test d'erreur dans l'initialisation de la classe Carte


@pytest.mark.parametrize(
    "params, erreur, message_erreur",
    [
        (
            {"valeur": "procrastiner_le_DM_d_IPOO", "couleur": "Trêfle"},
            ValueError,
            "La valeur de la carte n'existe pas.",
        ),
        (
            {"valeur": "2", "couleur": "coeur"},
            ValueError,
            "La couleur de la carte n'existe pas.",
        ),
    ],
)
def test_Carte_initialisation_parametres(params, erreur, message_erreur):
    # je suis pas du tout sûre de cette manière de faire des test parce que
    # c'est un truc qui check le fonctionnement de fonctions de base
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        # la solution, si ça marche pas ce serait de remplacer dans l7 et l27
        # Carte par __init__
        Carte(**params)


@pytest.mark.parametrize(
    "param",
    [
        ("Procrastiner le DM d IPOO", "Trêfle"),
        ("7", "Galérer sur les tests"),
        (7, "Coeur"),
    ],
)
def test_carte_init_valeur_echec(param):
    with pytest.raises(
        ValueError,
        match=(f"L'argument 'valeur' doit être dans {Carte.VALEURS()}"),
    ):
        Carte(param)
