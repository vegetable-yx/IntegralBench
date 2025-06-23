import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the constant pi
pi_value = mp.pi

# Compute the result: pi divided by 8
result = pi_value / 8

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))