from django.test import TestCase

import re

# Create your tests here.


class TestViews(TestCase):
    """ text """
    def test_full_name_letter(self):

        userVal = "Stuart Chapman"
        if re.match("^[a-zA-Z ]+$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, True)

    def test_full_name_number(self):

        userVal = "9"
        if re.match("^[a-zA-Z ]+$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, False)

    def test_full_name_special(self):

        userVal = "<"
        if re.match("^[a-zA-Z ]+$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, False)

    def test_full_name_dot(self):

        userVal = "."
        if re.match("^[a-zA-Z ]+$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, False)

    def test_full_name_asterisk(self):

        userVal = "*"
        if re.match("^[a-zA-Z ]+$", userVal):  # remove the '*' from the regex
            Result = True
        else:
            Result = False

        self.assertEqual(Result, False)

    """ alphanumeric """
    def test_street_address1_letter(self):

        userVal = "Clos Springfield"
        if re.match("^[a-zA-Z0-9 ]+$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, True)

    def test_street_address1_number(self):

        userVal = "38"
        if re.match("^[a-zA-Z0-9 ]+$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, True)

    def test_street_address1_special(self):

        userVal = "*"
        if re.match("^[a-zA-Z0-9 ]+$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, False)

    """ numeric """
    def test_phone_number_letter(self):

        userVal = "Clos Springfield"
        if re.match("^[0-9]+$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, False)

    def test_phone_number_number(self):

        userVal = "38"
        if re.match("^[0-9]+$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, True)

    def test_phone_number_special(self):

        userVal = "*"
        if re.match("^[0-9]+$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, False)

    """ email """
    def test_email_one(self):

        userVal = "user@provider.com"
        if re.match(r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, True)

    def test_email_two(self):

        userVal = "user@provider.co.uk"
        if re.match(r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, True)

    def test_email_three(self):

        userVal = "user.user@provider.co.uk"
        if re.match(r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, True)

    def test_email_four(self):

        userVal = "user"
        if re.match(r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, False)

    def test_email_five(self):

        userVal = "user.com"
        if re.match(r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$", userVal):
            Result = True
        else:
            Result = False

        self.assertEqual(Result, False)
