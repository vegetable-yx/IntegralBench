import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Assign the constant value 5040 to the result variable
result = 5040

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))