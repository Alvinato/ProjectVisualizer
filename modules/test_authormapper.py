import authormapper as AM
import unittest

class Test_AuthorMapper(unittest.TestCase):
    def setup():
        """ """
        pass

    def test_get_git_analysis_00(self):
        """ """
        pass

    def test_create_author_mappings_for_file_00(self):
        """ """
        pass

if __name__ == '__main__':
    # http://www.openp2p.com/pub/a/python/2004/12/02/tdd_pyunit.html#getting-started
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_AuthorMapper)
    unittest.TextTestRunner(verbosity=2).run(suite)
