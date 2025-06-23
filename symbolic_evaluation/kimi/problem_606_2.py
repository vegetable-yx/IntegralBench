import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi/2 directly
result = mp.pi / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))