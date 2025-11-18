import unittest
from main import *

class Tests_time_search(unittest.TestCase):
    def test_valid_time(self):
        text = "we are going to the cinema at 20:00:00, movie ends at 22:12:14, you will be at home 'till 00:00:00"
        self.assertEqual(extract_time(text), ["20:00:00", "22:12:14", "00:00:00"])
    def test_invalid_time(self):
        text = "we are going to the cinema at 24:00:00, movie ends at 21:12:90, we will reach home at 21:77:00"
        self.assertEqual(extract_time(text), [])
    def test_only_numbers(self):
        text = "we are going to the cinema at 2d0:00:00, movie ends at 22:12y:14 or 22:12:14W"
        self.assertEqual(extract_time(text), [])
    def test_single_digit(self):
        text = "we are going to the cinema at 2:12:14 pm, movie ends at 20:12:4 or 20:3:40"
        self.assertEqual(extract_time(text), [])
    def test_boundaries(self):
        text = "we are going to the cinema at20:00:00, movie ends at 22:12:14, you will be at home 'till00:00:00end"
        self.assertEqual(extract_time(text), ["22:12:14"])
    def test_empty_string(self):
        self.assertEqual(extract_time(""), [])
    def test_no_time_in_text(self):
        text = "we are going to the cinema"
        self.assertEqual(extract_time(text), [])
    def test_same_time(self):
        text = "01:01:01 and 01:01:01"
        self.assertEqual(extract_time(text), ["01:01:01", "01:01:01"])
    def test_too_much_digits(self):
        text = "we are going to the cinema at 023:00:00, movie ends at 21:120:00, we will reach home at 21:07:348"
        self.assertEqual(extract_time(text), [])
    def test_start_end_of_string(self):
        text = "01:01:01 we are going to the cinema 10:10:10"
        self.assertEqual(extract_time(text), ["01:01:01", "10:10:10"])

if __name__ == '__main__':
    unittest.main()