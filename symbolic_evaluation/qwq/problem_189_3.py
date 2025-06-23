import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Calculate the numerator (1 + sqrt(5))
numerator = 1 + sqrt5

# Calculate the argument for logarithm (1+√5)/2
log_argument = numerator / 2

# Compute natural logarithm of the argument
log_term = mp.log(log_argument)

# Calculate π/2
pi_half = mp.pi / 2

# Multiply π/2 with the logarithm term to get final result
result = pi_half * log_term

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))