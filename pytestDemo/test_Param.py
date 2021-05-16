import pytest


@pytest.mark.usefixtures("dataLoad")
class TestSample2:

    def test_2(self):
        x = 10
        y = 10
        print(x + y)
        assert x == y

    def test_ParamSample(self, dataLoad):
        print(dataLoad)