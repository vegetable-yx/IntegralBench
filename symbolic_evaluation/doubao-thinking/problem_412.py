import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# The mathematical constant e is directly available in mpmath
result = mp.e

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))