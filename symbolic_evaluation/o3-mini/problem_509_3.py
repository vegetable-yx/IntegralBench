import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the first term: (2 * pi) / 3
term1 = (2 * mp.pi) / 3

# Calculate the second term: 4 * sqrt(3)
term2 = 4 * mp.sqrt(3)

# Sum the two terms
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))