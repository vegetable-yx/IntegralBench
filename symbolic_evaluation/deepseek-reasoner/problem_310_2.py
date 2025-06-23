import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/2 directly using mpmath's constant
pi_half = mp.pi / 2

result = pi_half

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))