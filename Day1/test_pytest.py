'''
class TestClass:
    def testmethod1(self):
        print("testmethod1")

    def testmethod2(self):
        print("testmethod2")
'''
import pytest

@pytest.mark.order(1)
def test_open_ap():
    print("app opened")

@pytest.mark.order(3)
def test_execute():
    print("executed")

@pytest.mark.order(2)
def test_close():
    print("closed")
