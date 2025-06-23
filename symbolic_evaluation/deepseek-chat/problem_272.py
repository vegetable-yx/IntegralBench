import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate each term of the analytical expression
# term1 = π²/16
term1 = mp.pi**2 / 16

# term2 = -π*ln(2)/8
term2 = - (mp.pi * mp.ln(2)) / 8

# term3 = -Catalan/2 (Catalan's constant)
term3 = - mp.catalan / 2

# term4 = π*ln(2 + √2)/16
# First compute √2
sqrt2 = mp.sqrt(2)
# Then compute 2 + √2
inner = 2 + sqrt2
term4 = (mp.pi * mp.ln(inner)) / 16

# term5 = √2/4
term5 = sqrt2 / 4

# term6 = -1
term6 = -1

# Sum all terms
result = term1 + term2 + term3 + term4 + term5 + term6

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))