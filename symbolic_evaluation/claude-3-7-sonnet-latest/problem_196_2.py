import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# First term: π²/24
term1 = pi_sq / 24

# Second term: (π * ln(2))/8
term2 = (mp.pi * ln2) / 8

# Third term: (ln²(2))/8
term3 = (ln2 ** 2) / 8

# Combine terms: term1 - term2 + term3
result = term1 - term2 + term3

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))