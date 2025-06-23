import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate exponential of -1/4
exp_term = mp.exp(-0.25)

# Multiply by 2 and combine terms
result = 2 * sqrt_pi * exp_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))