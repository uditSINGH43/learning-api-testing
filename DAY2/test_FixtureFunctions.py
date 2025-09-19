import pytest


@pytest.fixture()
def setup():
    print("Launching the browser")
    yield
    print("closing the browser")


class TestClass:
    def test_Login(self, setup):
        print("this is test login")
    def test_search(self, setup):
        print("this is test search")