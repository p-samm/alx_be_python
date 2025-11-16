# finance_calculator.py
# This script calculates monthly savings and projected annual savings with 5% interest.

# Ask user for inputs
monthly_income = int(input("Enter your monthly income: "))  # e.g., 5000
monthly_expenses = int(input("Enter your total monthly expenses: "))  # e.g., 4000

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected annual savings with 5% interest
projected_annual_savings = monthly_savings * 12 * 1.05  # 5% interest added

# Print results
print(f"Your monthly savings are: ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings}")
