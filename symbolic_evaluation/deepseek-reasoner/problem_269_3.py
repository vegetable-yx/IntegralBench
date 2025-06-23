import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate each term of the expression separately
term1 = mp.pi**3 / 144          # π³/144
term2 = -(mp.pi**2 * mp.sqrt(3)) / 24  # -π²√3/24
term3 = mp.pi / 8               # π/8
term4 = mp.mpf(1)/4             # 1/4

# Sum all components to get final result
result = term1 + term2 + term3 + term4

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))