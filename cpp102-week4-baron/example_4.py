# Example 4: Daily Allowance Calculator
# Demonstrates arithmetic operators, comparison operators, and Boolean output

daily_allowance = "150"
transportation_expense = "50"
food_expense = "60"

total_expenses = transportation_expense + food_expense # arithmetic: +
remaining_allowance = daily_allowance - total_expenses # arithmetic: -
is_within_allowance = total_expenses <= daily_allowance # comparison ->
bool

print("\n--- Daily Allowance Summary ---")
print(f"Daily Allowance: ₱{daily_allowance:.2f}")
print(f"Total Expenses: ₱{total_expenses:.2f}")
print(f"Remaining Allowance: ₱{remaining_allowance:.2f}")
print(f"Within Allowance: {is_within_allowance}")