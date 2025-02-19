import json

monthlyReport = {}

def salaryDetails() :
    salary = float(input("Plese enter your salary for this month:  "))
    month = input("Please enter the name of this month: ")
    savingsP = float(input("Please enter savings percentage : "))
    rentP = float(input("Please enter rent percentage : "))
    electricityP = float(input("Please enter electricity percentage : "))
    return salary, month, savingsP, rentP, electricityP


def calculateExpenses(salary, savingsP, rentP, electricityP) :
    savings = (salary * savingsP) / 100
    rent = (salary * rentP) / 100
    electricity = (salary * electricityP) / 100
    remaining = salary - savings - rent - electricity
    return savings, rent, electricity, remaining

def storeResults(month, salary, expenses) :
    monthlyReport[month] = {"salary": salary,
     "savings": expenses[0],
     "rent": expenses[1], 
     "electricity": expenses[2], 
     "remaining": expenses[3], 
     "yearly rent": expenses[1] * 12,
     "yearly electricity": expenses[2] * 12,
     "salary squared": salary * salary}
     

print("\tWelcome to the finances program")

while True:
    salary, month, savingsP, rentP, electricityP = salaryDetails()
    expenses = calculateExpenses(salary, savingsP, rentP, electricityP)
    storeResults(month, salary, expenses)
    repeat = input("Do you want to enter another month? (yes/no): ").lower()
    if repeat == "no":
        break

print(json.dumps(monthlyReport, indent=4))
print("\tThank you for using the finances program")
