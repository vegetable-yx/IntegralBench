import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate exponential term with exponent -1/4
exp_term = mp.exp(-0.25)

# Combine components with coefficient 12
result = 12 * sqrt_pi * exp_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))