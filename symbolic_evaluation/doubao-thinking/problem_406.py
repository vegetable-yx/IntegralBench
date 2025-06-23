import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the argument for the arcsin function
sqrt3 = mp.sqrt(3)  # Compute square root of 3
numerator = sqrt3 - 1  # Compute numerator: sqrt(3) - 1
argument = numerator / 2  # Divide by 2 to get the argument

# Compute the arcsin of the argument and multiply by 2
arcsin_value = mp.asin(argument)  # Calculate inverse sine
result = 2 * arcsin_value  # Multiply by 2 for final result

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))