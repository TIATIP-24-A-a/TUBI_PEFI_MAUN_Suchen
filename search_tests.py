import unittest
import search

class SearchTextTestCase(unittest.TestCase):

    def test_searchText_A_in_ABC_expectOneOccurrence(self):
        result = search.searchText("ABC", "A")
        self.assertEqual(result, 1)

    def test_searchText_A_in_AABC_expectTwoOccurrences(self):
        result = search.searchText("AABC", "A")
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
