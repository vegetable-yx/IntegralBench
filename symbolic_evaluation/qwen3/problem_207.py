import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate 1 + sqrt(2)
sqrt_2 = mp.sqrt(2)
log_argument = 1 + sqrt_2

# Calculate natural logarithm of (1 + sqrt(2))
ln_term = mp.log(log_argument)

# Combine terms to get final result
result = (sqrt_pi * ln_term) / 2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))