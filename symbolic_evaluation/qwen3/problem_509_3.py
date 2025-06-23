import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 2π/3
term1 = mp.mpf(2) * mp.pi / mp.mpf(3)

# Calculate 4√3
term2 = mp.mpf(4) * mp.sqrt(3)

# Sum the two terms
result = term1 + term2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))