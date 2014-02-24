class Student(object):
    """A very simple model of a university student"""
    def __init__(self, name, student_no):
        """Create a Student with a name and unique student number

        Constructor: Student(str, int)
        """
        self._name = name
        self._sno = student_no
        self._enrolments = []  # list of pairs (course code, tuition fee)

    def get_name(self):
        return self._name

    def get_student_no(self):
        return self._sno

    def enrol(self, course_code, fee):
        """Enrol in a course, at a given fee."""
        self._enrolments.append((course_code, fee))

    def get_enrolments(self):
        """Return a list of courses the student is enrolled in."""
        return self._enrolments

    def calculate_fees(self):
        """Compute the total tuition fees for the student."""
        total = 0
        for course_code, fee in self._enrolments:
            total += fee
        return total


# Define your CollegeStudent class here
