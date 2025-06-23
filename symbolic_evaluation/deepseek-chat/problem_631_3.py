import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate sin(1) in radians
result = mp.sin(1)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))