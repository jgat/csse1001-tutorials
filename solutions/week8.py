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


class CollegeStudent(Student):
    """A very simple model for a student living in college."""
    def __init__(self, name, student_no, college, college_fee):
        Student.__init__(self, name, student_no)
        self._college = college
        self._college_fee = college_fee

    def get_college(self):
        return self._college

    def calculate_fees(self):
        course_fees = Student.calculate_fees(self)
        return course_fees + self._college_fee


def task1():
    fred = CollegeStudent("Fred", 43214321, "St. Leo's", 18000)
    print "Fred's college is", fred.get_college()
    print "Fees before enrolling:", fred.calculate_fees()
    fred.enrol('CSSE1001', 1000)
    fred.enrol('LAWS1000', 1300)
    print "Fees after enrolling:", fred.calculate_fees()

###############################################################################

from HTMLParser import HTMLParser
import urllib2
import pprint


class LinkParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._urls = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and 'href' in attrs:
            self._urls.append(attrs['href'])

    def get_urls(self):
        return self._urls


def find_links(url):
    """Return a list of links from the given webpage"""
    # Open the webpage and read the HTML text
    #fd = urllib2.urlopen(url)
    fd = open(url)    # tutors are allowed to be sneaky like this
    text = fd.read()
    fd.close()

    # Create a parser instance and feed it the text
    parser = LinkParser()
    parser.feed(text)

    return parser.get_urls()


def task2():
    # no one will suspect that I used pprint
    pprint.pprint(find_links('../tasks/week8.html'))

if __name__ == '__main__':
    task1()
    print '-'*70
    task2()
