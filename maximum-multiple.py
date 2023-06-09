import unittest


def max_multiple(divisor, bound):
    n = bound%divisor
    return bound-n

            
    # Your solution here
    pass


"""
These lines below are for testing purposes. Please, don't touch them :)
This code makes it possible to run a test on your solution during code review (or before, it's up to you!
If you run the following code, you can test your solution, just like on Codewars:

    python -m unittest maximum-multiple.TestMaxMultiple.test_ok

or

    pytest maximum-multiple.py
"""


class TestMaxMultiple(unittest.TestCase):

    def test_ok(self):
        assert max_multiple(2, 7) == 6
        assert max_multiple(3, 10) == 9
        assert max_multiple(7, 17) == 14
        assert max_multiple(10, 50) == 50
        assert max_multiple(37, 200) == 185
        assert max_multiple(7, 100) == 98


if __name__ == '__main__':
    unittest.main()
