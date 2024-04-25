#Samuel Rodriguez
#04/15/24
#P3HW1
#Using elif statements

grade1 = float(input("Enter grade for Module 1:" ))
grade2 = float(input("Enter grade for Module 2:" ))
grade3 = float(input("Enter grade for Module 3:" ))
grade4 = float(input("Enter grade for Module 4:" ))
grade5 = float(input("Enter grade for Module 5:" ))
grade6 = float(input("Enter grade for Module 6:" ))
print("--------Results---------")
grades_list=[]
grades_list.append(grade1)
grades_list.append(grade2)
grades_list.append(grade3)
grades_list.append(grade4)
grades_list.append(grade5)
grades_list.append(grade6)
print(grades_list)
LowestGrade=min(grades_list)
HighestGrade=max(grades_list)
SumofGrades=sum(grades_list)
Average=SumofGrades/len(grades_list)
print(f"Lowest Grade: {LowestGrade:.2f}")
print(f"Highest Grade: {HighestGrade:.2f}")
print(f"Sum of Grades: {SumofGrades:.2f}")
print(f"Average: {Average:.2f}")
if Average >= 90:
    Letter_Grade=("A")
elif Average >= 80:
    Letter_Grade=("B")
elif Average >= 70:
    Letter_Grade=("C")
elif Average >= 60:
    Letter_Grade=("D")
elif Average <= 59:
    Letter_Grade=("F")

print(f"Your grade is: {Letter_Grade}")
