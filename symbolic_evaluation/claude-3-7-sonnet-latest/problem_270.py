import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi cubed
pi_cubed = mp.pi ** 3

# Calculate each term of the expression separately
term1 = pi_cubed / 1536    # π³/1536
term2 = -mp.pi / 384       # -π/384
term3 = mp.mpf(1) / 192    # 1/192

# Combine all terms
result = term1 + term2 + term3

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))