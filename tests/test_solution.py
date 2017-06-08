from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        res = solution()

        self.assertEqual(res.shape, (3, 3, 3))
