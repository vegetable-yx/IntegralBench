import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise gamma(1/4) to the 4th power
gamma_fourth = gamma_val**4

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute the denominator: 4 * sqrt(pi)
denominator = 4 * sqrt_pi

# Divide the numerator by the denominator
result = gamma_fourth / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))