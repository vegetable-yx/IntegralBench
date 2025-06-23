import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π^3
pi_cubed = mp.pi ** 3

# Calculate first term: π³/288
term1 = pi_cubed / 288

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Calculate second term: (π * √3)/48
term2 = (mp.pi * sqrt3) / 48

# Calculate third term: 1/16
term3 = mp.mpf(1)/16

# Combine all terms
result = term1 - term2 + term3

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))