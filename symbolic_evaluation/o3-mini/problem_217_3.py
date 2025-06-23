import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Gamma function at 1/4
gamma_val = mp.gamma(1/4)

# Square the Gamma value
gamma_squared = gamma_val ** 2

# Compute cosine of 2 radians
cos2 = mp.cos(2)

# Multiply squared Gamma by cos(2)
numerator = gamma_squared * cos2

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Divide numerator by sqrt(pi)
result = numerator / sqrt_pi

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))