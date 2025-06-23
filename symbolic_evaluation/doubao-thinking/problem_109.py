import mpmath as mp
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Compute the logarithmic term's argument: 2 + sqrt(3)
log_argument = 2 + sqrt3

# Calculate natural logarithm of the argument
log_term = mp.log(log_argument)

# Multiply components: π * sqrt2 * log_term
pi_component = mp.pi * sqrt2
product = pi_component * log_term

# Divide by 4 to get final result
result = product / 4

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))