import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate each component separately
pi_cubed = mp.pi ** 3
term1 = pi_cubed / 144  # π³/144 calculation

term2 = mp.pi / 16      # π/16 calculation

sqrt3 = mp.sqrt(3)      # Pre-calculate √3
term3 = (mp.pi * sqrt3) / 24  # π√3/24 calculation

# Combine all terms
result = term1 - term2 + term3

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))