import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate the constant: (3 * pi) / 16
result = (3 * mp.pi) / 16

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))