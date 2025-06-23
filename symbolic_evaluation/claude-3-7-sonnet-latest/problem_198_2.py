import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate the constant factor: 2 * sqrt(2)
factor = 2 * mp.sqrt(2)

# Compute sine of 1 radian
sine_val = mp.sin(1)

# Multiply factor by sine_val to get the final result
result = factor * sine_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))