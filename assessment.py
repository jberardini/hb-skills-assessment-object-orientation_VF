"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

2. What is a class?

3. What is an instance attribute?

4. What is a method?

5. What is an instance in object orientation?

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """FILL IN DOCSTRING"""

    def __init__(self, first_name, last_name, address):
        """FILL IN DOCSTRING"""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """FILL IN DOCSTRING"""

    def __init__(self, question, correct_answer):
        """FILL IN DOCSTRING"""
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """FILL IN DOCSTRING"""
        print self.question
        self.user_answer = raw_input("Please enter your answer: ")

        if self.user_answer == self.correct_answer:
            self.right_answer = True
            return self.right_answer
        else:
            self.right_answer = False
            return self.right_answer


class Exam(object):
    """FILL IN DOCSTRING"""

    def __init__(self, name):
        """FILL IN DOCSTRING"""
        self.name = name
        self.questions = []

    def add_question(self, question):
        """FILL IN DOCSTRING"""

        self.questions.append(question)

    def administer(self):
        """FILL IN DOCSTRINGS"""
        self.score = 0
        self.number_of_questions = len(self.questions)

        for question in self.questions:
            question.ask_and_evaluate()
            if question.right_answer == True:
                self.score += 1

        return self.score

class Quiz(Exam):
    """FILL IN DOCSTRING"""

    def administer(self):
        """FILL IN DOCSTRING"""
        super(Quiz, self).administer()
        self.score_for_gradebook()

    def score_for_gradebook(self):
        """FILL IN DOCSTRING"""
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

###Test example functions####

def take_test(exam_name, student):
    """FILL IN DOCSTRINGS"""
    exam_name.administer()
    student.score = exam_name.score


def example(exam_name, student, question_one, question_two, question_three):
    """FILL IN DOCSTRINGS"""
    exam_name.add_question(question_one)
    exam_name.add_question(question_two)
    exam_name.add_question(question_three)

    take_test(exam_name, student)

    student_score = student.score

    return student_score

example(exam_name = exam, student = jill, question_one = question_one, 
        question_two = question_two, question_three = question_three)






