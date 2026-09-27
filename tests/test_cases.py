import unittest

from src.data_manager import get_cases
from src.cases import select_case


class TestCases(unittest.TestCase):

    def test_cases_are_loaded(self):
        cases = get_cases()

        self.assertGreater(len(cases), 0)

    def test_case_has_required_information(self):
        cases = get_cases()
        case = cases[0]

        self.assertIn("case_id", case)
        self.assertIn("title", case)
        self.assertIn("location", case)
        self.assertIn("suspects", case)
        self.assertIn("evidence", case)
        self.assertIn("witnesses", case)


if __name__ == "__main__":
    unittest.main()