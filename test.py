from unittest import TestCase, main
from whiteboard import solution


class WhiteboardTestCase(TestCase):
    
    def test_1_all_fizz(self):
        self.assertEqual(solution([3,6,9,12]), ['Fizz', 'Fizz', 'Fizz', 'Fizz'])
    
    def test_2_all_fizz_with_extras(self):
        self.assertEqual(solution([1,3,6,8,9,12,22,23]), [1, 'Fizz', 'Fizz', 8, 'Fizz', 'Fizz', 22, 23])

    def test_3_all_buzz(self):
        self.assertEqual(solution([5,10,20,35]),   ['Buzz', 'Buzz', 'Buzz', 'Buzz']) 

    def test_4_buzz_with_extras(self):
        self.assertEqual(solution([1,5, 20,14,34, 35, 65]),   [1, 'Buzz', 'Buzz', 14, 34, 'Buzz', 'Buzz'])

    def test_4_empty_list(self):
        self.assertEqual(solution([]), [])

    def test_4_buzz_with_extras(self):
        self.assertEqual(solution([7,8,9,10,11,12,13,14]),  [7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14])

    def test_4_buzz_with_extras(self):
        self.assertEqual(solution([0, 15, 30, 45]),   ['FizzBuzz', 'FizzBuzz', 'FizzBuzz', 'FizzBuzz'])

    def test_4_buzz_with_extras(self):
        self.assertEqual(solution([9,10,11,12,13,14,15,30,32,33,45]),  ['Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 'FizzBuzz', 32, 'Fizz', 'FizzBuzz'])
                        

if __name__ == "__main__":
    main()