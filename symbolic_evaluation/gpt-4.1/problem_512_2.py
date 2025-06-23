import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate e^2
exp_term = mp.exp(2)

# Subtract 1 from e^2
numerator = exp_term - 1

# Divide by 4 to get the final result
result = numerator / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))