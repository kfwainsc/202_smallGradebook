# input.py   "grades"  
##################################################################
# KENDRA WAINSCOTT           Prog 4/5          CS202 Winter 2022
#
# This file is input for the derived grade classes
# It is used to build a starting gradebook database for main
##################################################################
from gradeClasses import Grade, Demo, Exams, Thesis
from structures import Student, Course

#### DEMO #########################################################
demoList = []
demoList.append(Demo(True,True))
demoList.append(Demo(True,False))
demoList.append(Demo(False,True))
demoList.append(Demo(False,False))
demoList.append(Demo(True,True))
demoList.append(Demo(True,False))
#### EXAMS #################################################################
exList = []
exList.append(Exams([100,90,80]))
exList.append(Exams([44,30,0,21]))
exList.append(Exams([100,90,44]))
exList.append(Exams([10,50,80]))
exList.append(Exams([99,88,82,76]))
exList.append(Exams([100,90]))
#### THESIS ################################################################
thesList = []
thesList.append(Thesis("Solving the Housing Crisis", True, 'A'))
thesList.append(Thesis("Adventures with Pandas", True, 'B'))
thesList.append(Thesis("All About Birds", False, 'C'))
thesList.append(Thesis("What My Cat Mr. Tufty is Thinking",False,'D'))
thesList.append(Thesis("Algorithims and Complexity", False, 'F'))
thesList.append(Thesis("My Adventures with Tequila", True, 'F'))
### COURSE NAMES ###########################################################
courseNames = ["ALGORITHIMS & PAIN", "CS202",
               "INTRO TO WEB AND SPIDER DEVELOPMENT",
               "OP SYSTEMS AND OPERATIONS ON THEM",
               "CS302 - Gotcha", "ROCKS FOR JOCKS"]
### STUDENT NAMES ###########################################################
studentNames = ["Carole Singer", "Felix Cited", "Jack Pott", "Jai Walker", 
                "Serge A. Head", "Warren Peace" ]

# Create list of students with courses for gradebook in main 
