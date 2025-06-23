import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate the result directly using mpmath's pi constant
result = -mp.pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))