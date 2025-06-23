import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the first term: -1/2
term1 = mp.mpf(-1)/2

# Calculate the second term: -π/8
term2 = -mp.pi / 8

# Sum both terms to get the final result
result = term1 + term2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))