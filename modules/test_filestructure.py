import filestructure as FS
import unittest

class Test_FileStructure(unittest.TestCase):
    def setup():
        """ """
        pass

    def test_create_structure_00(self):
        """ """
        pass

if __name__ == '__main__':
    # http://www.openp2p.com/pub/a/python/2004/12/02/tdd_pyunit.html#getting-started
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_FileStructure)
    unittest.TextTestRunner(verbosity=2).run(suite)
