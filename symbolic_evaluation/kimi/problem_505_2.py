import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute π using mpmath constant
pi_val = mp.pi

# Calculate the analytical expression π/4
result = pi_val / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))