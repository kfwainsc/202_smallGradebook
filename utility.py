# utility.py  "grades"  
##################################################################
# KENDRA WAINSCOTT           Prog 4/5          CS202 Winter 2022
#
# This file contains menu and other utility functions
##################################################################
def mainMenu():
    print("Gradebook Options\n----------------------------------------")
    print("1) Search for Student to update/view")
    print("2) View all Student Names")
    print("3) View all Students with Grades")
    print("4) Add a Student")
    print("5) Remove a Student")
    print("0) QUIT")

def outStudentMenu():
    print("Student Options\n----------------------------------------")    
    print("1) View Final Grades")
    print("2) Select a Course to Update/Edit Grades")

def studentMenu(location, sList):
    done = False # student menu
    while done != True:
        outStudentMenu()
        choice = input("\nCHOICE:")
        choice = int(choice)

        if choice == 0: # Main menu
            done = True
        
        elif choice == 1: # View Final Grades
            sList[location].printStudent(1)

        elif choice == 2: # Select Course Update/Edit Grades
            key = input("Enter course name: ")
            foundCourse = sList[location].findCourse(key, 0)
            if foundCourse != None:
                gradesMenu(foundCourse)
            else:
                print("No Matching Course Found")

        else: pass # invalid menu option

def outGradesMenu():
    print("Course Options\n----------------------------------------")    
    print("1) Give Feedback")
    print("2) Review Results")
    print("3) Assign Demo Redo")
    print("4) Update Demo")
    print("5) View Exam Scores")
    print("6) Add Exam Scores")
    print("7) Publish Thesis")
    print("8) Change Thesis Topic")
    print("9) Schedule thesis defense")
    print("10) Overide Autofail")
    print("0) STUDENT MENU")

# Job: loop through all menu options till quit
# Arg: course tb used 
def gradesMenu(foundCourse):
    done = False # student menu
    while done != True:
        outGradesMenu()
        choice = input("\nCHOICE:")
        choice = int(choice)

        if choice == 0: # Main menu
            done = True

        elif choice == 1: # give feedback 
            print("Choose Assignment for Feedback ")
            char = input("D=Demo | E=Exams | T=Thesis : ")
            if foundCourse.addFeedback(char):
                print("Feedback Added!")

        elif choice == 2: # View Results
           foundCourse.output()
           
        elif choice == 3: # Assign Demo Redo
            ret = foundCourse.alterAssignments('D', 3)

        elif choice == 4: # Update Demo Results
            ret = foundCourse.alterAssignments('D', 4)

        elif choice == 5: # View Exam Scores
            ret = foundCourse.alterAssignments('E', 5)

        elif choice == 6: # Add Exam Scores
            ret = foundCourse.alterAssignments('E', 6)

        elif choice == 7: # Publish
            ret = foundCourse.alterAssignments('T', 7)

        elif choice == 8: # Change Thesis Topic
            ret = foundCourse.alterAssignments('T', 8)

        elif choice == 9: # schedule Thesis Defense
            ret = foundCourse.alterAssignments('T', 9)

        elif choice == 10: # overide auto fail
            print("Failed: ",foundCourse.checkAutofail())
            ret = foundCourse.alterAssignments('O', 0)

        else: # invalid menu option
            pass
