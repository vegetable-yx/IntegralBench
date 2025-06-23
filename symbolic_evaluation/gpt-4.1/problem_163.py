import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate each term separately for clarity

# Term 1: 8 * Li_3(e^{0.5})
term1 = 8 * mp.polylog(3, mp.exp(0.5))

# Term 2: 8 * Li_3(e^{-0.5})
term2 = 8 * mp.polylog(3, mp.exp(-0.5))

# Term 3: Li_3(e^{0.25})
term3 = mp.polylog(3, mp.exp(0.25))

# Term 4: Li_3(e^{-0.25})
term4 = mp.polylog(3, mp.exp(-0.25))

# Combine terms: term1 - term2 - term3 + term4
result = term1 - term2 - term3 + term4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))