# gradeClasses.py
##########################################################################
# KENDRA WAINSCOTT             Prog 4/5          CS202 Winter 2022 
#
# This file contains all class definitions for the Grade hierarchy
##########################################################################
#-------------------  GRADE  ------------------------------------
# Purpose: Common base class for Demo, Exams and Thesis classes
#          holds basic information common to all 3 derived classes 
# Fields: name of assignment (what derived will be)
#         feedback (if any) as a string 
#         total score averaged from all scores of derived
#         auto fail, triggered if derived has min unmet criteria          
##########################################################################
class Grade:

    # default constructor
    def __init__(self, assignment) :
        self._assignment = assignment
        self._feedback = None
        self._total = None
        self._autoFail = False

    # Job: overide auto fail, if student has updated scores or other
    # Ret: returns false if autofail had NOT been triggered, else true
    def overide_autoFail(self):
        if self._autoFail == False:
            return False
        self._autoFail = False
        return True 

    # Job: add optional feedback to score 
    # Ret: true if feedback given, else false 
    def give_feedback(self):
       self._feedback =  input("Enter Feedback: ")

    # Job: output all datafields 
    # Ret: 1 if all fields valid, else raises exception
    def output(self):
        if self._assignment == None:
            raise Exception("Invalid Assignment")
        else:
            print(self._assignment,"Total:",self._total,"Feedback:",
                  self._feedback)
        return 1

##########################################################################
#-------------------  DEMO  ----------------------------------------------
# Purpose: child of Grade class, if demo NP student will auto fail class
# Fields: bool Pass/No pass and bool use of debugger  
##########################################################################
class Demo(Grade):
    
    # constructor with scores, error check are boolean vals
    # Note: False = NP, True = Pass
    def __init__(self, passNopass, debugger) :

        # check valid init values 
        if (passNopass == False  or  passNopass == True) \
        and (debugger == False  or  debugger == True) :
            # call base constructor 
            Grade.__init__(self,"Demo")
            self._passNopass = passNopass
            self._debugger = debugger
            # check for autofail 
            if passNopass == False:
                self._autoFail = True
                self._total = 0
            else:
                self._total = 100
                self._autoFail = False
        else:
            raise Exception("Invalid Init Values")

    # Job: assign redo 
    # Ret: true if assigned, else false 
    def assignRedo(self):
        ret = input("Send Redo Requierment Message? (y|n): ")
        if ret == 'y' or ret == 'Y':
            return True
        return False

    # Job: update demo fields
    # Ret: return new P/NP value
    def update(self):
        print("Enter 'True' or 'False' values")
        self._debugger = input("Use of GDB?: ")
        self._passNopass = input("Pass for Demo?: ")
        return self._passNopass

    # Job: output all datafields 
    # Ret: 1 if all fields valid, else raises exception
    def output(self):
        if self._assignment != "Demo" :
            raise Exception("Invalid Assignment")
        else:
            print("--  ", self._assignment, "  --")
            if (self._passNopass == None) or (self._debugger == None):
                print("No scores yet.\n")
            else:
                if self._passNopass == False : print("NP")
                else : print("PASS")
                print("Debugger Use:", self._debugger)
                print("Feedback:", self._feedback)
        return 1


##########################################################################
#-------------------  EXAMS  ---------------------------------------------
# Purpose: child of Grade class, less than 45 an ANY exam is autofail
# Fields: number of total exams for the class
#         list of all exam scores 
##########################################################################
class Exams(Grade):

    # constructor with num exams & list of scores
    def __init__(self,scores) :
        Grade.__init__(self,"Exams")
        self._numExams = len(scores)
        self._allExams = scores
        # check for autofail 
        for i in range(len(self._allExams)):
            if self._allExams[i] < 45:
                self._autoFail = True
        # average total of all exams, updates self._total
        self.average()

    # Job: average list of all exam scores, updates self._total
    # Ret: true if valid exam values, else exception 
    def average(self):
        if (self._numExams == 0) or (len(self._allExams) == 0):
            raise Exception("Invalid Exams Values")
        else:
            total = 0
            for i in range(len(self._allExams)):
                total += self._allExams[i]
            self._total = total
            self._total = total // self._numExams
    
    # Job: add scores to list of exam scores 
    # Arg: list of scores, appends to end of existing score list '
    # Ret: returns true if valid scores, else exception
    def addScores(self, scores):
        if len(scores) < 1 :
            raise Exception("Invalid Exam Score List")
        for i in range(len(scores)):
            self._allExams.append(scores[i])
            if scores[i] < 45:
                self._autoFail = True
        # average total of all exams, updates self._total
        self.average()
        return True 

    # Job: output scores of all exams 
    # Ret: true if exam list not empty, else exception 
    def outExamsList(self):
        if len(self._allExams) == 0 or self._numExams == 0 :
            raise Exception("Invalid Exam List")
        else:
            for i in range(len(self._allExams)):
                print("Exam",i,":",self._allExams[i])
        return True

    # Job: output all Exams obj contents 
    # Ret: true if all fields valid, else exception 
    def output(self):
        if self._assignment != "Exams" :
            raise Exception("Invalid Assignment")
        else:
            print("--  ", self._assignment, "--  ")
            if self._total == None:
                print("No scores yet.\n")
            else:
                self.outExamsList()
                print("Total Score:",self._total)
        return True
    
##########################################################################
#-------------------  THESIS  -------------------------------------------
# Purpose: child of Grade class, is full letter graded (no + or -), 
#         F is an autofail 
# Fields: topic of thesis as a string
#         bool if tb published 
#         letter grade char
##########################################################################
class Thesis(Grade):

    # constructor with init values 
    def __init__(self, topic, publish, letterGrade) :
        # check for valid input 
        if (letterGrade <= 'F') or (letterGrade >= 'A') :
            # call base constructor 
            Grade.__init__(self,"Thesis")
            self._topic = topic
            self._topublish = publish
            self._letterGrade = letterGrade

            # check for autofail, update total
            if letterGrade  == 'F':
                self._autoFail = True
                self._total = 0
            else:
                self.convertLetter()
        else:
            raise Exception("Invalid Init Values")

    # Job: convert letter grade to % 
    def convertLetter(self):
        if self._letterGrade < 'B':
            self._total = 100
        elif self._letterGrade < 'C':
            self._total = 89 
        elif self._letterGrade < 'D':
            self._total = 79
        elif self._letterGrade < 'F':
            self._total = 69
        else:
            self._total = 59

    # Job: change topic of thesis 
    def changeTopic(self):
        self._topic = input("Enter new thesis topic: ")

    # Job: schedule defenses for thesis 
    # Ret: T if scheduled, else false 
    def defense(self):
        date = input("Enter Date for defense: ")
        ret = input("Send calendar invite? (y|n): ")
        if ret == 'y' or ret == 'Y':
            return True
        return False

    # Job: publish thesis 
    # Ret: true if topublish is true
    def publish(self):
        if self._topublish != True:
            print("This is not recommended.")
            return False
        publisher = input("Enter Publisher: ")
        return True

    # Job: output all Exams obj contents 
    # Ret: true if all fields valid, else exception 
    def output(self):
        if self._assignment != "Thesis" :
            raise Exception("Invalid Assignment")
        else:
            print("-- ", self._assignment, "  --")
            if self._total == None:
                print("No score Yet.\n")
            else:
                print("Topic: ", self._topic)
                print("To Publish:", self._topublish)
                print("Feedback: ",self._feedback)
                print("Letter Grade: ", self._letterGrade)
        return True
    
##########################################################################
##########################################################################
