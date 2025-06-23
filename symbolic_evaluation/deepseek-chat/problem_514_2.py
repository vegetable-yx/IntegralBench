import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute pi/6 term
term1 = mp.pi / 6

# Compute sqrt(3)/8 term
sqrt3 = mp.sqrt(3)
term2 = sqrt3 / 8

# Sum the two terms
result = term1 + term2

# Print final result to 10 decimal places
print(mp.nstr(result, n=10))