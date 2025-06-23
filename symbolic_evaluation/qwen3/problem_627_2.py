import mpmath as mp
mp.dps = 15  # Set decimal precision

# Calculate π/4
term1 = mp.pi / 4

# Calculate (ln 2)/2
term2 = mp.log(2) / 2

# Sum the two components
result = term1 + term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))