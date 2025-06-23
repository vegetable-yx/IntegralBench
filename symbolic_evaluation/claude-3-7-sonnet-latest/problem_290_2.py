import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 4
pi_sq_over_4 = pi_squared / 4

# Subtract 1
result = pi_sq_over_4 - 1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))