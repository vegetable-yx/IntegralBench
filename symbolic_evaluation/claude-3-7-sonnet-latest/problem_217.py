import mpmath as mp

# Set internal decimal places for sufficient precision
mp.dps = 15

# Compute the square root of (2 * pi)
sqrt_2pi = mp.sqrt(2 * mp.pi)

# Compute the cosine of 1 radian
cos_1 = mp.cos(1)

# Multiply the two components to get the final result
result = sqrt_2pi * cos_1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))