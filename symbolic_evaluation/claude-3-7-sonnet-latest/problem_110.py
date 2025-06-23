import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the value of pi/4
result = mp.pi / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))