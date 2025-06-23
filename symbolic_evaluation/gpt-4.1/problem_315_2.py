import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi**2

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute first term: (π²/3) * ln(2)
term1 = (pi_sq / 3) * ln2

# Compute ζ(3) - Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Compute second term: (3/2) * ζ(3)
term2 = (3/2) * zeta3

# Combine terms: first term minus second term
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))