import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute the exponential term: e^(-1/4)
exp_term = mp.exp(-0.25)

# Multiply components: -7 * sqrt(pi) * exp(-1/4)
result = -7 * sqrt_pi * exp_term

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))