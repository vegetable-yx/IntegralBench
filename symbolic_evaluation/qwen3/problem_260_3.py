import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate π/2
pi_half = mp.pi / 2

# Calculate Struve H function H₀(1)
struve_h0 = mp.struveh(0, 1)

# Multiply components to get final result
result = pi_half * struve_h0

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))