import unittest
from solution import Solution


class TestCourseScheduleII(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setup for all tests")

    @classmethod
    def tearDownClass(cls):
        print("Teardown for all tests")

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_example_1(self):
        self.assertEqual(self.solution.findOrder(2, [[1, 0]]), [0, 1])

    def test_example_2(self):
        result = self.solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
        self.assertTrue(result == [0, 2, 1, 3] or result == [0, 1, 2, 3])

    def test_example_3(self):
        self.assertEqual(self.solution.findOrder(1, []), [0])

    def test_no_prerequisites(self):
        self.assertEqual(self.solution.findOrder(3, []), [0, 1, 2])

    def test_impossible_to_complete(self):
        self.assertEqual(self.solution.findOrder(2, [[0, 1], [1, 0]]), [])

    def test_large_case(self):
        numCourses = 5
        prerequisites = [[1, 0], [2, 0], [3, 1], [4, 3], [2, 4]]
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertTrue(result == [] or result == [0, 1, 3, 4, 2] or result == [0, 2, 1, 3, 4])

    def test_multiple_valid_outputs(self):
        result = self.solution.findOrder(3, [[0, 1], [0, 2], [1, 2]])
        self.assertTrue(result == [2, 1, 0] or result == [2, 0, 1])

    def test_no_courses(self):
        self.assertEqual(self.solution.findOrder(0, []), [])

    def test_course_with_no_dependencies(self):
        self.assertEqual(self.solution.findOrder(3, [[1, 0]]), [0, 1, 2])

    def test_max_constraints(self):
        numCourses = 2000
        prerequisites = [[i, i - 1] for i in range(1, numCourses)]
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertTrue(self.is_valid_topological_sort(numCourses, prerequisites, result))

    def is_valid_topological_sort(self, numCourses, prerequisites, order):
        if len(order) != numCourses:
            return False
        position = {course: i for i, course in enumerate(order)}
        for crs, pre in prerequisites:
            if position[crs] <= position[pre]:
                return False
        return True

    def test_bug_report_example(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 1], [3, 2], [0, 3]]  # for creating a cycle
        self.assertEqual(self.solution.findOrder(numCourses, prerequisites), [])


if __name__ == '__main__':
    unittest.main()
