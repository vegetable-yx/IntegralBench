import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 4 * sqrt(3)
sqrt_term = mp.sqrt(3)
term1 = 4 * sqrt_term

# Calculate (2 * pi) / 3
pi_term = mp.pi
term2 = (2 * pi_term) / 3

# Sum the two terms for final result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))