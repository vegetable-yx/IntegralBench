import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π²
pi_squared = mp.pi**2

# Divide π² by 6
pi_sq_over_6 = pi_squared / 6

# Calculate natural logarithm of 3
ln_3 = mp.log(3)

# Compute the final result: -(π²/6) * ln(3)
result = -pi_sq_over_6 * ln_3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))