import filehelper as FH
import unittest

class Test_Config(unittest.TestCase):
    def setup():
        """ """
        pass

    def test_create_preferences_00(self):
        """ """
        pass

    def test_load_project_properties_00(self):
        """ """
        pass

if __name__ == '__main__':
    # http://www.openp2p.com/pub/a/python/2004/12/02/tdd_pyunit.html#getting-started
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Config)
    unittest.TextTestRunner(verbosity=2).run(suite)
