import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π^4
pi_power4 = mp.pi ** 4

# Multiply by 35/256 coefficient
result = (35 * pi_power4) / 256

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))