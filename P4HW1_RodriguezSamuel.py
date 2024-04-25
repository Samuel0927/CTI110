#Samuel Rodriguez
#04/19/24
#P4HW1
#Using Loops in General

grades_list=[]
grades = int(input("How many grades will you enter?: "))
for score in range(grades):
    grade1 = float(input("Enter grade: "))
    while grade1 < 0 or grade1 > 100:
        print("Grade must be between 0 and 100")
        grade1 = int(input("Enter grade: "))
    grades_list.append(grade1)

print (grades_list)
LowestGrade=min(grades_list)
print("--------Results---------")
grades_list.remove(LowestGrade)
print(f"Lowest Grade: {LowestGrade:.2f}")
print(f"Modified List: {grades_list:}")
SumofGrades=sum(grades_list)
Average=SumofGrades/len(grades_list)
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
print(f"Scores Average: {Average:.2f}")
print(f"Average: {Letter_Grade}")
print("------------------------")
