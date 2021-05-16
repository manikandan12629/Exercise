import pytest


@pytest.fixture(scope="class")
def setup():
    print("this is prerequisite which executed first")
    yield
    print("this will be executed last")


@pytest.fixture()
def dataLoad():
    return ["manikandan", "Arun", "Adf"]


@pytest.fixture(params=[("chrome", "mani"), "arun", "adf"])
def crossBrowser(request):
    return request.param
