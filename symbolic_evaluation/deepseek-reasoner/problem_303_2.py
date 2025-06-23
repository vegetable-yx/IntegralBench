import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate each term of the expression separately
# Term 1: π² / 64
term1 = mp.pi**2 / 64

# Term 2: -√3 * π / 32
term2 = -(mp.sqrt(3) * mp.pi) / 32

# Term 3: (15/32) * ln(5)
term3 = (15 / 32) * mp.log(5)

# Term 4: -(15/64) * ln(15)
term4 = -(15 / 64) * mp.log(15)

# Sum all terms to get the final result
result = term1 + term2 + term3 + term4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))