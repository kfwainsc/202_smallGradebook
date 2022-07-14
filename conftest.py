# conftest.py   "grades"  
##################################################################
# KENDRA WAINSCOTT           Prog 4/5          CS202 Winter 2022
#
# This file is to allow the use of FIXTURES in the test suite 
##################################################################
from  gradeClasses import Grade, Demo, Exams, Thesis
from structures import Course, Student
from input import demoList, exList, thesList, courseNames, studentNames
import pytest

@pytest.fixture # default
def aGrade():
    g = Grade("empty")
    return g

#### DEMO #########################################################
@pytest.fixture # pass demo
def pDemo():
    d = Demo(True,True)
    return d

@pytest.fixture # fail demo
def fDemo():
    d = Demo(False,False)
    return d

def bDemo():
    d = Demo("Yes","No")
    return d    

#### EXAMS #######################################################
@pytest.fixture
def passA_Exams():  # pass ALL exams 
    e = Exams([100,90,80])
    return e

@pytest.fixture
def failA_Exams():  # fail ALL exams 
    e = Exams([44,30,0,1])
    return e

@pytest.fixture
def fail_1_Exams():  # fail 1 exam
    e = Exams([100,90,44])
    return e

@pytest.fixture
def noExams():  # no exams 
    e = Exams()
    return e

@pytest.fixture
def bounds_Exams():  # scores out of bounds 
    e = Exams([100,90, -1, 80,44,70, 101])
    return e

#### THESIS ######################################################
@pytest.fixture # A & PUBLISH
def a_Thesis():
    t = Thesis("Solving the Housing Crisis", True, 'A')
    return t

@pytest.fixture # B & PUBLISH
def b_Thesis():
    t = Thesis("Adventures with Pandas", True, 'B')
    return t

@pytest.fixture # C & DONT publish 
def c_Thesis():
    t = Thesis("All About Birds", False, 'C')
    return t

@pytest.fixture # D & DONT publish 
def d_Thesis():
    t = Thesis("What My Cat Mr. Tufty is Thinking", False, 'D')
    return t

@pytest.fixture # F & DONT publish 
def f_Thesis():
    t = Thesis("Algorithims and Complexity", False, 'F')
    return t

@pytest.fixture # F & PUBISH
def fp_Thesis():
    t = Thesis("My Adventures with Tequila", True, 'F')
    return t

@pytest.fixture # Letter out of Bounds
def O_Thesis():
    t = Thesis("Letter out of bounds", True, 'E')
    return t

@pytest.fixture # Not boolean
def bool_Thesis():
    t = Thesis("Not boolean", "yes", 'E')
    return t
    

##### STUDENT ######################################################   
@pytest.fixture # list of students with NO courses
def stdntEmptyCourseList():
    SIZE = 6
    students = []
    for x in range(SIZE):
        students.append(Student(studentNames[x]))
    return students 

@pytest.fixture # list of students used in main 
def stdntTestList():
    SIZE = 6
    students = []
    for x in range(SIZE):
        students.append(Student(studentNames[x]))
        for y in range(-1,2):
            course = Course(courseNames[y], demoList[y], exList[y], thesList[y])
            students[x].addCourse(course)
    return students 