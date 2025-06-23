import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate cosh(1) - 1
cosh_value = mp.cosh(1)
cosh_term = cosh_value - 1

# Multiply by 2*sqrt(2) to get the final result
result = 2 * mp.sqrt(2) * cosh_term

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))