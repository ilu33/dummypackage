import os
import pexpect
import unittest

class Test(unittest.TestCase):
    def test_cli_count(self):
        count = 3
        p = pexpect.spawn('dummypackage ' + str(count))
        self.assertEqual(0, p.expect(pexpect.EOF))
        self.assertEqual(p.before, b'False\r\n' * count)

if __name__ == '__main__':
    unittest.main()
