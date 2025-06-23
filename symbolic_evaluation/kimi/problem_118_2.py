import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi**2

# Calculate the factor (sqrt(2) - 1)
sqrt2_minus_1 = mp.sqrt(2) - 1

# Compute the expression: (pi_squared / 2) * (sqrt(2) - 1)
result = (pi_squared / 2) * sqrt2_minus_1

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))