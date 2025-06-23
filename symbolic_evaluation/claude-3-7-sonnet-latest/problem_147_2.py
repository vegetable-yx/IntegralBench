import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the gamma function at 1/4
gamma_val = mp.gamma(1/4)

# Square the gamma value
gamma_sq = gamma_val**2

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Multiply gamma squared by sqrt(pi)
product = gamma_sq * sqrt_pi

# Divide by 2 to get the final result
result = product / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))