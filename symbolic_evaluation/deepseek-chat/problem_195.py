import mpmath as mp

# Set internal decimal precision to 15 digits for accurate calculations
mp.dps = 15

# Extract the constant pi
pi_value = mp.pi

# Compute the expression: 2 - (pi / 2)
result = 2 - (pi_value / 2)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))