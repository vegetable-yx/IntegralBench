import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute the final result as π divided by 36
result = pi_value / 36

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))