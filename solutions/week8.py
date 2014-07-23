class Student(object):
    """A very simple model of a university student"""
    def __init__(self, name, student_no):
        """Create a Student with a name and unique student number

        Constructor: Student(str, int)
        """
        self._name = name
        self._student_no = student_no
        self._enrolments = []  # list of pairs (course code, tuition fee)

    def get_name(self):
        """
        Returns the name of this student.

        get_name(self)-> str
        """
        return self._name

    def get_student_no(self):
        """
        Returns the student number of this student.

        get_student_no(self) -> int
        """
        return self._student_no

    def enrol(self, course_code, fee):
        """
        Enrol in a course, at a given fee.

        enrol(self, str, int) -> None
        """
        self._enrolments.append((course_code, fee))

    def get_enrolments(self):
        """
        Return a list of courses the student is enrolled in.

        get_enrolments(self) -> list( (str, int) )
        """
        return self._enrolments

    def calculate_fees(self):
        """
        Compute the total tuition fees for the student.

        calculate_fees(self) -> int
        """
        total = 0
        for course_code, fee in self._enrolments:
            total += fee
        return total


class CollegeStudent(Student):
    """A very simple model for a student living in college."""
    def __init__(self, name, student_no, college_name, college_fee):
        """
        Creates an instance of CollegeStudent.

        Constructor: CollegeStudent(str, int, str, int)
        """
        

        # ---------------------------------------------------------------------
        # First initialize this instance of CollegeStudent as a Student with
        # the appropriate name and student number (student_no).
        # ---------------------------------------------------------------------
        Student.__init__(self, name, student_no)

        # Keep a reference to the college name and college fee for this
        # CollegeStudent
        self._college_name = college_name
        self._college_fee = college_fee

    def get_college(self):
        """
        Returns the name of the college that this CollegeStudent belongs to.

        get_college(self) -> str
        """
        return self._college_name

    def calculate_fees(self):
        """
        Returns the total amount of fees for this CollegeStudent.

        calculate_fees(self) -> int
        """


        # ---------------------------------------------------------------------
        # For this method, we need to calculate the sum of the CollegeStudent's
        # tuition fees (i.e. for courses) and their college fee (i.e. for
        # staying in their college).
        # 
        # We can calculate the tuition fees by utilizing the calculate_fees
        # method of the Student class which CollegeStudent extends, and the
        # college fee is stored in ._college_fee
        # ---------------------------------------------------------------------

        # Calculate the student fees by calling the calculate_fees method of
        # Student on this instance of CollegeStudent (i.e. self)
        tuition_fees = Student.calculate_fees(self)

        # Return the sum of the tuition fees and the college fee
        return tuition_fees + self._college_fee


def task1():
    """
    Convenience method to group all code relating to task 1.
    """
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

class LinkParser1(HTMLParser):
    def __init__(self):
        """
        Creates an instance LinkParser to parse hyperlinks from html text.

        Constructor: LinkParser()
        """

        # First initialize this instance of LinkParser as a HTMLParser, since it
        # directly inherits from HTMLParser.
        HTMLParser.__init__(self)

        # Keep a list of all the urls found in the files parsed by this
        # instance of LinkParser.
        self._urls = []

    def handle_starttag(self, tag, attrs):
        """
        Handles the start tag of every html element parsed by this instance.

        handle_starttag(self, str, list( (str, str) ))

        * Note this docstring is not necessary at this time, as it may not be
        * apparent exactly what this method is doing until after the task is
        * completed.
        """

        print tag, attrs
        # ---------------------------------------------------------------------
        # From the output of the above code, it can be seen that this method is
        # called for the start tag for each html element found by the parser,
        # with the name of the tag (tag), and a list of tuples of the
        # attributes of the tag, with each tuple having two elements, the first
        # being the name of the attribute, and the second being the
        # corresponding value.
        # I.e. [(attr1_name, attr1_value), (attr2_name, attr2_value), ...]
        # ---------------------------------------------------------------------

    def get_urls(self):
        pass

class LinkParser2(HTMLParser):
    def __init__(self):
        """
        Creates an instance LinkParser to parse hyperlinks from html text.

        Constructor: LinkParser()
        """

        # First initialize this instance of LinkParser as a HTMLParser, since
        # it directly inherits from HTMLParser.
        HTMLParser.__init__(self)

        # Keep a list of all the urls found in the files parsed by this
        # instance of LinkParser.
        self._urls = []

    def handle_starttag(self, tag, attrs):
        """
        Handles the start tag of every html element parsed by this instance.

        handle_starttag(self, str, list( (str, str) ))

        * Note this docstring is not necessary at this time, as it may not be
        * apparent exactly what this method is doing until after the task is
        * completed.
        """

        # ---------------------------------------------------------------------
        # Considering the output from step 1 (i.e. LinkParser1), we will need
        # to iterate over each attribute and only print out the values for the
        # attributes with the name 'href', but only for 'a' tags.
        # ---------------------------------------------------------------------

        if tag == 'a':
            for name, value in attrs:
                if name == 'href':
                    print value

        # ---------------------------------------------------------------------
        # A neater way would be to return early for all non-'a' tags,
        # transforming the above code to:
        # ---------------------------------------------------------------------
        #
        # if tag != 'a':
        #     return
        #
        # for name, value in attrs:
        #     if name == 'href':
        #         print value  
        #
        # ---------------------------------------------------------------------


        # ---------------------------------------------------------------------
        # Now it is fair to assume that there will be no duplicate attributes,
        # i.e. a certain attribute should only occur for a given tag once. In
        # the case of duplicates, the above code will output all values for
        # the href attribute. If we say that we assume that there will only be
        # a single occurrence of the href attribute for a given tag, and that
        # in the case of duplicates we will only consider the last one, we can
        # simplify this code by converting the list of attributes into a
        # dictionary first. I.e.
        # ---------------------------------------------------------------------
        #
        # if tag != 'a':
        #     return
        #
        # attrs = dict(attrs)
        # # Use get in case there is no href attribute
        # print attrs.get('href')
        #
        # ---------------------------------------------------------------------


    def get_urls(self):
        pass


class LinkParser(HTMLParser):
    def __init__(self):
        """
        Creates an instance LinkParser to parse hyperlinks from html text.

        Constructor: LinkParser()
        """

        # First initialize this instance of LinkParser as a HTMLParser, since it
        # directly inherits from HTMLParser.
        HTMLParser.__init__(self)

        # Keep a list of all the urls found in the files parsed by this
        # instance of LinkParser.
        self._urls = []

    def handle_starttag(self, tag, attrs):
        """
        Handles the start tag of every html element parsed by this instance.

        handle_starttag(self, str, list( (str, str) ))
        """

        # ---------------------------------------------------------------------
        # Using the code from step 2 (i.e. LinkParser2), we need to add the url
        # of each link we encounter to the list of urls, rather than printing
        # it out.
        # ---------------------------------------------------------------------

        if tag != 'a':
            return

        attrs = dict(attrs)
        # Use get in case there is no href attribute
        href = attrs.get('href')
        # Ensure that we only add a url if the href attribute exists
        if href != None:
            self._urls.append(href)

    def get_urls(self):
        """
        Returns a list of urls found by this LinkParser.

        get_urls(self) -> list(str)
        """
        return self._urls


def find_links(url):
    """Return a list of links from the given webpage"""
    # Open the webpage and read the HTML text
    fd = urllib2.urlopen(url)
    text = fd.read()
    fd.close()

    # Create a parser instance and feed it the text
    parser = LinkParser()
    parser.feed(text)

    return parser.get_urls()


def task2():
    """
    Convenience method to group all code relating to task 2.
    """
    url = 'http://csse1001.uqcloud.net/csse1001/_tutorials/week8.html'
    print find_links(url)

    # -------------------------------------------------------------------------
    # Alternatively, we could utilize the pretty print module to make the
    # output a bit more readable.
    # See https://docs.python.org/2/library/pprint.html
    # -------------------------------------------------------------------------
    # pprint.pprint(find_links(url))
    # -------------------------------------------------------------------------


###############################################################################

if __name__ == '__main__':
    task1()
    print '-'*70
    task2()
