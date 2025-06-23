import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate sqrt(5)
sqrt5 = mp.sqrt(5)

# Compute the argument inside the logarithm: 2 + sqrt(5)
log_argument = 2 + sqrt5

# Calculate natural logarithm of (2 + sqrt(5))
log_term = mp.log(log_argument)

# Multiply by pi/4 to get the final result
result = (mp.pi / 4) * log_term

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))