import unittest

class ThrowExceptionTest(unittest.TestCase):
    def test_failure(self):
        assert False, "Dang!"
    def test_success(self):
        pass
