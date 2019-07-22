#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      ufu1
#
# Created:     13/02/2017
# Copyright:   (c) ufu1 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math


class student:
    name = None #public variables
    id = None
    age = None
    major = None
    __grade1 = 0 #private variables
    __grade2 = 0
    __grade3 = 0

    def __init__(self,a,b,c,d):  #constructor __init__ that creates a customized student attributes
        self.name = a
        self.id = b
        self.age = c
        self.major = d
    def __str__(self):
        return 'The students name is '+ self.name  + ' ('+'ID:'+str(self.id)+')'   + ' '+self.major +' major in age '+str(self.age)
    def setGrades(self, x, y, z): #encapsulation that sets gardes x,y,z=grade1,grade2,grade3
        self.__grade1 = x
        self.__grade2 = y
        self.__grade3 = z

    def getGrades(self):   #encapsulation that gets gardes for one student
        return self.__grade1,self.__grade2,self.__grade3

    def __add__(self,other): #operator overloading __add__
        return self.__grade1 + other.__grade1 + self.__grade2 + other.__grade2 + self.__grade3  + other.__grade3

    def __lt__(self, other): #operatior overloading with __lt__ to compare sum of the three grades
        student1 = self.__grade1 + self.__grade2 + self.__grade3
        student2 = other.__grade1 + other.__grade2 + other.__grade3
        if student1 < student2:
            return True
        else:
            return False

    def getAva(self): # calculating avarage of three grades for one student
        return (self.__grade1+self.__grade2+self.__grade3)/3

if __name__ == '__main__':

# the code below creates instance for student1 and student2
    s1 = student('Ugo',246,28,'GIS')
    s2 = student('Francis',247,26,'Data Science')

# the code will print basic informations of s1 and s2
    print s1
    print s2

# the code below will print major of s1 and s2
    print "student 1 major is ",s1.major, ',' "student 2 major is ",s2.major

# the code below will set grades and print out grades for the two students
    s1.setGrades(99,100,98)
    s2.setGrades(50,37,44)
    print 's1 grades are:',s1.getGrades(),',', 's2 grades are:',s2.getGrades()

# the code below will add two student's grades
    print 's1+s2 =',s1+s2

# the code below will compare sum of student1 and student2 grades
    print s1<s2

# the code below will get average grades for the two students
    print 'the avaerage grades of s1 and s2 are:', s1.getAva(), 'and',s2.getAva()





