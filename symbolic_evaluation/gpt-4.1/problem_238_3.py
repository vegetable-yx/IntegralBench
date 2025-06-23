import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Assign the constant value 8 to the result variable
result = 8

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))