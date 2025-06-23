import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/4 directly using mpmath's constant
pi_value = mp.pi
result = pi_value / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))