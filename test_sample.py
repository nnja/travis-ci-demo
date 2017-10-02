import unittest

from sample import add


class SampleTest(unittest.TestCase):
    """
    Unit tests for code in the sample module
    """

    def test_add_integers(self):
        result = add(3, 5)
        self.assertEquals(8, result)

    def test_add_strings(self):
        result = add('Hello,', ' World!')
        self.assertEquals('Hello, World!', result)

    def test_add_lists(self):
        result = add([3], [5])
        self.assertEquals([3, 5], result)

    def test_bad_test(self):
        """ A failing unit test. """
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
