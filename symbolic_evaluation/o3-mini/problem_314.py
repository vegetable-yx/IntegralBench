import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the trilogarithm of 1/4 and multiply by 1/4
term1 = mp.polylog(3, 1/mp.mpf(4)) / 4

# Calculate the trilogarithm of 1/2 and multiply by 2
term2 = 2 * mp.polylog(3, 1/mp.mpf(2))

# Combine the terms: (1/4)*Li_3(1/4) - 2*Li_3(1/2)
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))