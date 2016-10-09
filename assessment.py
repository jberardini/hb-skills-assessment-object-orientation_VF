"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   A) Polymorphism: It's easy to make different, but interchangeable types
   B) Encapsulation: Functions and their relevant data are grouped together
   C) Abstraction: You don't need to understand how a method works to use it


2. What is a class?
   A template for creating objects

3. What is an instance attribute?
   A characteristic of one particular occurence within a class

4. What is a method?
   A function that belongs to a particular class

5. What is an instance in object orientation?
   One particular occurence of a class

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is defined for every member of a class.
   An instance attribute is defined only for a particular instance. 
   In defining an animal class hierarchy, it would be appropriate in each subclass
   to define a class attribute for species (e.g. cat, dog, etc.), since all members
   of the subclass share that attribute. However, it would be better to define
   name as an instance attribute, since every animal instance will likely have a 
   particular name.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """Creates a student class"""

    def __init__(self, first_name, last_name, address):
        """Initialize student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """Creates a question class"""

    def __init__(self, question, correct_answer):
        """Initialize question attributes"""
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Ask question and compare user answer to correct answer"""
        print self.question
        self.user_answer = raw_input("Please enter your answer: ")

        if self.user_answer == self.correct_answer:
            self.right_answer = True
            return self.right_answer
        else:
            self.right_answer = False
            return self.right_answer


class Exam(object):
    """Creates an exam class"""

    def __init__(self, name):
        """Initialize exam attributes"""
        self.name = name
        self.questions = []

    def add_question(self, question):
        """Add a question to an exam"""

        self.questions.append(question)

    def administer(self):
        """Ask user all question on exam and track score"""
        self.score = 0
        self.number_of_questions = len(self.questions)

        for question in self.questions:
            question.ask_and_evaluate()
            if question.right_answer == True:
                self.score += 1

        return self.score

class Quiz(Exam):
    """Creates a quiz subclass of Exam"""

    def administer(self):
        """Ask user all questions, track score, and return Pass/Fail"""
        super(Quiz, self).administer()
        self.score_for_gradebook()

    def score_for_gradebook(self):
        """Evalute Pass / Fail based on percent correct"""
        self.percent_correct = float(self.score) / self.number_of_questions
        
        if self.percent_correct >= 0.5:
            print "You passed!"
            self.passed = True
        else:
            print "You failed :("
            self.passed = False
        return self.passed


###Instantiate a student, exam, and questions###

question_one = Question("What is your name?", "Jill")
question_two = Question("What is your quest?", "To learn to program")
question_three = Question("What is your favorite color?", "blue")

jill = Student('Jill', 'Berardini', '2012 Baker Street')

exam = Exam('Monty Python')

###Create take_test and example functions####

def take_test(exam_name, student):
    """Administers exam and saves score as a student attribute"""
    exam_name.administer()
    student.score = exam_name.score


def example(exam_name, student, question_one, question_two, question_three):
    """Add questions to test, administer exam, and save student score"""
    exam_name.add_question(question_one)
    exam_name.add_question(question_two)
    exam_name.add_question(question_three)

    take_test(exam_name, student)

    student_score = student.score

    return student_score

example(exam_name = exam, student = jill, question_one = question_one, 
        question_two = question_two, question_three = question_three)






