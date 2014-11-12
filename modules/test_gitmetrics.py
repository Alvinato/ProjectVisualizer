import gitmetrics as GM
import unittest

class Test_GitMetrics(unittest.TestCase):
    def setup():
        """ """
        pass

    def test_get_contributors_for_file_00(self):
        """ """
        pass

    def test_get_contributor_for_line_00(self):
        """ """
        pass

if __name__ == '__main__':
    # http://www.openp2p.com/pub/a/python/2004/12/02/tdd_pyunit.html#getting-started
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_GitMetrics)
    unittest.TextTestRunner(verbosity=2).run(suite)
