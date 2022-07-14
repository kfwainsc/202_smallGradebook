# structures.py  "grades"  
##################################################################
# KENDRA WAINSCOTT           Prog 4/5          CS202 Winter 2022
#
# This file contains the implementation for the Student LLL class
# which holds a list of all grades for a given student in the form
# of Course class objects.
###################################################################
##################################################################
#------------  COURSE  -------------------------------------------
##################################################################
# Purpose: a course acts as a containter for all the assignments 
#          for a given course. It is used as a node in the Student 
#          class, which is a LLL of grades and student name
# Fields:  course name as a string
#          Demo, Exams, and Thesis objects
#          final grade for the course 
#          list of any assignment sections failed 
#          marker to next course in the students LLL of courses
##################################################################
class Course:

    # Job: constructor wt already formed derived grades
    # Arg: Demo, Exams, Theis objects and the name of the course 
    def __init__(self,course,demo,exams,thesis):
        self._course = course
        self._demo = demo
        self._exams = exams
        self._thesis = thesis
        self._sectionsFailed = []
        self._finalGrade = self.calcFinalG()
        self._nextCourse = None

    # Job: average all assignments sections total scores
    # to calculate final grade for course 
    # Ret: final grade for course, exception if 0 
    def averageAll(self):
        total = 0
        total = self._demo._total + self._exams._total \
                + self._thesis._total
        if total == 0:
            raise Exception("Confirm final Grade of 0") 
        else:
            total /= 3
        return total 

    # Job: check for auto fail in all assignment sections,
    # append to self._sectionsFailed if auto fail == true
    # Ret: list of assignmet sections failed 
    def checkAutofail(self):
        if self._demo._autoFail == True:
            self._sectionsFailed.append(self._demo._assignment)
        if self._exams._autoFail == True: 
            self._sectionsFailed.append(self._demo._assignment)
        if self._thesis._autoFail == True :
            self._sectionsFailed.append(self._demo._assignment)
        return self._sectionsFailed

    # Job: calculate final grade for the course
    def calcFinalG(self):
        self.checkAutofail()
        if len(self._sectionsFailed) != 0:
            self._finalGrade = 'F' 
        else: 
            self._finalGrade = self.averageAll()

    # Job: add feedback to assignments
    # Arg: char for which assignment to access 
    # Ret: returns T for valid char, else exception
    def addFeedback(self, char):
            if char == "D" or char == "d":
               self._demo.give_feedback()

            elif char == "E" or char == "e":
                self._exams.give_feedback()           

            elif char == "T" or char == "t":
               self._thesis.give_feedback()

            else: raise Exception("Invalid Assignment")
            return True

    # Job: add feedback to assignments
    # Arg: char for which assignment to access 
    # Ret: returns T for valid char, else exception
    def alterAssignments(self, char, choice):
            ret = False
            if char == "D" or char == "d":
                if choice == 3:
                    ret = self._demo.assignRedo()
                elif choice == 4:
                    ret = self._demo.update()

            elif char == "E" or char == "e":
                if choice == 5:
                    ret = self._exams.outExamsList()
                if choice == 6:
                    numScores = int(input("Number of exams to add: "))
                    if numScores > 0:
                        scores = []
                        for x in range(numScores):
                            inScore = int(input("Score: "))
                            scores.append(inScore)
                    ret = self._exams.addScores(scores)

            elif char == "T" or char == "t":
                if choice == 7:
                    ret = self._thesis.publish()
                elif choice == 8:
                    ret = self._thesis.changeTopic()                
                elif choice == 9:
                    ret = self._thesis.defense() 

            elif char == "O":
                self._demo._autoFail == False
                self._exams._autoFail == False
                self._thesis._autoFail == False
                print("Overide Applied.")
                ret = True
            else: raise Exception("Invalid Assignment")
            return ret

    # Job: set the next course marker to passed in course
    # Arg: next course in the list
    def setNext(self,nextCourse):
        self._nextCourse = nextCourse

    # Job: check if there is a next item in the list
    # Ret: true if is a next, else false
    def isNext(self):
        if self._nextCourse == None:
            return False
        else: return True

    # Job: move to next course in the list
    # Ret: next item in list
    def goNext(self):
        return self._nextCourse

    # Job: check if passed key is a match to course
    # Ret: true if match, else false
    def matchCourse(self, key):
        return self._course == key 

    # Job: print contents of course node 
    # Ret: 1 if valid fields, derived will throw exceptions
    def output(self):
        print("\n<<< CLASS:",self._course,">>>")
        self._demo.output()
        self._exams.output()
        self._thesis.output()
        return 1
##################################################################
#-----------  STUDENT  -------------------------------------------
##################################################################
# Purpose: represents an individual student, is a LLL of courses 
# Fields:  student name as a string 
#          head of a LLL of courses   
##################################################################
class Student:

    # constructor, set student name, course list empty
    def __init__(self,name):
        self._name = name
        self._headClist = None # head of course LLL

    # Job: add a course to the front of the course LLL
    # Arg: course to be added, exception if invalid course 
    def addCourse(self, course): # add new course @ head of list
        if self._headClist == None:
           self._headClist = course
           #self._headClist.setNext(None)
        else:
            hold = self._headClist
            self._headClist = course 
            self._headClist.setNext(hold)

    # Job: search for a course by name  with key in the LLL
    # Arg: keyword course name to search for
    # Ret: course data
    def findCourse(self, key, directive):
        if self._headClist.matchCourse(key):
            return self._headClist
        else:
            return self._findCourse(key,self._headClist.goNext())
 
    def _findCourse(self, key, temp):
        if temp.matchCourse(key):
            temp.output()
            print("MATCH COURSE")
            return temp
        if temp.isNext() == False:
            return None
        return self._findCourse(key, temp.goNext())


    # Job: recursively print entire list of courses
    # Ret: number of courses printed 
    def _printCourses(self, temp):
        temp.output()
        if temp.isNext() == False:
            return 1
        else:
            return self._printCourses(temp.goNext()) +1

    # Job: wrapper to print entire list of courses
    # Ret: number of courses printed 
    def printCourses(self):
        if self._headClist == None: # empty list
            return 0 
        elif self._headClist.isNext() == False:
            self._headClist.output() #  1 item in list
            return 1
        else:
            return self._printCourses(self._headClist) 

    # Job: output student info, with or without course list
    # Arg: choice value 1 will print course list as well
    # Ret: courses printed  
    def printStudent(self, choice):
        ret = 0
        print("\n\nSTUDENT NAME: ", self._name)
        print("=========================================")
        if choice == 1:
            print("COURSE LIST\n=========================================")
            ret = self.printCourses()
        print("=========================================")
        return ret

    #################### OVERLOADED STUDENT OPERATORS ##################    
    ########### STUDENT & STUDENT ###########

    # Job:  ==  overloaded EQUALITY op for use in other data structures. 
    # Ret: result of comparison of name fields 
    def __eq__(self, op2):
        return self._name == op2

    # Job:  !  overloaded NOT EQ operator, compares two student names
    def __ne__(self, op2):
        return self._name != op2._name

    # Job:  <  overloaded LESS than operator, compares two student names
    def __lt__(self, op2):
        return self._name < op2._name

    # Job:  >  overloaded GREATER than operator, compares two student names
    def __gt__(self, op2):
        return self._name > op2._name

    # Job:  <=  overloaded LESS/EQ operator, compares two student names
    def __le__(self, op2):
        return self._name <= op2._name

    # Job:  >=  overloaded GREATER/EQ operator, compares two student names
    def __ge__(self, op2):
        return self._name >= op2._name

    # STUDENT & KEY  ##########################################################
    ###########################################################################

    # Job: since equality ops overloaded for Student objects
    # Arg: string key of name to match, string of comparison operator
    # Ret: True / False of comparison, exception if invalid operator 
    def compareKey(self, key, strOperator):
        if strOperator == "==":
            return self._name == key
        if strOperator == "!=":
            return self._name != key
        if strOperator == "<":
            return self._name < key
        if strOperator == ">":
            return self._name > key
        if strOperator == "<=":
            return self._name <= key
        if strOperator == ">=":
            return self._name >= key
        raise Exception("Unsupported Comparison Operator")
