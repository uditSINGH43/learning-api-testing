import pytest


# #scope is function
# @pytest.fixture(scope='function')   #decorator
# def fixture_function():
#     print("Launching a browser")   #setup
#     yield
#     print("Closing a browser")      #Teardown
#
#
# class TestClass:
#     def testLogin(self,fixture_function):
#         print("This is Login Test")
#     def test_Search(self,fixture_function):
#         print("This is search Test")

# #scope is class
# @pytest.fixture(scope='class')   #decorator
# def fixture_function():
#     print("Launching a browser")   #setup
#     yield
#     print("Closing a browser")      #Teardown
#
# @pytest.mark.usefixtures("fixture_function")
# class TestClass:
#     def testLogin(self):
#         print("This is Login Test")
#     def test_Search(self):
#         print("This is search Test")


#scope is module
# @pytest.fixture(scope='module')   #decorator
# def fixture_function():
#     print("Launching a browser")   #setup
#     yield
#     print("Closing a browser")      #Teardown
#
#
# class TestClass:
#     def testLogin(self,fixture_function):
#         print("This is Login Test")
#     def test_Search(self,fixture_function):
#         print("This is search Test")

# #scope is module
# @pytest.fixture(scope='module')   #decorator
# def fixture_function():
#     print("Launching a browser")   #setup
#     yield
#     print("Closing a browser")      #Teardown
#
# @pytest.mark.usefixtures("fixture_function")
# class TestClass:
#     def testLogin(self):
#         print("This is Login Test")
#     def test_Search(self):
#         print("This is search Test")
#
# @pytest.mark.usefixtures("fixture_function")
# class TestClass1:
#     def testLogin(self):
#         print("This is Login Test")
#     def test_Search(self):
#         print("This is search Test")

#scope is function
@pytest.fixture(scope='function',autouse=True)   #decorator
def fixture_function():
    print("Launching a browser")   #setup
    yield
    print("Closing a browser")      #Teardown


class TestClass:
    def testLogin(self):
        print("This is Login Test")
    def test_Search(self):
        print("This is search Test")