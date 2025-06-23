import mpmath as mp

# Set the internal decimal precision to 15
mp.dps = 15

# Calculate 506 times pi
result = 506 * mp.pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))