import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate hyperbolic sine of 1
sinh_val = mp.sinh(1)

# Multiply by 2 and by pi
result = 2 * mp.pi * sinh_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))