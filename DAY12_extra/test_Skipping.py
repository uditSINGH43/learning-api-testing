import sys

import pytest

class TestSkipping:
    #skipping unconditionalyy
    @pytest.mark.skip(reason="Feature not yet implemented")
    def test_unfinished(self):
        assert True

    #conditional skip based on system platform
    @pytest.mark.skipif(sys.platform == "win32",reason="Does not run on windows")
    def test_non_windows(self):
        assert True


    #skipping inside a Test
    @pytest.fixture()
    def skip_if_no_network(self):
        network_available = False  #simulate no network
        if not network_available:
            pytest.skip("Skipping because no netwrok is available")

    def test_network_feature(self,skip_if_no_network):
        assert True

    #xfail --> Expected to fail
    @pytest.mark.xfail(reason="Known bug in the feature")
    def test_failing_feature(self):
        assert False   #This test will fail but marked as xfail