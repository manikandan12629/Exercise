import pytest

product = [
    (1, 4, 4),
    (2, 5, 10),
    (5, 6, 30),
    (2, 9, 18)
]


@pytest.mark.parametrize("a, b, val", product)
def test_ParamSamp(a, b, val):
    assert a * b == 0
