import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate each term of the expression separately
# Term 1: π²/48
term1 = mp.pi**2 / 48

# Term 2: -π√3/8
term2 = - (mp.pi * mp.sqrt(3)) / 8

# Term 3: 1/4
term3 = mp.mpf(1)/4

# Term 4: (3 * ln(3)) / 16
term4 = (3 * mp.log(3)) / 16

# Sum all terms to get final result
result = term1 + term2 + term3 + term4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))