from django.test import TestCase

import re

# Create your tests here.


class TestViews(TestCase):

    def test_test(self):
        self.assertEqual(1, 1)

    def test_service_validation_text(self):

        userVal = "What is your quest"
        if re.match("^[a-zA-Z0-9* ]+$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, True)

    def test_service_validation_dot(self):

        userVal = "What is your quest."
        if re.match("^[a-zA-Z0-9.* ]+$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, True)

    def test_service_validation_qmark(self):

        userVal = "What is your quest.?"
        if re.match("^[a-zA-Z0-9.?* ]+$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, True)
