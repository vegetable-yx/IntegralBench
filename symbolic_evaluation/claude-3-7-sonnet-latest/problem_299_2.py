import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate the value: -pi/2
pi_value = mp.pi  # Get the constant pi
result = -pi_value / 2  # Compute the expression

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))