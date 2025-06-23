import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant factor: (3 * sqrt(3)) / 2
factor = (3 * mp.sqrt(3)) / 2

# Calculate hyperbolic sine of 3
sinh_val = mp.sinh(3)

# Compute the final result by multiplying factor and sinh_val
result = factor * sinh_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))