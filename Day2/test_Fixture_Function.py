import pytest

@pytest.fixture() #decorator (now this function is called as fixture function and default scoping is the function
def setup():
    print("Launching the browser")
    yield
    print("Closing the browser")

class TestClass:
    def test_Login(self, setup):
        print("This is login test")

    def test_Search(self, setup):
        print("This is search test")
