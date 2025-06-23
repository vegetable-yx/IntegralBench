import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute the exponential term: e^(-1/4)
exp_term = mp.exp(-0.25)

# Combine the components: 12 * sqrt(pi) * e^(-1/4)
result = 12 * sqrt_pi * exp_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))