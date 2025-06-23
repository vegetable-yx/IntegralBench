import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt_val = mp.sqrt(2)

# Calculate the hyperbolic sine of 1
sinh_val = mp.sinh(1)

# Multiply the components: 2 * sqrt(2) * sinh(1)
result = 2 * sqrt_val * sinh_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))