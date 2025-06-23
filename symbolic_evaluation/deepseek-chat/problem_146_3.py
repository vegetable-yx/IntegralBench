import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the modulus k = 1/sqrt(2)
k = 1 / mp.sqrt(2)

# Compute the complete elliptic integral of the first kind, K(k)
K_value = mp.ellipk(k)

# Square the elliptic integral value
K_squared = K_value**2

# Compute the constant factor: 2 * sqrt(2)
constant_factor = 2 * mp.sqrt(2)

# Multiply to get the final result
result = constant_factor * K_squared

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))