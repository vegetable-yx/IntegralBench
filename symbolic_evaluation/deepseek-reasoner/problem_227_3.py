import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate sqrt(2) using mpmath's square root function
sqrt_2 = mp.sqrt(2)

# Compute 1 + sqrt(2)
log_argument = 1 + sqrt_2

# Calculate natural logarithm of (1 + sqrt(2))
log_value = mp.log(log_argument)

# Raise the logarithm result to the 4th power
log_power = log_value**4

# Divide by 4 to get the final result
result = log_power / 4

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))