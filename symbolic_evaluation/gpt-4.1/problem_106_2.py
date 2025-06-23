import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the result: π/2
result = mp.pi / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))