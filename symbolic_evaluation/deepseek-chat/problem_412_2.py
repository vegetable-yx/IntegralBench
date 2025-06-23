import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the mathematical constant e to the result
result = mp.e

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))