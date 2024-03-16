import random

# Generate a random amount between 0.00000100 and 0.00000115, rounded to 8 decimal places
amount = round(random.uniform(0.00000100, 0.00000115), 8)

# Print the generated amount
print(amount)
