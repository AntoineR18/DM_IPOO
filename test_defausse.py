"""Implémentation des tests pour la classe Defausse."""

import pytest
from defausse import Defausse
from reserve import Reserve


@pytest.mark.parametrize(
    "param1, param2, reserve_attendue",
    [
        (
            [pytest.dame_pique, pytest.quatre_trefle, pytest.as_pique],
            [],
            [pytest.as_pique, pytest.quatre_trefle, pytest.dame_pique],
        ),
        (
            [],
            [pytest.roi_carreau],
            [pytest.roi_carreau],
        ),
        (
            [pytest.dame_pique, pytest.quatre_trefle, pytest.as_pique],
            [pytest.roi_carreau],
            [
                pytest.roi_carreau,
                pytest.as_pique,
                pytest.quatre_trefle,
                pytest.dame_pique,
            ],
        ),
    ],
)
def test_defausse_vider(param1, param2, reserve_attendue):
    defausse = Defausse(param1)
    reserve = Reserve(param2)
    d = defausse.__len__()
    r = reserve.__len__()
    defausse.vider(reserve)
    assert defausse.__len__() == 0
    assert reserve.__len__() == r + d
    assert reserve_attendue.__eq__(Reserve(param1 + param2))


# le troisième assert à refaire si on a le temps
