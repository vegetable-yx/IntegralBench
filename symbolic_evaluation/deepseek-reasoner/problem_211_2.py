import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Bessel function of the first kind J0 at 1
j0_value = mp.besselj(0, 1)

# Square the Bessel function result
j0_squared = j0_value ** 2

# Multiply by π/2 to get final result
result = (mp.pi / 2) * j0_squared

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))