#Samuel Rodriguez
#04/09/24
#P2HW1
#Build on P1HW2 Assignment. The only change that will be done is how the results are displayed.

print("This program calculates and displays travel expenses")
Budget = int(input("Enter Budget: "))
Travel = input("Enter your travel destination: ")
Fuel = int(input("How much do you think you will spend on gas?: "))
Accomodation = int(input("Approximately, how much will you need for accomodation/hotel?: "))
Food = int(input("Last, how much do you need for food?: "))
print("----------Travel Expenses----------")
print("Location: ", Travel)
print(f"Initial Budget: ${Budget:.2f}")
print(f"Fuel:  ${Fuel:.2f}")
print(f"Accomodation: ${Accomodation:.2f}")
print(f"Food:  ${Food:.2f}")

RemainingBalance = Budget-Fuel-Accomodation-Food
print(f"Remaining Balance:  ${RemainingBalance:.2f}")
