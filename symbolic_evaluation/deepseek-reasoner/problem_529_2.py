import mpmath as mp
mp.dps = 15

# Calculate the result directly using mpmath's pi constant
result = -mp.pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))