# class TestClass:
#     def testmethod1(self):
#         print("this is Method1")
#     def testmethod2(self):
#         print("this is Method2")

import pytest

@pytest.mark.dependency()
@pytest.mark.order(1)
def test_open_app():
    print("app opened")
    assert False

@pytest.mark.dependency(depends=["test_login"])
@pytest.mark.order(3)
def test_dashboard():
    print("Dashboard Loaded")

@pytest.mark.dependency(depends=["test_open_app"])
@pytest.mark.order(2)
def test_login():
    print("login Successfully")
