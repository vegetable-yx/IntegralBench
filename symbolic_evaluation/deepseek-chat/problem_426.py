import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate each term separately for clarity
# Term 1: constant 1
term1 = mp.mpf(1)

# Term 2: (1/2) * ln(3)
term2 = mp.mpf(0.5) * mp.log(3)

# Term 3: (sqrt(3) * pi) / 6
term3 = (mp.sqrt(3) * mp.pi) / 6

# Sum all terms
result = term1 + term2 + term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))