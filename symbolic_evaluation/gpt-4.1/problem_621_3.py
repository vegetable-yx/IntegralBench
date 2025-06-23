import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Retrieve the constant pi
pi_val = mp.pi

# Calculate the expression: -π/2
result = -pi_val / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))