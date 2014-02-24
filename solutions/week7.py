class Student(object):
    """A university student"""
    def __init__(self, name, no, degree):
        """Create a student with a name.

        Constructor: Student(str)
        """
        self._name = name
        self._no = no
        self._degree = degree
        self._grades = {}

    def get_name(self):
        return self._name

    def get_student_no(self):
        return self._no

    def get_degree(self):
        return self._degree

    def set_degree(self, degree):
        self._degree = degree

    def get_first_name(self):
        return self._name.split()[0]

    def get_last_name(self):
        return self._name.split()[1]

    def get_email(self):
        return '{0}.{1}@uq.net.au'.format(self.get_first_name().lower(),
                                          self.get_last_name().lower())

    def __str__(self):
        return '{0} ({1}, {2}, {3})'.format(self._name, self.get_email(),
                                            self._no, self._degree)

    def __repr__(self):
        return 'Student({0!r}, {1!r}, {2!r})'.format(self._name, self._no,
                                                     self._degree)

    def add_grade(self, course, grade):
        self._grades[course] = grade

    def gpa(self):
        if not self._grades:
            return 0.0
        else:
            return float(sum(self._grades.values())) / len(self._grades)

s = Student('Michael Palin', 43215678, 'BInfTech')
print "Name:   ", s.get_name()
print "Stud. #:", s.get_student_no()
print "Degree: ", s.get_degree()
print "set_degree..."
s.set_degree('BE')
print "Degree: ", s.get_degree()
print "First:  ", s.get_first_name()
print "Last:   ", s.get_last_name()
print "Email:  ", s.get_email()
print "str:    ", str(s)
print "repr:   ", repr(s)

###############################################################################


def check_students(students):
    seen = []
    for s in students:
        n = s.get_student_no()
        if n in seen:
            return False
        seen.append(n)
    return True


def check_students(students):
    # Lazier, but more computationally expensive
    for s in students:
        for t in students:
            if s is not t and s.get_student_no() == t.get_student_no():
                return False
    return True


def check_students2(students):
    """A variant where you raise a ValueError when invalid"""
    seen = {}
    for s in students:
        n = s.get_student_no()
        if n in seen:
            raise ValueError(seen[n].get_name() + ' and ' + s.get_name() +
                             ' have the same student number')
        seen[n] = s
    return True

students1 = [Student('Alice A', 1, 'BE'), Student('Bob B', 2, 'BA'),
             Student('Carol C', 4, 'BA')]
assert check_students(students1) is True

students2 = [Student('Alice A', 1, 'BE'), Student('Bob B', 2, 'BA'),
             Student('Carol C', 4, 'BA'), Student('Dan D', 2, 'BInfTech')]
assert check_students(students2) is False

try:
    check_students2(students2)
except ValueError as e:
    pass
else:
    raise RuntimeError("that can't be right... tutors never make mistakes")

###############################################################################


class Course(object):
    def __init__(self, code, name):
        self._code = code
        self._name = name

    def get_code(self):
        return self._code

    def get_name(self):
        return self._name


csse1001 = Course('CSSE1001', 'Intro to Software Engineering')
deco1800 = Course('DECO1800', 'Design Computing Studio I')

assert s.gpa() == 0
s.add_grade(csse1001, 4)
assert s.gpa() == 4.0
s.add_grade(deco1800, 5)
assert s.gpa() == 4.5
s.add_grade(csse1001, 6)
assert s.gpa() == 5.5
