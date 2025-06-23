import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π/2 directly using mpmath's constant for π
result = mp.pi / 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))