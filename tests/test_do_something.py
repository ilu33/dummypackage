import unittest

from dummypackage import scripts


class Test(unittest.TestCase):
    def test_do_something(self):
        self.assertEqual('SMTH', scripts.cli.do_something('smth'))


if __name__ == '__main__':
    unittest.main()
