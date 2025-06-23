import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate each term separately
# Term 1: -π²/48
term1 = - (mp.pi ** 2) / 48

# Term 2: (ln(2))² / 16
log2 = mp.log(2)
term2 = (log2 ** 2) / 16

# Term 3: 3/8
term3 = mp.mpf(3) / 8

# Term 4: -3 * ln(3) / 32
log3 = mp.log(3)
term4 = -3 * log3 / 32

# Combine all terms
result = term1 + term2 + term3 + term4

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))