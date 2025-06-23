import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the result directly using mpmath's constant for pi
result = -mp.pi

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))