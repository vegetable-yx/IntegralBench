import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sine of 1 radian
result = mp.sin(1)

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))