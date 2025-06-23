import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Compute the value of π/3
result = mp.pi / 3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))