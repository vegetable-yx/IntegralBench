import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate each component of the expression
term1 = mp.sqrt(2) * mp.pi**2 / 8
term2 = mp.log(3) / 4
term3 = mp.asin(mp.sqrt(0.75))
term4 = mp.ellipe(0.6) * mp.struveh(1, 2.5)

# Combine all terms to get final result
result = (term1 - term2) * term3 + term4

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))