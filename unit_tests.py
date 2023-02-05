import unittest
from generatefixtures import main

class TestClass(unittest.TestCase):
    def test_third(self): 
        with self.assertRaises(SystemExit) as cm:
            main(['hello.csv'])
        self.assertEqual(cm.exception.code, 3)
    def test_fourth(self):
        with self.assertRaises(SystemExit) as cm:
            main(['empty_file.csv'])
        self.assertEqual(cm.exception.code, 4)
    def test_fifth(self): 
        with self.assertRaises(SystemExit) as cm:
            main(['temp.csv', 'test.csv'])
        self.assertEqual(cm.exception.code, 5)
    def test_sixth(self): 
        with self.assertRaises(SystemExit) as cm:
            main(['one_row.csv'])
        self.assertEqual(cm.exception.code, 6)
    def test_sixth_again(self): 
        with self.assertRaises(SystemExit) as cm:
            main(['newlines.csv'])
        self.assertEqual(cm.exception.code, 6)
    # def test_sixth(self): 
    #     with self.assertRaises(SystemExit) as cm:
    #         main(['empty_file.csv'])
    #     self.assertEqual(cm.exception.code, 5)
        # self.assertEqual(main(['invalid_file.csv']), 3)
# 	# check function_to_test

# def test_<name_2>(self):
# 	# check function_to_test
# def test_<name_n>(self):
	# 	# check function_to_test

if __name__=='__main__':
	unittest.main()