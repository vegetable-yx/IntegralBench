import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant factor: 27/4
factor = mp.mpf(27) / 4

# Multiply by pi to get the result
result = factor * mp.pi

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))