import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π^3
pi_cubed = mp.pi ** 3

# Compute first term: π³/768
term1 = pi_cubed / 768

# Compute second term: π/64
term2 = mp.pi / 64

# Compute third term: 1/32 (using mpmath type for precision)
term3 = mp.mpf(1) / 32

# Combine all terms
result = term1 - term2 + term3

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))