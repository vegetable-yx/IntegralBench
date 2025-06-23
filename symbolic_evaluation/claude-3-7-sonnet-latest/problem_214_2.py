import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sin(1.0)
result = mp.sin(1.0)

# Print result to 10 decimal places
print(mp.nstr(result, n=10))