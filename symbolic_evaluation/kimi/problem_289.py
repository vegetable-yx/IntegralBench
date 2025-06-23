import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the result: π/4
result = mp.pi / 4

# Output the result to 10 decimal places
print(mp.nstr(result, n=10))