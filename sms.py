
import pandas as pd


print("\n\n\n\n\n")

print('School Management System')
print('Author: Samip Paudel')
print("Developed as an assignment for Grade-12")
print("To be submitted to: Lekhnath Pantha")

print("\n\n\n\n\n")

print("Available Actions:\n (1)Add a student\n (2)Enquire details about a student \n (3)Add a teacher\n (4)Enquire Detail about a Teacher\n (5)Enquire about Student Dues\n (6)Modify a student Details\n")

user_action  = input("Enter Your Action: \n")


student_details = pd.read_csv('student_details.csv')



print(student_details.columns)


if user_action == '1':
    id = input("Enter The Student ID")
    name = input("Enter The Student Name")
    std_class = input("Enter the class")
    std_sec  = input("Enter the Section")
    roll = input('Enter the roll number')
    dob = input('Enter The Date of Birth (YY-MM-DD)')
    address = input('Enter Your Address')
    contact = input('Enter Your Contact')
    email = input('Enter Your Email')
    joined = input("Enter the joining date")
    list = [id,name,std_class,std_sec,roll,dob,address,contact,email,joined]
    data = pd.Series(list,index=student_details.columns)
    student_details = student_details.append(data,ignore_index=True)
    print(student_details)
elif user_action == '2':
    enquire_student()
elif user_action =='3':
    add_teacher()
elif user_action == '4':
    enquire_teacher()
elif user_action =='5':
    enquire_dues()
elif user_action == '6':
    modify_student_details()


