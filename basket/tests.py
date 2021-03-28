from django.test import TestCase

import re

# Create your tests here.


class TestViews(TestCase):

    def test_servings_letter(self):

        userVal = "a"
        if re.match("^[0-9]+$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, False)

    def test_servings_number(self):

        userVal = "9"
        if re.match("^[0-9]+$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, True)

    def test_servings_special(self):

        userVal = "<"
        if re.match("^[0-9]+$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, False)

    def test_servings_dot(self):

        userVal = "."
        if re.match("^[0-9]+$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, False)

    def test_servings_asterisk(self):

        userVal = "*"
        if re.match("^[0-9]+$", userVal):  # remove the '*' from the regex
            Result = True
        else:
            Result = False

        self.assertEqual(Result, False)
