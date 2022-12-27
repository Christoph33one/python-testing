import unittest
from student import Student


class TestStudent(unittest.TestCase):
    def test_full_name(self):
        student = Student("John", "Doe")
        self.assertEqual(student.full_name, "John Doe")
        # assertEqual() in Python is a unittest library function that is
        # used in unit testing to check the equality of two values.
        # This function will take three parameters as input and return
        # a boolean value depending upon the assert condition.
        # If both input values are equal assertEqual()
        # will return true else return false.

    def test_alert_santa(self):
        student = Student("John",  "Doe")
        student.alert_santa()
        self.assertTrue(student.naughty_list)
        # assertTrue() in Python is a unittest library function
        #  that is used in unit testing to compare test value with true.
        #  This function will take two parameters as input and return a
        # boolean value depending upon the assert condition. If test
        # value is true then assertTrue() will return true else return false.


if __name__ == "__main__":
    unittest.main()
