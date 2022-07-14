# test_grades.py
########################################################################
# KENDRA WAINSCOTT             Prog 4/5            CS202 Winter 2022
########################################################################
# This file contains testing for all of the derived grade classes 
# Demo, Exams, Thesis
########################################################################
from  gradeClasses import Grade, Demo, Exams, Thesis
import pytest

############################# Test Constructors ########################

# Test valid init assignment names 
def test_grades_assignment(pDemo, fDemo, passA_Exams, failA_Exams, a_Thesis, f_Thesis):
    assert( pDemo._assignment == "Demo")
    assert( fDemo._assignment == "Demo")
    assert( passA_Exams._assignment == "Exams")
    assert( failA_Exams._assignment == "Exams")
    assert( a_Thesis._assignment == "Thesis")
    assert( f_Thesis._assignment == "Thesis")

# Test out of bounds init input 
#def test_init_bounds(bDemo, bounds_Exams, noExams, O_Thesis, bool_thesis):
    #assert( bDemo ==)   



# Test demo init fields 
def test_init_demo(pDemo, fDemo):
    assert( pDemo._passNopass == True)
    assert( pDemo._debugger == True)
    assert( pDemo._autoFail == False )
    assert( fDemo._passNopass == False)
    assert( fDemo._debugger == False)
    assert( fDemo._autoFail == True )

# Test Exams init fields

# Test Thesis init fields 

# test autofail 
def test_init_exams(passA_Exams, failA_Exams, fail_1_Exams):
    assert( passA_Exams._autoFail == False )
    assert( failA_Exams._autoFail == True )
    assert( fail_1_Exams._autoFail == True )

# bounds_Exams noExams


'''def test_overide(fDemo, failA_Exams, f_Thesis):
    pass


def test_final_init(aFinal):
    pass

def test_student_init(aStudent):
    pass

########################## Test Common Base  ############################
def test_output(aGrad, aDemo, aExams, aThesis):
    pass

############################ Test Unique  ###############################
def test_assignRedo(aDemo): 
    pass

def test_average(aExams):
    pass

def test_updateScore(aExams):
    pass

def test_changeTopic(aThesis):
    pass
        
def test_defense(aThesis):
    pass
'''
#######################################################################