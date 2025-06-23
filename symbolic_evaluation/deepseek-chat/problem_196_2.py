import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate each term of the expression separately for clarity
# Term 1: π/8
term1 = mp.pi / 8

# Term 2: -1/4
term2 = -1 / mp.mpf(4)

# Term 3: -π√3/24
# First compute √3
sqrt3 = mp.sqrt(3)
term3 = - (mp.pi * sqrt3) / 24

# Term 4: (3/8) * ln(3)
ln3 = mp.log(3)
term4 = (3 / mp.mpf(8)) * ln3

# Sum all terms to get the final result
result = term1 + term2 + term3 + term4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))