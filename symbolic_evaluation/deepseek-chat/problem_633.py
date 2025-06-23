import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi squared
pi_sq = mp.pi ** 2

# Calculate the first term: - (pi^2 / 24) * ln(2)
term1 = - (pi_sq / 24) * mp.log(2)

# Compute zeta(3)
zeta3 = mp.zeta(3)

# Calculate the second term: - (7/16) * zeta(3)
term2 = - (7 / 16) * zeta3

# Sum the terms to get the final result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))