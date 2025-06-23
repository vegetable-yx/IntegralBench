import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sqrt(2) using mpmath
sqrt_2 = mp.sqrt(2)

# Compute the argument for the logarithm
log_argument = 1 + sqrt_2

# Calculate natural logarithm of (1 + sqrt(2))
log_term = mp.log(log_argument)

# Cube the logarithmic term
log_cubed = log_term ** 3

# Final result by dividing the cubed term by 3
result = log_cubed / 3

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))