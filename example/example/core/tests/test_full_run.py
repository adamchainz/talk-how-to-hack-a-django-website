import unittest

from django.test import TestCase


class ExampleTests(TestCase):
    def test_success_1(self):
        pass

    def test_success_2(self):
        pass

    def test_success_3(self):
        pass

    def test_fail_1(self):
        self.assertTrue(False)

    def test_error_1(self):
        raise ValueError("Uh oh")

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertTrue(False)

    @unittest.expectedFailure
    def test_unexpected_success(self):
        pass

    @unittest.skip("Temp disabled")
    def test_skip(self):
        pass
