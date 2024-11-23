import unittest
import search

class SearchTextTestCase(unittest.TestCase):

    def test_searchText_A_in_ABC_expectOneOccurrence(self):
        result = search.searchText("ABC", "A")
        self.assertEqual(1, result)

    def test_searchText_A_in_AABC_expectTwoOccurrences(self):
        result = search.searchText("AABC", "A")
        self.assertEqual(2, result)

    def test_searchText_BC_in_AABCAA_expectOneOccurrence(self):
        result = search.searchText("AABCAA", "BC")
        self.assertEqual(1, result)

    def test_searchText_BC_in_AABCABCA_expectOneOccurrence(self):
        result = search.searchText("AABCABCA", "BC")
        self.assertEqual(2, result)

    def test_searchText_empty_in_empty_expectOneOccurrence(self):
        result = search.searchText("", "")
        self.assertEqual(0, result)

if __name__ == '__main__':
    unittest.main()
