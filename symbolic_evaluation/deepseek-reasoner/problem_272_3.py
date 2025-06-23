import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Compute square root of 2
sqrt2 = mp.sqrt(2)

# Calculate the argument for the natural logarithm
log_arg = (sqrt2 + 1) / 2

# Compute the natural logarithm term
log_term = mp.log(log_arg)

# Calculate the expression inside the parentheses
parentheses_term = sqrt2 - 1 - log_term

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * parentheses_term

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))