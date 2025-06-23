import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by 3
numerator_part = 3 * sqrt2

# Subtract 4 from the intermediate result
numerator = numerator_part - 4

# Divide by 12 to get the final result
result = numerator / 12

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))