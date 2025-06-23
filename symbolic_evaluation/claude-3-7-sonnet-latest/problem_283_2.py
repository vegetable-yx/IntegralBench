import mpmath as mp

# Set internal decimal precision to 15 digits for accurate computation
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Divide pi squared by 8 to get the first term
term1 = pi_sq / 8

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the argument for the logarithm: 2 + sqrt(5)
log_arg = 2 + sqrt5

# Calculate the natural logarithm of the argument
log_val = mp.log(log_arg)

# Multiply the first term by the logarithm to get the final result
result = term1 * log_val

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))