# test_structures.py
########################################################################
# KENDRA WAINSCOTT             Prog 4/5            CS202 Winter 2022
########################################################################
# This file contains testing for the Student and Concept classes 
########################################################################
from  gradeClasses import Grade, Demo, Exams, Thesis
from structures import Course, Student
import conftest

import pytest
from math import inf

############################# Test Constructors ########################

# students with name but empty course list
def test_student_init(stdntEmptyCourseList):
    for x in range(len(stdntEmptyCourseList)):
        assert(stdntEmptyCourseList[x]._name != "")
        assert(stdntEmptyCourseList[x]._headClist == None)

# students with name & full course list of 6 classes
def test_student_init(stdntTestList):
    for x in range(len(stdntTestList)):
        assert(stdntTestList[x]._name != "")
        assert(stdntTestList[x]._headClist != None)
        assert(stdntTestList[x].printStudent(1) == 6)

