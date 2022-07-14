# rbtree.py  
##################################################################
# KENDRA WAINSCOTT           Prog 5          CS202 Winter 2022
#
# This file contains the implementation for the Red Black Balanced
# Tree and the implementation for the Node which the RB tree uses
# to hold a collection of Student objects. Both classes are 
# written generically to allow for reuse with different class types
# trypes. A Red-Black tree is used to emulate a 2-3-4 tree by using
# color flags to note interior/exterior relationships. 
###################################################################
###################################################################
#------------  NODE  -------------------------------------------
##################################################################
# Purpose: a Node acts as a containter for a Student object which 
#          is a LLL of all the Courses for a given student.
# Fields:  
#          item (here a Student object)
#          parent of the node
#          left and right holding onto any children
#          color 'Red' or 'Black' indicating interior/exterior 
##################################################################
class Node():

    # constructor with item to hold
    def __init__(self, item):
        self._item = item
        self.parent = None
        self.left = None
        self.right = None
        self._color = 1

    # Job: check if left child, True if exisits, else False
    def checkLeft(self):
        if self.left == None:
            return False
        return True

    # Job: check if right child, True if exisits, else False    
    def checkRight(self):
        if self.right == None:
            return False
        return True

    # Job: check if Node is a leaf, True if leaf, else False
    def isLeaf(self):
        if (self.left == None) and (self.right == None):
            return True
        return False

    # Job: set parent, child, or parent-child branches 
    # Arg: P=parent, L=left, R=right
    def setBranch(self, branch, node):
        if branch == 'P':
            self.parent = node
        elif branch == 'L':
            self.left = node
        elif branch == 'R':
            self.right = node
        else:
            raise Exception("Invalid Input Branch")
        return True 

    # Job: return color of current node or branches
    # Arg: S=self, P=parent, L=left, R=right
    def getColor(self, branch):
        if branch == 'S':
            return self._color
        if branch == 'P':
            return self.parent._color
        if branch == 'L':
            return self.left._color
        if branch == 'R':
            return self.right._color
        raise Exception("Invalid Input Branch")

    # Job: set color of current node from given color
    # Ret: new color
    def setColor(self, color):
        self._color = color
        return self._color

    # Job: set color of current node from passed in node
    # Ret: new color
    def setColorNode(self, node):
        self._color = node._color
        return self._color

    # Job: set color of self or branch node
    # Arg: S=self P=parent L=left R=right 
    # Ret: new color
    def setColorBranch(self, branch, color):
        if branch == 'S':
            self._color = color
        elif branch == 'P':
            self.parent._color = color
        elif branch == 'PP':
            self.parent.parent._color = color
        elif branch == 'L':
            self.left._color = color
        elif branch == 'R':
            self.left._color = color
        else:
            raise Exception("Invalid Input Branch")

    # Job: get L or R child of current node 
    def getChild(self, branch):
        if branch == 'L':
            return self.left
        if branch == 'R': 
            return self.right
        raise Exception("Invalid Input Branch")

    # Job: get parent 'P' or child of parent 'L'/'R' 
    # or parent of parent 'PP or child of pp-> PPR/PPL
    def getParent(self, branch):
        if branch == 'L':
            return self.parent.left
        if branch == 'R': 
            return self.parent.right
        if branch == 'P':
            return self.parent
        if branch == 'PP':
            return self.parent.parent
        if branch == 'PPL':
            return self.parent.parent.left
        if branch == 'PPR':
            return self.parent.parent.right
        raise Exception("Invalid Input Branch")

    # Job: for Search, compare item to passed in string key,
    # relational operators already overloaded for Node & Node     
    def strItemComp(self, keyStr, operatorStr):
        return self._item.compareKey(keyStr, operatorStr)

    #### OVELOADED NODE & NODE RELATIONAL OPERATORS ##########
    # Job:  ==  overloaded EQUALITY comparison of item fields 
    #def __eq__(self, op2):
    #    return self._item == op2._item
    # Job:  !=  overloaded NOT EQ comparison of item fields 
    #def __ne__(self, op2):
    #    return self._item != op2._item

    # Job:  <  overloaded LESS than operator, compares item fields 
    def __lt__(self, op2):
        return self._item < op2._item

    # Job:  >  overloaded GREATER than operator, compares item fields 
    def __gt__(self, op2):
        return self._item > op2._item

    # Job:  <=  overloaded LESS/EQ operator, compares item fields
    def __lt__(self, op2):
        return self._item <= op2._item

    # Job:  >=  overloaded GREATER/EQ operator, compares item fields
    def __gt__(self, op2):
        return self._item >= op2._item

###################################################################
#------------  RBTREE  -------------------------------------------
##################################################################
# Purpose: the Red-Black tree is a data structure that holds a 
#          collection of class Student objects inside of the 
#          Nodes class. It is a balanced tree, performing rotations
#          and relationship color changes to self balance. 
# Fields:  
#          root of the tree 
##################################################################
class RedBlackTree():

    # Job: constructor 
    def __init__(self):
        self._root = None

    # Job: insert new item into the tree
    # Arg: new data to store in node and insert into tree  
    def insert(self, data):
        if self._root == None: # empty tree 
            self._root = Node(data)
            return  
        newNode = Node(data)
        rebal = False
        if self._root.isLeaf(): # only 1 node
            newNode.setBranch('P', self._root) #= self._root
            if newNode < self._root:
                self._root.setBranch('L', newNode)
            else:
                self._root.setBranch('R', newNode)
        else:
            if newNode < self._root:
                rebal = self._insert(newNode, self._root.getChild('L'))
            else:
                rebal = self._insert(newNode, self._root.getChild('R'))
        # rebalance tree if needed 
        if rebal:
            self.balanceInsert(newNode) 

    # Job: recursive insert new item into tree
    # Arg: new Node tb added, current node that will be ancestor
    # Ret: false if tree does not need to be rebalanced, else true 
    def _insert(self, newNode, ancestor):
        if ancestor == None: 
            return 
        if ancestor.isLeaf():  
            newNode.setBranch('P', ancestor) # parent = ancestor
            if newNode < ancestor : # newNode < parent 
                ancestor.setBranch('L', newNode) 
            else:
                ancestor.setBranch('R', newNode) # newNode < parent
            # check if needs to be rebalanced 
            if newNode.getParent('PP') == None:
                return False
            return True
        if newNode < ancestor:
            return self._insert(newNode, ancestor.getChild('L'))
        else:
            return self._insert(newNode, ancestor.getChild('R'))

    # Job: rebalance tree after insert, through color flag 
    # changes and L or R rotations
    # Args: passed in node move
    def balanceInsert(self, node):
        while (node != self._root) and (node.getColor('P') == 1) :
            if node.getParent('P') == node.getParent('PPR'):
                curr = node.parent.getParent('L')
                if curr != None and curr.getColor('S') == 1:
                    curr.setColor(0)
                    node.setColorBranch('P',0)
                    node.setColorBranch('PP',1)
                    node = node.getParent('PP')
                else:
                    if node == node.getParent('L'):
                        node = node.getParent('P')
                        self._rotateRight(node) # ROTATE R
                    node.setColorBranch('P',0)
                    node.setColorBranch('PP',1)
                    self._rotateLeft(node.getParent('PP'))
            else:
                curr = node.getParent('PPR')
                if curr!= None and curr.getColor('S') == 1:
                    curr.setColor(0)
                    node.setColorBranch('P', 0)
                    node.setColorBranch('PP', 1)
                    node = node.getParent('PP')
                else:
                    if node == node.getParent('R'):
                        node = node.getParent('P')
                        self._rotateLeft(node) # ROTATE L
                    node.setColorBranch('P', 0)
                    node.setColorBranch('PP',1)
                    self._rotateRight(node.getParent('PP'))
        self._root.setColor(0)

    # Job: search tree for key tb found 
    # Ret: node if found, else None
    def search(self, key):
        return self._search(self._root, key)

    # Job: recursively search treee for key tb found 
    # Ret: node if found, else None
    def _search(self, current, key):
        if current.isLeaf() == True: 
            return None
        if current.strItemComp(key, "=="): 
            return current 
        if current.strItemComp(key, ">"): # key < current
            return self._search(current.getChild('L'), key)
        return self._search(current.getChild('R'), key)

    # Job: delete a node from the tree
    # Arg: item tb deleted 
    # Ret: None if item not found, else True
    def deleteNode(self, key):
        if self._root == None: 
            return None 
        return self._deleteNode(self._root, key)


    # Job: helper to delete a node from the tree
    # Arg: current node, key for tb deleted 
    def _deleteNode(self, current, key):
        comp = None
        while current != None:
            if current.strItemComp(key,"=="):
                comp = current
            if current.strItemComp(key,">"): # key < current
                current = current.getChild('L')
            else:
                current = current.getChild('R') 
        if comp == None:
            return None
        n1 = comp
        n1.original_color = n1.getColor('S')
        if comp.checkLeft() == False:
            x = comp.right
            self._swap(comp, comp.right)
        elif (comp.checkRight() == False):
            x = comp.left
            self._swap(comp, comp.left)
        else:
            n1= self._findMin(comp.right)
            n1.original_color = n1.getColor('S')
            x = n1.right
            if n1.parent == comp:
                x.parent = n1
            else:
                self._swap(n1, n1.right)
                n1.right = comp.right
                n1.right.parent = n1

            self._swap(comp, n1)
            n1.left = comp.left
            n1.left.parent = n1
            n1.setColor(comp)
        if n1.original_color == 0:
            self._balanceDelete(x)
        return True

    # Job: rebalance tree after deletion 
    def _balanceDelete(self, x):
        while x != None  and  x != self._root and x.getColor('S') == 0:
            if x == x.getParent('L'):
                n1 = x.getParent('R')
                if n1.getColor('S') == 1:
                    n1.setColor(0)
                    x.setColorBranch('P',1)
                    self._rotateLeft(x.getParent('P'))
                    n1 = x.getParent('R')

                if n1.getColor('L') == 0 and n1.getColor('R') == 0:
                    n1.setColor(1)
                    x = x.getParent('P')
                else:
                    if n1.right.getColor() == 0:
                        n1.left.setColor(0)
                        n1.setColor(1)
                        self._rotateRight(n1)
                        n1 = x.getParent('R')

                    n1.setColorNode(x.getParent('P'))
                    x.setColorBranch('P',0)
                    n1.setColorBranch('R',0)
                    self._rotateLeft(x.getParent('P'))
                    x = self._root
            else:
                n1 = x.parent.left
                if n1.getColor() == 1:
                    n1.setColor(0)
                    x.parent.setColor(1)
                    self._rotateRight(x.parent)
                    n1 = x.getParent('L')

                if n1.getColor('R') == 0: 
                    n1.setColor(1)
                    x = x.getParent('P')
                else:
                    if n1.getColor('L') == 0:
                        n1.right.setColor(0)
                        n1.setColor(1)
                        self._rotateLeft(n1)
                        n1 = x.getParent('L')

                    n1.setColorNode(x.parent)
                    x.setColorBranch('P',0)
                    n1.left.setColor(0)
                    self._rotateRight(x.getParent('P'))
                    x = self._root

    # Job: swap nodes for deletion, helper function  
    def _swap(self, x, y):
        if x.parent == None:
            self._root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
            if y != None:
                y.parent = x.parent 

    # Job: recursively find MIN of subtree & return it 
    def _findMin(self,node):
        if node.checkLeft() == True:
            return self._findMin(node.getChild('L'))
        return node

    # Job: recursively find Max of subtree & return it 
    def _findMax(self, node):
        if node.checkRight() == True:
            return self._findMax(node.getChild('R'))
        return node

    # Job find successor and return it     
    def successor(self, current):
        if current.checkRight() != False: 
            return self._findMin(current.right)
        self._successor(current, current.getParent('P'))

    # Job find successor and return it     
    def _successor(self, current, ancestor):
        if ancestor == None:
            return None 
        if current != ancestor.getChild('R'):
            return ancestor
        self._successor(current.getParent('P'), x)

    def _rotateLeft(self, x):
        y = x.right
        x.right = y.left
        if y.checkLeft() != False:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self._root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotateRight(self, x):
        y = x.left
        x.left = y.right
        if y.checkRight() != False:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self._root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # Job: Preorder recursive print with format for item 
    def _preorder(self, node, format):
        if node != None:
            node._item.printStudent(format)
            self._preorder(node.left, format)
            self._preorder(node.right, format)

    # Job: Inorder recursive print with format for item 
    def _inorder(self, node, format):
        if node != None:
            self._inorder(node.left, format)
            node._item.printStudent(format)
            self._inorder(node.right, format)

    # Job: Postorder recursive print with format for item 
    def _postorder(self, node, format):
        if node != None:
            self._postorder(node.left, format)
            self._postorder(node.right, format)
            node._item.printStudent(format)

    # Job: print entire tree
    # Arg: order to print, format/fields to print 
    # Ret: F if empty, exception invalid format, else T
    def printTree(self, order, format):
        if self._root == None:
            return False
        if order == 0:
            self._preorder(self._root, format)
        elif order == 1:
            self._inorder(self._root, format)
        elif order == 2:
            self._postorder(self._root, format)
        else: raise Exception("Invalid Print Order")
        return True

    def studentWork(self, key, job):
        workNode = self.search(key) 
        



'''if __name__ == "__main__":

    from structures import Course, Student
    from input import demoList, exList, thesList, courseNames, studentNames
    
    bst = RedBlackTree()
    SIZE = 6
    students = []
    for x in range(SIZE):
        students.append(Student(studentNames[x]))
        for y in range(SIZE):
            course = Course(courseNames[y], demoList[y], exList[y], thesList[y])
            students[x].addCourse(course)

    for x in range(SIZE):
        bst.insert(students[x])
    for x in range(SIZE):
        bst.insert(students[x])
    for x in range(SIZE):
        bst.insert(students[x])


    order = 1
    fields =  0
    #bst.printTree(order, fields)

    print("\nAfter deleting an element")
    bst.deleteNode("Jai Walker")
    bst.deleteNode("Jai Walker")
    bst.deleteNode("Warren Peace")
    bst.deleteNode("Warren Peace")

    bst.printTree(order,fields) '''
