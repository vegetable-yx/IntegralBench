import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi/2: we use mp.pi and divide by 2
result = mp.pi / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))