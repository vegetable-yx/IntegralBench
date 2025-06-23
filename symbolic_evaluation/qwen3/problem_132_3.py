import mpmath as mp
mp.dps = 15

# Calculate each term in the series using exact denominators
term1 = mp.mpf(1)/3
term2 = mp.mpf(1)/60
term3 = mp.mpf(1)/3360
term4 = mp.mpf(1)/362880

# Sum all terms in the series
result = term1 + term2 + term3 + term4

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))