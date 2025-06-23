import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Compute natural log of 2
ln2 = mp.log(2)

# Compute π (pi)
pi = mp.pi

# Compute Li_2(1/2) - dilogarithm at 1/2
li2_half = mp.polylog(2, 0.5)

# Compute Li_3(1/2) - trilogarithm at 1/2
li3_half = mp.polylog(3, 0.5)

# Compute term: (π * (ln2)^3) / 4
term1 = pi * ln2**3 / 4

# Compute term: (π * ln2 * Li_2(1/2)) / 2
term2 = pi * ln2 * li2_half / 2

# Combine terms: term1 - term2 + Li_3(1/2)
result = term1 - term2 + li3_half

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))