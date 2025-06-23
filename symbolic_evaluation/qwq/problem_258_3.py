import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute the term 24 * sqrt(pi)
term_24sqrtpi = 24 * sqrt_pi

# Sum the constants 40 and 24*sqrt(pi)
sum_terms = 40 + term_24sqrtpi

# Calculate the exponential term e^(-1/4)
exp_term = mp.exp(-0.25)

# Multiply the sum by the exponential term to get the final result
result = sum_terms * exp_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))