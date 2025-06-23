import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π^3
pi_cubed = mp.pi ** 3

# Divide by 600 to get the final result
result = pi_cubed / 600

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))