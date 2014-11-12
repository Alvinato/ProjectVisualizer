import fusor as FS
import unittest

class Test_Fusor(unittest.TestCase):
    def setup():
        """ """
        pass

    def test_fuse_00(self):
        """ """
        pass

    def test_fuse_file_00(self):
        """ """
        pass

    def test_combine_results_00(self):
        """ """
        pass

if __name__ == '__main__':
    # http://www.openp2p.com/pub/a/python/2004/12/02/tdd_pyunit.html#getting-started
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Fusor)
    unittest.TextTestRunner(verbosity=2).run(suite)
