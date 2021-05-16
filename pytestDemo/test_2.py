import inspect

import pytest


#@pytest.mark.xfail
def test_2():
    x = 10
    y = 10
    print(inspect.stack()[1][3])
    assert x == y


def test_3():
    x = 30
    y = 10
    assert x == y
