import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate first term: (2 * pi) / 3
term1 = (2 * mp.pi) / 3

# Calculate second term: 2 * sqrt(3)
term2 = 2 * mp.sqrt(3)

# Sum the two terms
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))