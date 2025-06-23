import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π^4
pi_power4 = mp.pi ** 4

# Divide by 64 to get final result
result = pi_power4 / 64

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))