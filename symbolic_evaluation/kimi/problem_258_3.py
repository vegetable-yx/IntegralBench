import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate each component of the expression
sqrt_pi = mp.sqrt(mp.pi)
exp_term = mp.exp(-0.25)

# Combine components to compute the final result
result = 2 * sqrt_pi * exp_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))