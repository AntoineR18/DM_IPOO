"""Implémentation des tests pour la classe Reserve."""
import re
import pytest
from reserve import Reserve


# test d'erreur de la méthode distribuer
@pytest.mark.parametrize(
    "params, erreur, message_erreur",
    [
        (
            {"self": Reserve([pytest.as_pique, pytest.as_carreau, pytest.neuf_coeur]),
             "n_joueurs": 'procrastiner_le_DM_d_IPOO', 'idx_premier_joueur': 1, 'n_cartes': "14/15"},
            ValueError,
            "procrastiner_le_DM_d_IPOO doit être un entier compris entre 2 et 5."
        ),
        (
            {"self": Reserve([pytest.as_pique, pytest.as_carreau, pytest.neuf_coeur]),
             "n_joueurs": 4, 'idx_premier_joueur': 'procrastiner_le_DM_d_IPOO', 'n_cartes': "14/15"},
            ValueError,
            "procrastiner_le_DM_d_IPOO doit être un entier positif."
        )
    ]
)
def test_Reserve_distribuer_parametres(params, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Reserve.distribuer(**params)


# test des résultats de la méthode distribuer
@pytest.mark.parametrize(
    "params, resultat_attendu",
    [
        ({Reserve([pytest.as_trefle, pytest.neuf_coeur, pytest.neuf_pique, pytest.roi_coeur]), 3, 1, "14/15"},
         [[pytest.as_trefle], [pytest.neuf_coeur], [pytest.neuf_pique]])
    ]
)
def test_Reserve_distribuer_resultat(params, resultat_attendu):
    assert Reserve.distribuer(params) == resultat_attendu
#ici un problème très facile à problème c'est l'orde des cartes dans le résultat attendu parce que là j'y suis allée au pif
