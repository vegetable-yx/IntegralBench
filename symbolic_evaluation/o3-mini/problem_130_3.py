import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2π
sqrt_2pi = mp.sqrt(2 * mp.pi)

# Calculate the hyperbolic sine of 1
sinh_1 = mp.sinh(1)

# Multiply the components to get the final result
result = sqrt_2pi * sinh_1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))