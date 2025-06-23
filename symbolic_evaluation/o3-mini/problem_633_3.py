import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi**2

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute the first term: -π² * ln(2) / 8
term1 = -pi_sq * ln2 / 8

# Compute zeta(3) - Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Compute the second term: 7 * zeta(3) / 16
term2 = 7 * zeta3 / 16

# Sum the two terms to get the final result
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))