import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the value of π/4
result = mp.pi / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))