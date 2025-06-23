import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate k = 1 / sqrt(2)
k = 1 / mp.sqrt(2)

# Compute the complete elliptic integral of the first kind: K(k)
K_value = mp.ellipk(k)

# Square the elliptic integral value
K_sq = K_value**2

# Compute the constant factor: (π * √2) / 2
constant_factor = (mp.pi * mp.sqrt(2)) / 2

# Multiply the constant factor by the squared elliptic integral
result = constant_factor * K_sq

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))