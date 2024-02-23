
"""
Created on Tue Jan 30 23:48:29 2024

@author: mattmeadows
"""
# Program takes in a number of students registering for an exam.

# Takes in inputted number and asks for student ID for each corresponding student

# Each Student ID number is stored into a .txt file named "reg_form.txt".

file = open('reg_form.txt', 'w')

total = input("Please enter the number students registering for this exam : " + "\n")

for i in range(int(total)):
    student_ID = input(f"Please enter the student ID number for student {i+1}: " + "\n" +  "-"*60 + "\n" )
    file.write(student_ID + "\n" + "-"*80 +"\n")
    

file.close() 

