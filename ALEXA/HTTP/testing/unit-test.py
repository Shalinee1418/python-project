import unittest
 from fizzbuzz import fizzbuzz

 class TestFizzBuzz( unittest, TestCase):
    def test_fizzbuzz_normal(self):
        self.assertEqual(fizzbuzz(1), '1')
        self.assertEqual(fizzbuzz(11), '11')
        self.assertEqual(fizzbuzz(14), '14')

    def test_fizzbuzz_fizz(self):
        self.assertEqual(fizzbuzz(3), 'fizz')
        self.assertEqual(fizzbuzz(39), 'fizz')
    def test_fizzbuzz_buzz(self):
        self.assertEqual(fizzbuzz(5),'buzz')
        self.assertEqual(fizzbuzz(40),'buzz')
    def test_fizzbuzz_buzz(self):
        self.assertEqual(fizzbuzz(15),'fizzbuzz')
        self.assertEqual(fizzbuzz(45), 'fizzbuzz')

 if __name__ == '__main__':
    unittest.main()                   