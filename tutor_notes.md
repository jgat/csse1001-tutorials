# CSSE1001 - Tutor Cheatsheet

Jackson Gatenby
February 2014

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

At the start of the session, wander around the tables and ensure students are using IDLE correctly. For most students, even though they've attempted a set of MyPyTutor tasks, this is their first time using IDLE. The most common problems include
- not knowing to open a new file to start writing code,
- not saving files with a `.py` extension,
- not knowing where to save it (files in `C:\Python27` will probably be lost forever... note also that some students (first years) may not have ever saved files to their H: drive before, so be prepared to show them how).

The first "Hello, World" task does what it says on the label, followed by a `x=raw_input(); print "Hello,", x` task; the observant student may notice that the solution can be copied directly out of the course notes - bonus points to them for reading the notes!

The second task is an exercise in playing around with the IDLE console, as well as getting used to quirks like integer division, string operations, and the modulo operator. If students can't guess, encourage them to try more examples with different numbers/etc.

The third task is to write a simple function involving some `if` statements. Some students may require a hint on how to perform a divisibility check using `%`; some may also struggle with the task of turning a human-readable task statement into formal language. The extension task is optional, for any students who are racing ahead.

The final task involves using multiple variables in one program, as well as using the `random` library. This is good practice at using the builtin libraries, as well as taking snippets of code and applying it to your needs (i.e. recognising how and where to put `random.randint(10, 99)` into your code).

### Week 3 - Intro Part 2

Welcome to turtle week! You can read all about the [turtle](http://docs.python.org/2/library/turtle.html) in the python docs. This style of tutorial hasn't been tried before in this course, so it will be interesting to see how it goes.

Each of the tasks are self-explanatory, helping the turtle to boldly go where it hasn't gone before. The main emphasis is to practice writing functions, using while loops, and doing some spatial problem solving.

The final task is to write an `interact` function, which does the same [REPL](http://en.wikipedia.org/wiki/REPL) thing that it normally does in assignment 1. Feel free to hint to students that this task might be useful.

### Week 4 - Abstract Data Types (aka "Indexing and looping over strings")

This week's tasks are self-explanatory. The main take-home points are how to loop over strings, how to slice strings, etc. The tasks continue to give students practice at taking a high-level problem description ("find a number in this string") and turning it into code.

The extension task is useful, but some students may not get time to attempt it within the hour.

### Week 5 - Classes and Objects (aka "String methods, Lists and Files")

Take-home points from this week are how to read/write files, and using lists and tuples. Importantly, this tutorial often marks the "everything you need to know for assignment 1" point (useful, considering the assignment is due the next week).

On a more subtle level, this section of the course teaches students that an object can "do things" via its methods, and that different types of objects have different methods. Obvious, yes, but if students understand this, then they'll have a better idea of what a 'class' is when they come to write their own.

The first task is a new style - students are given a block of code which contains errors, and asked to identify and fix them. The aims of the task include being able to read and understand code written by other people, being able to interpret and respond to exception messages and incorrect output, and being aware of mistakes that students might make. For your reference, the errors in the code include:
* trying to use `+` to concatenate strings and ints in a `print` statement
* referencing a variable outside the scope of the function it's used in (`primes` in the last line)
* putting code at the wrong indentation level (the `i += 1` should not be in the if statement)
* mixing up types (beginning a function with an empty string instead of an empty list)
* forgetting to return a value
* prematurely returning in a for-loop (the `return True` should not be in the loop)

The second task is mostly about reading/writing files, and string manipulation (how do you get the `'square'` bit out of `'def square(x):'`?) The sample test file also tries to catch potential bugs, such as searching for a line which starts with `'def'` instead of `'def '`; you may like to note to students that they should be aware of potential hard-to-spot errors in their assignments.

### Week 6 - Classes, Error Handling and I/O (aka "Dictionaries and Error Handling")

The take-home points for this week are the what/how/why of dictionaries, and exception handling.

The first task is a pretty simple "read a file and parse it into a dictionary", and "write a function which does a loop and accesses a dictionary".

The challenge in the second task lies in understanding the data structure -- dictionaries inside dictionaries -- and having to write a function which will generate this structure. There's also a bit at the end on getting the students to raise exceptions.

### Week 7 - Class Design

This tutorial is all one big scenario with several subtasks. As well as being able to write a class with some non-trivial methods (in the first section), students should learn how to write other code outside the class which uses instances of the class (i.e. the `check_students` method). The final section gets students creating two classes which interact with each other.

It's difficult to guage how much students will be able to complete within the 50 minute period, but hopefully they will at least be able to finish the `check_students` task.

### Week 8 - Inheritance

The first task is a short warm-up, getting students to create a subclass of a given class, including overwriting a method or two. It shouldn't take too long to get through this.

The second task uses inheritance in a different way to other areas of the course -- the overall goal is to demonstrate that the `HTMLParser` class does very general things with the specifics left out (i.e. it parses all the HTML, but does nothing with it), but allows you to make a subclass which fills in the missing 'specific' functionality. Students should recognise that "under the hood", the `feed` method calls `handle_starttag`, but it's still easy to use this fact without understanding how `feed` works. (Of course, you're welcome to [try and understand](http://hg.python.org/cpython/file/2.7/Lib/HTMLParser.py) :P)

Students often forget that the `handle_starttag` method is called lots of times, once for each tag, rather than being called once with every tag. This means that the list of URLs needs to be created in the `__init__` method, instead of at the beginning of `handle_starttag`; moreover that `handle_starttag` should not return the list, instead another `get_urls` method is needed.

### Week 9 - GUIs Part I

In week 1 of GUIs, we aim to teach students how to get a desired widget layout using frames and packing options, and how to use button callbacks to modify the GUI appearance. There's also a bit at the end which gets students using the `tkMessageBox.showerror` method, which sometimes comes up in assignment 2.

The other subtle lesson in the provided template code is that to make a GUI application with classes, we simply put all the setup code in `__init__`, and make all the callbacks methods of the class. It may be worthwhile highlighting this structure to students.

### Week 10 - GUIs Part II

In week 2 of GUIs, we do a lot with a `Canvas` and event bindings. The tasks are designed so that it is difficult to jump from task statement to code, the students will need to think carefully about precisely what happens on each event, and what state needs to be stored internally.

In particular, students often struggle with the "two clicks to draw a line" task; the solution is to recognise that we need to store some kind of state within the class to know whether or not we are half-way through a line, and then that an `if` statement is needed in the `<Button-1>` callback.

It's also worth noting the way the `DrawingApp` and `SettingsFrame` interact with each other: `SettingsFrame` handles its own logic, and `DrawingApp` calls upon it when needed. Furthermore, it's noteworthy that `SettingFrame` inherits from `Frame`, while `DrawingApp` does not - this behaviour sometimes appears in assignment 2 as well (that the top-level class inherits from `object`, and other GUI classes inherit from `Frame`s and contain their own widgets).

### Week 11 - Recursion

Welcome to Recursion week! [Dress appropriately](http://www.cafepress.com.au/+recursive+t-shirts) to celebrate.

To warm up, we've got a simple recursive problem, which shouldn't take very long. The second task on file systems is a really nice example of a place where recursion makes everything nice, and iteration doesn't.

If there's time at the end of the session, load up a past exam from the library website, and get students to attempt the recursion question (and/or any other questions you decide). If you like, point students at resources like UQAttic (and throw in the usual "not official, don't blame us if they're wrong" disclaimer).

### Week 12 - Complexity and Computability (aka "just Complexity")

Just one task this week - write a function which is quadratic in the length of the list, and then make some optimisations using sorting and a dictionary. In the past, this tutorial has worked well as a "class discussion", led mostly by a tutor.

For the 'past exam practice', good options (at time of writing) include [2012 sem 2 Q38](http://www.library.uq.edu.au/pdfserve.php?image=1202/2012_2_CSSE1001.pdf) (students will often struggle with determining the logarithmic complexity of binary search), and [2012 sem 1 Q38-39](http://www.library.uq.edu.au/pdfserve.php?image=1201/2012_1_CSSE1001.pdf).

### Week 13 - Functional Programming, etc, etc.

This tutorial (and the course notes) go over a lot more than the usual examinable content, so it's not the end of the world if it goes in one ear and out the other. Towards the end of the session, get students to attempt the Q40 from some past exams (any of them will do, pick two or three).
