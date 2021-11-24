#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grades - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:
    name  = ""
    studentNumber = ""
    grade = ""
    courses = ""
    grades = ()


    def __init__(self, name, studentNumber, grade, courses, grades):
        self.grade = grade
        self.name = name
        self.grades = grades
        self.studentNumber = studentNumber
        self.courses = courses
        print("the student's name is " + self.name)
    

def act():
        print("press:")
        print("1 for average")
        print("2 for courses")
        print("3 for grade, then enter which course")
        print("4 for honor roll check")
        return None

print(act())
    
exit()
x = 1

if x == 1:
    def __del__():

        pass
def average(self):
        self.getGrades()

        pass
















def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( [91, 94, 87, 99, 82, 100, 73])

    st2 = student("Joe Lunchbox","12346", 11)
    st2.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st2.getGrades( [71, 98, 93, 95, 68, 81, 71])




main()