import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi**2

# Divide by 16
pi_sq_over_16 = pi_squared / 16

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute (1 + sqrt(2))
one_plus_sqrt2 = 1 + sqrt2

# Multiply the two parts: (pi^2/16) * (1 + sqrt(2))
result = pi_sq_over_16 * one_plus_sqrt2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))