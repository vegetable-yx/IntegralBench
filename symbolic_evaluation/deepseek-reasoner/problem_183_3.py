import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute the argument for the logarithm
log_argument = 2 + sqrt5

# Calculate natural logarithm of (2 + sqrt(5))
log_term = mp.log(log_argument)

# Multiply by pi/4 to get final result
result = (mp.pi / 4) * log_term

# Print result with 10 decimal places
print(mp.nstr(result, n=10))