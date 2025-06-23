import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π/6
term1 = mp.pi / 6

# Compute √3
sqrt3 = mp.sqrt(3)

# Compute √3 / 8
term2 = sqrt3 / 8

# Sum the two terms
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))