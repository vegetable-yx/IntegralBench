import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate each term of the closed-form solution separately

# Term 1: π² / 64
term1 = mp.power(mp.pi, 2) / 64

# Term 2: -π / 16
term2 = -mp.pi / 16

# Term 3: 1/16
term3 = mp.mpf(1) / 16

# Term 4: -(π/64) * ln(2 + √2)
# Compute inner expression: 2 + sqrt(2)
sqrt2 = mp.sqrt(2)
inner4 = 2 + sqrt2
term4 = -(mp.pi / 64) * mp.log(inner4)

# Term 5: (1/16) * ln(1 + √2)
inner5 = 1 + sqrt2
term5 = (mp.mpf(1)/16) * mp.log(inner5)

# Sum all terms
result = term1 + term2 + term3 + term4 + term5

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))