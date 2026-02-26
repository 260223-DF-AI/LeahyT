# budget_calculator.py - Personal Finance Calculator
# Starter code for e002-exercise-python-intro

"""
Personal Finance Calculator
---------------------------
This program helps users understand their monthly budget by collecting
income and expense information and displaying a formatted summary.

Complete the TODO sections below to finish the program.
"""

# prompt user with given message and keep looping until user gives an answer with the proper data type
def promptUser(message, dataType):
    promptAnswer = None
    while type(promptAnswer) != dataType:
        promptAnswer = input(message)
        try:
            promptAnswer = dataType(promptAnswer)
        except:
            print("Please enter a " + str(dataType) + ".")
    if type(promptAnswer) != str:
        if promptAnswer < 0:
            promptAnswer = 0.0
    return promptAnswer


print("=" * 44)
print("       PERSONAL FINANCE CALCULATOR")
print("=" * 44)
print()

# =============================================================================
# TODO: Task 1 - Collect User Information
# =============================================================================
# Get the user's name
# Example: name = input("Enter your name: ")
name = promptUser("Please Enter your name: ", str)
if name == "":
    name = "Anonymous"
# Get monthly income (as a float)
# Remember to convert the input to a float!
income = promptUser("Please enter your monthly income: ", float)
if income == 0:
    print("Fatal: Income must be positive.")
    exit()
# Get expenses for at least 4 categories:
# - rent: Rent/Housing
# - utilities: Utilities (electric, water, internet)
# - food: Food/Groceries
# - transportation: Transportation (gas, public transit)
rent = promptUser("Please enter your monthly rent: ", float)
utilities = promptUser("Please enter your monthly utilities: ", float)
food = promptUser("Please enter your monthly food cost: ", float)
transportation = promptUser("Please enter your monthly transportation cost: ", float)
# =============================================================================
# TODO: Task 2 - Perform Calculations
# =============================================================================
# Calculate total expenses
expenseTotal = rent + utilities + food + transportation

# Calculate remaining balance (income - expenses)
remainingBalance = (income - expenseTotal)

# Calculate savings rate as a percentage
# Formula: (balance / income) * 100
savingsRate = (remainingBalance / income) * 100

# Determine financial status
# - If balance > 0: status = "in the green"
# - If balance < 0: status = "in the red"
# - If balance == 0: status = "breaking even"
if remainingBalance > 0:
    status = "in the green"
elif remainingBalance < 0:
    status = "in the red"
else:
    status = "breaking even"

# =============================================================================
# TODO: Task 3 - Display Results
# =============================================================================
# Create a formatted budget report
# Use f-strings for formatting
# Dollar amounts should show 2 decimal places: f"${amount:.2f}"
# Percentages should show 1 decimal place: f"{rate:.1f}%"

print("=" * 44)
print("       MONTHLY BUDGET REPORT")
print("=" * 44 + "\n")

print(f"Name: {name}")
print(f"Monthly Income: ${income:.2f}"+ "\n")

print("EXPENSES:")
print(f"  - Rent/Housing:   ${rent:.2f}")

print(f"  - Utilities:      ${utilities:.2f}")

print(f"  - Food/Groceries: ${food:.2f}")
print(f"  - Transportation: ${transportation:.2f}")
print("-" * 44)
print("EXPENSE BREAKDOWN:")
print(f"  - Rent/Housing:   {(rent/income * 100):<.1f}% of income")
print(f"  - Utilities:      {(utilities/income * 100):<.1f}% of income")
print(f"  - Food/Groceries: {(food/income * 100):<.1f}% of income")
print(f"  - Transportation: {(transportation/income * 100):<.1f}% of income")
print("-" * 44)
print(f"Total Expenses:     ${expenseTotal:.2f}")
print(f"Remaining Balance:  ${remainingBalance:.2f}")
print(f"Savings Rate:       {savingsRate:.1f}%")
print(f"Status: You are {status}!")

print("=" * 44 + "\n")
# Example structure:
# print("=" * 44)
# print("       MONTHLY BUDGET REPORT")
# print("=" * 44)
# print(f"Name: {name}")
# ... continue building the report ...


# =============================================================================
# TODO: Task 4 - Add Validation (Optional Enhancement)
# =============================================================================
# Add these validations before calculations:
# - If name is empty, use "Anonymous"
# - If income is <= 0, print error and exit
# - If any expense is negative, treat as 0


# =============================================================================
# STRETCH GOAL: Category Percentages
# =============================================================================
# Add a section showing what percentage each expense is of total income
# Example: print(f"  - Rent/Housing:    {(rent/income)*100:.1f}% of income")
