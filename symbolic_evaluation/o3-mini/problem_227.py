import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate ln(2)
ln2 = mp.log(2)

# Calculate polylog(2, 1/2)
Li2_half = mp.polylog(2, 0.5)

# Calculate polylog(3, 1/2)
Li3_half = mp.polylog(3, 0.5)

# First term: -π * (ln2)^3 / 48
term1 = - (mp.pi * ln2**3) / 48

# Second term: - (ln2 * Li2_half) / 16
term2 = - (ln2 * Li2_half) / 16

# Third term: 9 * Li3_half / 32
term3 = 9 * Li3_half / 32

# Sum all terms
result = term1 + term2 + term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))