import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate each component separately
pi_sqrt3 = mp.pi * mp.sqrt(3)  # π * √3
pi_sq = mp.pi ** 2             # π²

# Compute individual terms
term1 = pi_sqrt3 / 16          # (π√3)/16
term2 = -pi_sq / 48            # -π²/48
term3 = -mp.mpf(1)/32          # -1/32

# Combine all terms
result = term1 + term2 + term3

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))