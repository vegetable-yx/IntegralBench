import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the argument for the logarithm
log_arg = (1 + sqrt5) / 2

# Calculate the natural logarithm of the argument
log_term = mp.log(log_arg)

# Multiply by π/2 to get the final result
result = (mp.pi / 2) * log_term

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))