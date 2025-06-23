import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate gamma(1/4)
gamma_val = mp.gamma(0.25)

# Square the gamma value
gamma_sq = gamma_val**2

# Calculate cosine of 2 radians
cos2 = mp.cos(2)

# Multiply gamma squared by cos(2)
numerator = gamma_sq * cos2

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Divide numerator by denominator
result = numerator / sqrt_pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))