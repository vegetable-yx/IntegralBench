import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sqrt(2) using mpmath's square root function
sqrt2 = mp.sqrt(2)

# Compute the argument for the logarithm
log_argument = 1 + sqrt2

# Calculate the natural logarithm of the argument
log_term = mp.log(log_argument)

# Multiply by pi constant from mpmath
result = mp.pi * log_term

# Print the result with 10 decimal places using mpmath's number string function
print(mp.nstr(result, n=10))