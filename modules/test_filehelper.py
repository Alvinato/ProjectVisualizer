import filehelper as FH
import unittest

class Test_FileHelper(unittest.TestCase):
    def setup():
        """ """
        pass

    def test_convert_file_to_json_00(self):
        """ """
        pass

    def test_find_python_files_in_project_00(self):
        """ """
        pass

if __name__ == '__main__':
    # http://www.openp2p.com/pub/a/python/2004/12/02/tdd_pyunit.html#getting-started
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_FileHelper)
    unittest.TextTestRunner(verbosity=2).run(suite)
