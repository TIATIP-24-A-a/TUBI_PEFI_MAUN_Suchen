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

    def test_searchText_Reis_in_Apfel_expectOneOccurrence(self):
        result = search.searchText("Apfel", "Reis")
        self.assertEqual(0, result)

    def test_searchText_Reis_in_DeineMutterkochtReis_expectOneOccurrence(self):
        result = search.searchText("Deine Mutter kocht Reis", "Reis")
        self.assertEqual(2, result)

    def test_searchText_Gedicht_in_String_expectOneOccurrence(self):
        result = search.searchText("Gedichte sind poetische Texte. Sie unterscheiden sich von anderen Texten durch ihren Rhythmus, die Verse und die oftmals bildliche Sprache. Ein Gedicht besteht aus mehreren Versen, die zu Strophen zusammengefasst werden. Oftmals reimen sich einzelne Verse; dies ist aber keine zwingende Voraussetzung für ein Gedicht.", "Gedicht")
        self.assertEqual(3, result)

if __name__ == '__main__':
    unittest.main()
