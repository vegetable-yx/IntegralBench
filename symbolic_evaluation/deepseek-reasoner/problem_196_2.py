import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate each component separately
sqrt3 = mp.sqrt(3)          # √3
pi_sq = mp.pi ** 2          # π²
log3 = mp.log(3)            # Natural logarithm of 3

term1 = sqrt3 / 2           # √3/2
term2 = -1                  # -1
term3 = -pi_sq / 24         # -π²/24
term4 = (mp.pi * sqrt3) / 8 # π√3/8
term5 = (3/16) * log3       # (3/16)ln3

# Combine all terms
result = term1 + term2 + term3 + term4 + term5

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))