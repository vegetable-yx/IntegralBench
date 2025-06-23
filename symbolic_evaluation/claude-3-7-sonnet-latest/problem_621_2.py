import mpmath as mp

# Set the internal decimal precision to 15 to ensure accuracy
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide pi squared by 6
pi_sq_over_6 = pi_squared / 6

# Apply the negative sign to get the final result
result = -pi_sq_over_6

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))