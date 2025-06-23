import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π/8 directly using mpmath's constant for pi
result = mp.pi / 8

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))