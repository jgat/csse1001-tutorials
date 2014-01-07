# CSSE1001 - Tutor Cheatsheet

January 2014

### General Notes

Students have a wide variety of learning resources available to them. For each topic, students should do things in the following order:
1. Read the course notes on that topic before the lectures.
2. Attend the lectures.
3. Attempt the MyPyTutor tasks (due Monday of the week after the lectures).
4. Attend a tutorial (T session) the week after lectures.

Obviously, it is a very rare thing for students to do everything that's expected of them. But you can usually expect that when (and if) students attend the tutorials, they will at least have heard of the concepts being taught -- e.g. for the GUI tutorials, you can expect that students will have heard of 'packing', and have a vague idea of what it does.


The following sections are some extra notes on each of the tutorial tasks (for T sessions), to assist your preparations.

### Week 2 - Intro Part 1

The first two weeks of the course have a steep learning curve (including variable manipulation, `raw_input`, `print`, if statements, while loops, and function definitions). This is all lumped together in one section of the course notes and MyPyTutor tasks, but is split into two weeks of tutorials. To smooth out the learning curve a little bit, the first week of tutorials has no while loops, and little emphasis on functions.

At the start of the session, wander around the tables and ensure students are using IDLE correctly. For most students, even though they've attempted a set of MyPyTutor tasks, this is their first time using IDLE. The most common problems are
- not knowing to open a new file to start writing code,
- not saving files with a `.py` extension,
- not knowing where to save it (files in `C:\Python27` are doomed to be lost forever... note also that some students (first years) may not have ever saved files to their H: drive before).

The first "Hello, World" task does what it says on the label; the observant student may notice that the solution can be copied directly out of the course notes - bonus points to them for reading the notes!

The second task is an exercise in playing around with the IDLE console, as well as getting used to quirks like integer division, string operations, and the modulo operator. If students can't guess, encourage them to try more examples with different numbers/etc.

The third task is to write a simple function involving some `if` statements. Some students may require a hint on how to perform a divisibility check using `%`; some may also struggle with the task of turning a human-readable task statement into formal language. The extension task is optional, for any students who are racing ahead.

The final task involves using multiple variables in one program, as well as using the `random` library. This is good practice at using the builtin libraries, as well as taking snippets of code and applying it to your needs (i.e. recognising how and where to put `random.randint(10, 99)` into your code).

### Week 3 - Intro Part 2

Welcome to turtle week! You can read all about the [turtle](http://docs.python.org/2/library/turtle.html) in the python docs. This style of tutorial hasn't been tried before in this course, so it will be interesting to see how it goes.

Each of the tasks are self-explanatory, helping the turtle to boldly go where it hasn't gone before. The main emphasis is to practice writing functions, using while loops, and doing some spatial problem solving.

The final task is to write an `interact` function, which does the same [REPL](http://en.wikipedia.org/wiki/REPL) thing that it normally does in assignment 1. Feel free to hint to students that this task might be useful.

### Week 4 - Abstract Data Types (aka "Indexing and looping over strings")

The main take-home points from this week are how to loop over strings, how to slice strings, and more of how to take a high-level problem description ("find a number in this string") and turn it into code.
Students may need reminding of the `enumerate` function.
The extension task is useful, but some students may not get time to attempt it within the hour.

### Week 5 - Classes and Objects (aka "String methods, Lists and Files")

Take-home points are reading/writing files, and using lists. Importantly, this tutorial often marks the "everything you need to know for assignment 1" point.

On a more subtle level, this section of the course teaches students that an object can "do things" via its methods, and that different types of objects have different methods. Obvious, yes, but if students understand this, then they'll have a better idea of what a 'class' is when they come to write their own.

### Week 6 - Classes, Error Handling and I/O (aka "Dictionaries and Error Handling")

The take-home points are the what/how/why of dictionaries and exception handling.

### Week 7 - Class Design



### Week 8 - Inheritance



### Week 9 - GUIs Part I



### Week 10 - GUIs Part II



### Week 11 - Recursion

Welcome to Recursion week! [Dress appropriately](http://www.cafepress.com.au/+recursive+t-shirts) to celebrate.

To warm up, we've got a simple recursive problem, which shouldn't take very long. The second task on file systems is a really nice example of a place where recursion makes everything nice, and iteration doesn't.

If there's time at the end of the session, load up a past exam from the library website, and get students to attempt the recursion question (and/or any other questions you decide). If you like, point students at resources like UQAttic (and throw in the usual "not official" disclaimer).

### Week 12 - Complexity and Computability (aka "just Complexity")

Just one task this week - write a function which is quadratic in the length of the list, and then make some optimisations using sorting and a dictionary. In the past, this tutorial has worked well as a "class discussion", led mostly by a tutor.

For the 'past exam practice', good options (at time of writing) include [2012 sem 2 Q38](http://www.library.uq.edu.au/pdfserve.php?image=1202/2012_2_CSSE1001.pdf) (students will often struggle with determining the logarithmic complexity of binary search), and [2012 sem 1 Q38-39](http://www.library.uq.edu.au/pdfserve.php?image=1201/2012_1_CSSE1001.pdf).

### Week 13 - Functional Programming, etc, etc.

This tutorial (and the course notes) go over a lot more than the usual examinable content, so it's not the end of the world if it goes in one ear and out the other. Towards the end of the session, get students to attempt the Q40 from some past exams (any of them will do, pick two or three).
