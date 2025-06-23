import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate first term: (2*π)/3
term1 = mp.mpf(2) * mp.pi
term1 = term1 / 3

# Calculate second term: 4*sqrt(3)
term2 = mp.mpf(4) * mp.sqrt(3)

# Combine both terms
result = term1 + term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))