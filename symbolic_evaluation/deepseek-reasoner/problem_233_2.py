import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate 2^(5/4)
term1 = mp.power(2, 5/4)

# Calculate square root of pi
term2 = mp.sqrt(mp.pi)

# Calculate Gamma(3/4) and square it
gamma_val = mp.gamma(3/4)
term3 = gamma_val ** 2

# Combine all terms
result = term1 * term2 * term3

# Print result to 10 decimal places
print(mp.nstr(result, n=10))