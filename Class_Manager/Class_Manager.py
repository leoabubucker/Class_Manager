from time import sleep
import os
def get_data():

    # Student Name Input
    raw_students = input("List your students, separating their names with commas:   ")
    init_students = raw_students.split(", ")
    print("Your students are:")
    print(*init_students, sep=', ')

    # Student Homework Input

    int_homework = []
    str_homework = []
    for student in init_students:
        raw_homework= input("List " + student + "'s homework grades (Disregard % Sign), separating individual grades with commas:   ")
        str_homework.append(raw_homework.split(", "))
        split_homework = raw_homework.split(", ")
        for number in split_homework:
            number = int(number)
            int_homework.append(number)

    # Student Quiz Input

    int_quizzes = []
    str_quizzes = []
    for student in init_students:
        raw_quizzes= input("List " + student + "'s quiz grades (Disregard % Sign), separating individual grades with commas:   ")
        split_quizzes = raw_quizzes.split(", ")
        for number in split_quizzes:
            number = int(number)
            int_quizzes.append(number)
        str_quizzes.append(raw_quizzes.split(", "))

    # Student Test Input
    int_tests = []
    str_tests = []
    for student in init_students:
        raw_tests= input("List " + student + "'s test grades (Disregard % Sign), separating individual grades with commas:   ")
        split_tests = raw_tests.split(", ")
        for number in split_tests:
            number = int(number)
            int_tests.append(number)
        str_tests.append(raw_tests.split(", "))
    
    # Grade Category Weighting Input

    global homework_weight
    global quiz_weight
    global test_weight

    homework_weight = float(input("What Percentage of Your Class's Grade is Based on Homework? (Input Percentage as a Decimal):    "))
    quiz_weight = float(input("What Percentage of Your Class's Grade is Based on Quizzes? (Input Percentage as a Decimal):    "))
    test_weight = float(input("What Percentage of Your Class's Grade is Based on Tests? (Input Percentage as a Decimal):    "))
    

    # Function Calls for Outputs
    initialize_data(init_students, str_homework, str_quizzes, str_tests)
    compute_data(int_homework, int_quizzes, int_tests)
   
def initialize_data(students, homework, quizzes, tests):
    global student
    index = 0

    for student in students:
        int_homework = []
        int_quizzes = []
        int_tests = []
        letter_homework = []
        letter_quizzes = []
        letter_tests = []

        student = {
            "name": str(student),
            "homework": str(homework[index]),
            "quizzes": str(quizzes[index]),
            "tests": str(tests[index])}
        index += 1
#Name
        print("")
        print(student["name"] + ":")
#Homework
        #Removes Brackets and Single Quotes From Homework Grade List
        init_homework_str = str(student["homework"]) [1: -1]
        homework_str = init_homework_str.replace("'", "")

        #Converts Homework Grade Strings to Ints and Calls the Average Function.
        split_homework = homework_str.split(", ")
        for number in split_homework:
            number = int(number)
            int_homework.append(number)
        homework_avg = average_data(int_homework)
        
        #Prints the Formatted Homework Grade List and the Returned Homework Averages
        print("Homework Grade Percentages: " + homework_str + " (Average: " + str(homework_avg) + "%)")

        #Calls the Converter Function to Convert Homework Grade Percenetages to Letter Grades
        for grade in int_homework:
            letter_homework.append(letter_grade_converter(grade))
        
        #Removes Brackets and Single Quotes From Letter Grade List
        init_letter_homework_str = str(letter_homework)[1: -1]
        letter_homework_str = init_letter_homework_str.replace("'", "")

        #Calls the Converter Function to Convert The Average Homework Grade Percentage to a Letter Grade
        letter_homework_avg = letter_grade_converter(homework_avg)

        #Prints the Formatted Homework Letter Grade List and the Returned Homework Average Letter Grade
        print("Homework Letter Grades: " + letter_homework_str + " (Average: " + letter_homework_avg + ")")

#Quizzes
        #Removes Brackets and Single Quotes From Quiz Grade List
        init_quiz_str = str(student["quizzes"]) [1: -1]
        quiz_str = init_quiz_str.replace("'", "")

        #Converts Quiz Grade Strings to Ints and Calls the Average Function.
        split_quizzes = quiz_str.split(", ") 
        for number in split_quizzes:
            number = int(number)
            int_quizzes.append(number)
        quizzes_avg = average_data(int_quizzes)

        #Prints the Formatted Quiz Grade List and the Returned Quiz Averages
        print("Quiz Grades: " + quiz_str + " (Average: " + str(quizzes_avg) + "%)")

        #Calls the Converter Function to Convert Quiz Grade Percenetages to Letter Grades
        for grade in int_quizzes:
            letter_quizzes.append(letter_grade_converter(grade))
        
        #Removes Brackets and Single Quotes From Letter Grade List
        init_letter_quizzes_str = str(letter_quizzes)[1: -1]
        letter_quizzes_str = init_letter_quizzes_str.replace("'", "")

        #Calls the Converter Function to Convert The Average Homework Grade Percentage to a Letter Grade
        letter_quizzes_avg = letter_grade_converter(quizzes_avg)

        #Prints the Formatted Homework Letter Grade List and the Returned Homework Average Letter Grade
        print("Quiz Letter Grades: " + letter_quizzes_str + " (Average: " + letter_quizzes_avg + ")")

#Tests
        #Removes Brackets and Single Quotes From Test Grade List
        init_test_str = str(student["tests"])[1: -1]
        test_str = init_test_str.replace("'", "")

        #Converts Test Grade Strings to Ints and Calls the Average Function.
        split_tests = test_str.split(", ") 
        for number in split_tests:
            number = int(number)
            int_tests.append(number)
        tests_avg = average_data(int_tests)

        #Prints the Formatted Test Grade List and the Returned Test Averages
        print("Test Grades: " + test_str + " (Average: " + str(tests_avg) + "%)")

        #Calls the Converter Function to Convert Homework Grade Percenetages to Letter Grades
        for grade in int_tests:
            letter_tests.append(letter_grade_converter(grade))
        
        #Removes Brackets and Single Quotes From Letter Grade List
        init_letter_tests_str = str(letter_tests)[1: -1]
        letter_tests_str = init_letter_tests_str.replace("'", "")

        #Calls the Converter Function to Convert The Average Homework Grade Percentage to a Letter Grade
        letter_tests_avg = letter_grade_converter(tests_avg)

        #Prints the Formatted Homework Letter Grade List and the Returned Homework Average Letter Grade
        print("Test Letter Grades: " + letter_tests_str + " (Average: " + letter_tests_avg + ")")
        
 
def compute_data(homework, quizzes, tests): 
    #Calls the Average Function and Averages the Grades
    homework_avg = average_data(homework)
    quizzes_avg = average_data(quizzes)
    tests_avg = average_data(tests)

    #Calls the Converter Function and Converts the Grade Averages to Letter Grades
    letter_homework_avg = letter_grade_converter(homework_avg)
    letter_quizzes_avg = letter_grade_converter(quizzes_avg)
    letter_tests_avg = letter_grade_converter(tests_avg)
    
    #Calls the Weighted Grade Function and Calculates the Class's Overall Grade
    init_class_grade = weighted_grade(homework_avg, quizzes_avg, tests_avg)
    class_grade = format(init_class_grade, '.2f')
    converted_homework_weight = int(homework_weight * 100)
    converted_quiz_weight = int(quiz_weight * 100)
    converted_test_weight = int(test_weight * 100)


    letter_class_grade = letter_grade_converter(init_class_grade)
    #Prints the Class Averages

    print("")
    print("Class Averages:")  
    print("The average homework grade is " + str(homework_avg) + "% (" + letter_homework_avg + ")")    
    print("The average quiz grade is " + str(quizzes_avg) + "% (" + letter_quizzes_avg + ")")    
    print("The average test grade is " + str(tests_avg) + "% (" + letter_tests_avg + ")")
    print("The average class grade with a weighting of: Homework: " + str(converted_homework_weight) + "% , Quiz: " + str(converted_quiz_weight) + "% , and Test: " \
    + str(converted_test_weight) + "% is " + str(class_grade) + "% (" + str(letter_class_grade) + ")")
    print("")

def average_data(data):
    #Averages the Inputted Data and Returns the Average
        sum = 0
        for i in data:
            sum = sum + i
        avg = int(sum/len(data))
        return avg

def letter_grade_converter(grade):
    # Converts the Inputted Grade into a Letter Grade and Returns It
    if(grade >= 90):
        letter_grade = "A"
    elif(grade >= 80):
        letter_grade = "B"
    elif(grade >= 70):
        letter_grade = "C"
    elif(grade >=  60):
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade

def weighted_grade(homework, quizzes, tests):
    grade = (homework * homework_weight) + (quizzes * quiz_weight) + (tests * test_weight)
    return grade

def clear():
    #Clears Windows 
    if os.name == 'nt':
        _ = os.system('cls')

    #Clears Mac and Windows (os name is 'posix')
    else:
        _ = os.system('clear')
# Start of Program Function Call
get_data()           