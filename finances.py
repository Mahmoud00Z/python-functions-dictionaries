def salaryDetails() :
    salary = float(input("Plese enter your salary for this month:  "))
    month = input("Please enter the name of this month: ")
    return salary, month

def expensesDetails() :
    savingsP = float(input("Please enter savings percentage : "))
    rentP = float(input("Please enter rent percentage : "))
    electricityP = float(input("Please enter electricity percentage : "))
    return savingsP, rentP, electricityP

def calculateExpenses(salary, savingsP, rentP, electricityP) :
    savings = (salary * savingsP) / 100
    rent = (salary * rentP) / 100
    electricity = (salary * electricityP) / 100
    remaining = salary - savings - rent - electricity
    return savings, rent, electricity, remaining

def results(salary, month, expenses) :
    print("Salary for the month of ", month, " is ", salary)
    print("Savings for the month of ", month, " is ", expenses[0])
    print("Rent for the month of ", month, " is ", expenses[1])
    print("Electricity for the month of ", month, " is ", expenses[2])
    print("Remaining amount for the month of ", month, " is ", expenses[3])
    yearlyRent = expenses[1] * 12
    yearlyElecticity = expenses[2] * 12
    salarySquared = salary * salary
    extra = 50
    if expenses[0] > 0:
        extraSavRatio = extra / expenses[0]
    else:
        extraSavRatio = 0
    print("Yearly rent is ", yearlyRent)
    print("Yearly electricity is ", yearlyElecticity)
    print("Square of salary is ", salarySquared)
    print(f"If $50 extra is divided by savings, the ratio is: {extraSavRatio}")
