import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Square the gamma value
gamma_sq = gamma_val**2

# Calculate the denominator: 2 * sqrt(2 * pi)
# First, compute 2 * pi
two_pi = 2 * mp.pi
# Compute sqrt(2 * pi)
sqrt_two_pi = mp.sqrt(two_pi)
# Multiply by 2
denominator = 2 * sqrt_two_pi

# Compute the final result: gamma_sq / denominator
result = gamma_sq / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))