import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate the exponential term: e^(-0.25)
exp_term = mp.exp(-0.25)

# Compute the final result: 2 * sqrt(pi) * e^(-0.25)
result = 2 * sqrt_pi * exp_term

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))