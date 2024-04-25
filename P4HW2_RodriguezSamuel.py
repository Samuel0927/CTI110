#Samuel Rodriguez
#04/19/24
#P4HW2
#Using while loops and an incrementer 

TotalEmployees=0
TotalOvertime=0
TotalHours=0
TotalGross=0
name= "doe"
while name != "Done":
    name=input("Enter employee's name or \"Done\" to termate: ")
    if name == "Done":
        break
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
    TotalEmployees += 1
    TotalOvertime += otpay
    TotalHours += pay
    TotalGross += pay+otpay
    print(f"Employee name: {name}")
    print(f"{'Hours Worked':<24}{'Pay Rate':<24}{'OverTime':<24}{'OverTime Pay':<24}{'RegHour Pay':<24}{'Gross Pay':<24}")
    print("----------------------------------------------------------------------------------------------------------------------------------")
    print(f"{hours:<24}{payrate:<24}{overtimehours:<24}${otpay:<24.2f}${pay:<24.2f}${otpay+pay:<24.2f}")

print(f"Total number of employees entered: {TotalEmployees:.2f}")
print(f"Total amount paid for overtime: {TotalOvertime:.2f}")
print(f"Total amount paid for regular hours: {TotalHours:.2f}")
print(f"Total amount paid in gross: {TotalGross:.2f}")
