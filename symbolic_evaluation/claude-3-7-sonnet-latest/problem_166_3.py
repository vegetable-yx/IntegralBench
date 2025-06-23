import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Get the mathematical constant pi
pi_val = mp.pi

# Compute the expression: π divided by 4
result = pi_val / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))