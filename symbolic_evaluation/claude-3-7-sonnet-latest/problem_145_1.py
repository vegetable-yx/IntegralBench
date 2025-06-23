import mpmath as mp

# Set internal decimal precision to 15 for reliable calculations
mp.dps = 15

# Compute the constant pi
pi_value = mp.pi

# Calculate the expression: pi/4
result = pi_value / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))