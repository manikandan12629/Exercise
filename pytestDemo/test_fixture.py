import pytest


@pytest.mark.usefixtures("setup")
class TestSample:

    def test_10(self):
        x = "manikandan"
        y = "kandan"
        print(x + y)
        assert y in x

    def test_20(self):
        x = 10
        y = 10
        print(x + y)
        assert x == y
