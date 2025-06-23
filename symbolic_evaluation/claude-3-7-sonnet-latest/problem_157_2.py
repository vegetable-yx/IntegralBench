import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Multiply by 3: 3 * sqrt(pi)
numerator = 3 * sqrt_pi

# Divide by 4 to get the fraction: (3 * sqrt(pi)) / 4
fraction = numerator / 4

# Compute the exponential term: e^(-1/4)
exp_term = mp.exp(-0.25)

# Multiply fraction by exponential term to get final result
result = fraction * exp_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))