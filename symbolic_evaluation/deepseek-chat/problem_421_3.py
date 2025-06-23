import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sin(1) radians
result = mp.sin(1)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))