#  main.py  
########################################################################
# KENDRA WAINSCOTT               Prog 4/5           CS202 Winter 2022
#
# The purpose of this program is to simulate a gradebook, it supports 
# three different kinds of grades 'Demo', 'Exams', and 'Thesis' all 
# derived from a common 'Grade' base class. 
# A Course object stores all of the derived grade objects for one subject
# along with the name of the subject and the student's final grade for
# the course. 
# The collection of all of the grades for one student is then held in
# a LLL class named 'Student' and these students are held in a Tree. 
# This program also includes a test suite for black box testing.
########################################################################
from gradeClasses import Grade, Demo, Exams, Thesis
from structures import Course, Student
from input import demoList, exList, thesList, courseNames, studentNames
import utility
from rbtree import RedBlackTree

def main():
    
    print("\nGrade Book Project #4/5\nKendra Wainscott")
    print("#######################################################\n\n")

    # create list of LLL Students to work with from input file
    SIZE = 6
    students = []
    bst = RedBlackTree()

    for x in range(SIZE):
        students.append(Student(studentNames[x]))
        for y in range(SIZE):
            course = Course(courseNames[y], demoList[y], exList[y], thesList[y])
            students[x].addCourse(course)

    # add students to Red-Black-Tree
    for x in range(SIZE):
        bst.insert(students[x])

    done = False
    choice = 0
    while done != True:
        utility.mainMenu()
        choice = input("CHOICE:")
        choice = int(choice)

        if choice == 0:
            done = True

        elif choice == 1: # Search for Student
            key = input("Full Student Name:")
            struct = input("Work in BST or List? Answer( B | L )")

            location = -1
            if struct == 'L':
                for x in range(len(students)):
                    if students[x] == key:
                        location = x
            if struct == 'B':
                found = bst.search(key)

            if location >= 0 or found != None:
                print("MATCH FOUND")
                print("View Menu Options for this student?")
                answer = input("(y|n)\nANSWER:")
                if answer == "y" or answer == "Y":
                    utility.studentMenu(location, students)
                    # have not implemented for BST
                      
        elif choice == 2: # View all Student Names
            #for x in range(len(students)):
            #    students[x].printStudent(0)
            order = input("Print student is Preoder(0), Inorder(1), Postorder(2): ")
            order = int(order)
            bst.printTree(order,0)
        
        elif choice == 3: # View all Students with Grades
            #for x in range(len(students)):
            #    students[x].printStudent(1)
            order = input("Print student is Preoder(0), Inorder(1), Postorder(2): ")
            order = int(order)
            bst.printTree(order,1)

        elif choice == 4: #() Add a Student")
            students.append(Student(input("Student Name:")))        
            bst.insert(Student(input("Student Name:")))

            print("Tree & List have Added Student")
            print("Add course for this student in LIST? (y|n)")
            answer = input("ANSWER:")
            # COURSES
            while answer == "y" or answer == "Y":
                cName = input("Course Name:")
                # DEMO
                pnp = input("Demo Passed? (y|n)")        
                if pnp == "y" or pnp == "Y":
                    D = Demo(True,True)
                else: D = Demo(False,False)
                # EXAMS
                num_e = int(input("Number of Exams:"))    
                exScores = []
                for x in range(num_e):
                    print("Enter Score",(x+1))
                    exScores.append(int(input(":")))
                E = Exams(exScores) 
                # THESIS
                tName = input("Thesis Topic: ")
                letter = input("Letter Grade (in CAPS): ")        
                pnp = input("To Publish? (y|n)")        
                if pnp == "y" or pnp == "Y":
                    T = Thesis(tName, True, letter)
                else: T = Thesis(tName, False, letter)

                course = Course(cName, D, E, T)
                students[len(students)-1].addCourse(course)    
                #bst.studentWork("add course" course)

                print("Add ANOTHER course for this student? (y|n)")
                answer = input("ANSWER:")

        elif choice == 5: # Remove a Student"
            key = input("Full Student Name:")

            found = bst.deleteNode(key)
            if found != None:
                print("Student Removed")
            else: print("Student NOT found")
            '''
            location = -1
            for x in range(len(students)):
                if students[x] == key:
                    print("MATCH FOUND")
                    location = x
            if location >= 0:
                students.pop(location)
            '''

        elif choice == 6: # Output Student Transcript to File
           pass 


if __name__ == "__main__":
    main()