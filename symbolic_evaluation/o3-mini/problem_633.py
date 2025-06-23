import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate zeta(3) - Apéry's constant
zeta3 = mp.zeta(3)

# Calculate the first term: (7 * zeta(3)) / 16
term1 = (7 * zeta3) / 16

# Calculate pi squared
pi_sq = mp.pi**2

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Calculate the second term: (pi_sq * ln2) / 8
term2 = (pi_sq * ln2) / 8

# Combine terms: term1 minus term2
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))