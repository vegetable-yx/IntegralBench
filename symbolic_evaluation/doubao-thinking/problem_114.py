import mpmath as mp

# Set internal precision to 15 decimal places for accurate calculations
mp.dps = 15

# Calculate the negative of pi divided by 2
result = -mp.pi / 2

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))