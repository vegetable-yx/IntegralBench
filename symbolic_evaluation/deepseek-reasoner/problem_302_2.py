import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate first term: (π/2) * arcsin(1/4)
arcsin_val = mp.asin(mp.mpf(1)/4)
term1 = (mp.pi / 2) * arcsin_val

# Calculate dilogarithm components
li2_1 = mp.polylog(2, mp.mpf(1)/4)   # Li₂(1/4)
li2_2 = mp.polylog(2, mp.mpf(-1)/4)  # Li₂(-1/4)

# Calculate second term: (Li₂(1/4) - Li₂(-1/4)) / 8
term2 = (li2_1 - li2_2) / 8

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))