import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Extract the constant pi
pi_val = mp.pi

# Compute the expression: π/4
result = pi_val / 4

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))