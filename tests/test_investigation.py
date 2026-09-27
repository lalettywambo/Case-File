import unittest

from src.data_manager import get_cases


class TestInvestigation(unittest.TestCase):

    def test_case_has_correct_suspect(self):
        cases = get_cases()
        case = cases[0]

        self.assertIn("correct_suspect", case)
        self.assertEqual(case["correct_suspect"], "James Carter")

    def test_suspects_exist(self):
        cases = get_cases()
        case = cases[0]

        self.assertGreater(len(case["suspects"]), 0)

    def test_evidence_exists(self):
        cases = get_cases()
        case = cases[0]

        self.assertGreater(len(case["evidence"]), 0)


if __name__ == "__main__":
    unittest.main()