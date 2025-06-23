import mpmath as mp

# Set internal decimal precision to 15 to ensure 10 decimal places accuracy
mp.dps = 15

# Calculate each term in the expression separately

# Term 1: π^3 / 48
term1 = mp.pi**3 / 48

# Term 2: (π * (ln 2)^2) / 2
ln2 = mp.log(2)            # Natural logarithm of 2
ln2_sq = ln2**2            # Square of ln2
term2 = (mp.pi * ln2_sq) / 2

# Term 3: -ln2 * Li_2(1/2)
li2_half = mp.polylog(2, 0.5)  # Dilogarithm at 1/2
term3 = -ln2 * li2_half

# Term 4: Li_3(1/2)
term4 = mp.polylog(3, 0.5)     # Trilogarithm at 1/2

# Sum all terms
result = term1 + term2 + term3 + term4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))