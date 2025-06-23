import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/4 directly using mpmath's constant for pi
pi_value = mp.pi
result = pi_value / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))