import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the exponential term: e^{-1/4}
exp_term = mp.exp(-0.25)

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Combine terms: 2 * sqrt(pi) * e^{-1/4}
result = 2 * sqrt_pi * exp_term

# Print result with 10 decimal places
print(mp.nstr(result, n=10))