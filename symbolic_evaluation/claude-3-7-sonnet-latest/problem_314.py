import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Divide by 6 to get pi^2 / 6
pi_sq_over_6 = pi_sq / 6

# Compute natural logarithm of 3
ln3 = mp.log(3)

# Multiply the two parts: (pi^2 / 6) * ln(3)
product = pi_sq_over_6 * ln3

# Apply the negative sign to get the final result
result = -product

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))