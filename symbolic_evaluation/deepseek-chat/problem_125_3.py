import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the analytical expression: (3 * pi) / 16
numerator = mp.mpf(3) * mp.pi
result = numerator / mp.mpf(16)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))