import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute Bessel function J_1 of the first kind at sqrt(2)
j1_value = mp.besselj(1, sqrt2)

# Square the Bessel function result
j1_squared = j1_value ** 2

# Multiply by 2 to get final result
result = 2 * j1_squared

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))