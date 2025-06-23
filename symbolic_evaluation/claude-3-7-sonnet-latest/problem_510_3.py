import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Compute the first term: 2π / √3
term1 = (2 * mp.pi) / mp.sqrt(3)

# Compute the second term: π / 3
term2 = mp.pi / 3

# Sum the two terms to get the final result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))