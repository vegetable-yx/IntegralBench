import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate first term: π/6
term1 = mp.pi / 6

# Calculate second term: sqrt(3)/8
term2 = mp.sqrt(3) / 8

# Sum both terms for final result
result = term1 + term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))