import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π² and reuse for multiple terms
pi_sq = mp.pi ** 2

# First term: π^4 / 1152
pi_fourth = pi_sq ** 2
term1 = pi_fourth / 1152

# Second term: -(π² * ln2) / 48
ln2 = mp.log(2)
term2 = -(pi_sq * ln2) / 48

# Third term: 1/144
term3 = mp.mpf(1)/144

# Combine all terms
result = term1 + term2 + term3

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))