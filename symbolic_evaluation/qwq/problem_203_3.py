import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute Struve functions at z=1
H0_1 = mp.struveh(0, 1)  # Struve H_0(1)
H1_1 = mp.struveh(1, 1)  # Struve H_1(1)

# Calculate individual components of the expression
term1 = mp.pi * H0_1          # π * H_0(1)
term2 = 2 * mp.pi * H1_1      # 2π * H_1(1)
term3 = mp.mpf(2)/3           # 2/3 term

# Combine all terms to get final result
result = term1 - term2 + term3

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))