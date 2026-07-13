# Example 2: Product Cost Calculator
# Demonstrates input(), type conversion, arithmetic operators, and formatted

product_name = "cookies"
quantity = "5"
unit_price = "25"
total_cost = quantity * unit_price # arithmetic operator: multiplication
print("\n--- Receipt ---")
print(f"Product: {product_name}")
print(f"Quantity: {quantity}")
print(f"Unit Price: ₱{unit_price:.2f}")
print(f"Total Cost: ₱{total_cost:.2f}")