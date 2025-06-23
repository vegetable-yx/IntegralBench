import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute pi squared
pi_sq = mp.pi**2

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Calculate the first term: - (pi^2 / 8) * ln(2)
term1 = - (pi_sq / 8) * ln2

# Compute zeta(3) - Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Calculate the second term: - (7/16) * zeta(3)
term2 = - (7/16) * zeta3

# Sum both terms to get the final result
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))