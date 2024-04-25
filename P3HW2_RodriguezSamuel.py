#Samuel Rodriguez
#04/15/24
#P3HW2
#Using if else statements

name=input("Enter employee's name: ")
hours=int(input("Enter number of hours worked: "))
payrate=float(input("Enter employee's pay rate: "))

if hours > 40:
    reghours= 40
    overtimehours= hours-40

else:
    overtimehours= 0
    reghours= hours

pay=reghours*payrate
otpay=payrate*1.5*overtimehours
print(f"Employee name: {name}")
print(f"{'Hours Worked':<24}{'Pay Rate':<24}{'OverTime':<24}{'OverTime Pay':<24}{'RegHour Pay':<24}{'Gross Pay':<24}")
print("----------------------------------------------------------------------------------------------------------------------------------")
print(f"{hours:<24}{payrate:<24}{overtimehours:<24}${otpay:<24.2f}${pay:<24.2f}${otpay+pay:<24.2f}")
