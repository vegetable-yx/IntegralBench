import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign pi constant to result
result = mp.pi

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))