#Samuel Rodriguez
#04/22/24
#P5HW
#Using user defined functions
import random

def menu():
    print("Welcome to Math Quiz")
    print()
    print("MAIN MENU")
    print("----------------")
    print("1. Adding Random Numbers")
    print("2.Subtracting Random Numbers")
    print("3.Exit")
    print()
def add_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    print(f"{num1}")
    print(f"+ {num2}")
    CorrectAnswer = num1 + num2
    answer = int(input(f"Enter Answer."))
    guesses = 1
    while answer != CorrectAnswer:
        guesses += 1
        if answer > CorrectAnswer:
            print("Sorry, guess is too high")
        if answer < CorrectAnswer:
            print("Sorry, guess is too low")
        answer = int(input(f"Enter Answer."))
    print("Congratulations!!!! Your answer is correct.")
    print(f"Number of Guesses {guesses}")

def subtract_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    print(f"{num1}")
    print(f"- {num2}")
    CorrectAnswer = num1 - num2
    answer = int(input(f"Enter Answer."))
    guesses = 1
    while answer != CorrectAnswer:
        guesses += 1
        if answer > CorrectAnswer:
            print("Sorry, guess is too high")
        if answer < CorrectAnswer:
            print("Sorry, guess is too low")
        answer = int(input(f"Enter Answer."))
    print("Congratulations!!!! Your answer is correct.")
    print(f"Number of Guesses {guesses}")
    
def main():
    menu()
    Options=int(input(f"Please choose one of the menu options:"))
    while Options !=3:
        if Options ==1:
            print("Add")
            add_numbers()
        if Options ==2:
            print("subtract")
            subtract_numbers()
        Options=int(input(f"Please choose one of the menu options:"))
    print("Program is ending")
#Call the main function
main()
