import mpmath as mp
mp.dps = 15

# Compute each term in the series
term1 = (4 * mp.sqrt(2)) / 3
term2 = (4 * mp.sqrt(2)) / 15
term3 = mp.sqrt(2) / 70

# Sum all terms
result = term1 + term2 + term3

print(mp.nstr(result, n=10))