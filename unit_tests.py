import unittest
from generatefixtures import main

class TestClass(unittest.TestCase):
    def test_third(self): 
        with self.assertRaises(SystemExit) as sys_exit:
            main(['hello.csv'])
        self.assertEqual(sys_exit.exception.code, 3)
    def test_fourth(self):
        with self.assertRaises(SystemExit) as sys_exit:
            main(['empty_file.csv'])
        self.assertEqual(sys_exit.exception.code, 4)
    def test_fifth(self): 
        with self.assertRaises(SystemExit) as sys_exit:
            main(['temp.csv', 'test.csv'])
        self.assertEqual(sys_exit.exception.code, 5)
    def test_sixth(self): 
        with self.assertRaises(SystemExit) as sys_exit:
            main(['one_row.csv'])
        self.assertEqual(sys_exit.exception.code, 6)
    def test_sixth_again(self): 
        with self.assertRaises(SystemExit) as sys_exit:
            main(['newlines.csv'])
        self.assertEqual(sys_exit.exception.code, 6)

if __name__=='__main__':
	unittest.main()