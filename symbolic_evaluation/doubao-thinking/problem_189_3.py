import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate π/4 directly using mpmath's constant for pi
result = mp.pi / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))