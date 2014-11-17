import gitmetrics as GM
import unittest
import os
from collections import OrderedDict

class Test_GitMetrics(unittest.TestCase):
    def setUp(self):
        """ """

        self.name = os.path.abspath("fusor.py")
        # http://stackoverflow.com/a/2860193
        self.parent = os.path.abspath(os.path.join(self.name, os.pardir))

        self.fusor_module = GM.get_contributors_for_file(self.parent, self.name)
        self.fusor_line_01 = GM.get_contributor_for_line(self.parent, self.name, '1')

    def test_get_contributors_for_file_00(self):
        """ """
        self.assertTrue(type(self.fusor_module), OrderedDict)

    def test_get_contributor_for_line_00(self):
        """ """
        self.assertTrue(type(self.fusor_line_01), str)
        self.assertEqual(self.fusor_line_01, "arjunsumal@gmail.com\n")

if __name__ == '__main__':
    # http://www.openp2p.com/pub/a/python/2004/12/02/tdd_pyunit.html#getting-started
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_GitMetrics)
    unittest.TextTestRunner(verbosity=2).run(suite)
