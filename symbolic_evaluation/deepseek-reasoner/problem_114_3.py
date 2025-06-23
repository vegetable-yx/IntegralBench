import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the result using mpmath's constant for pi
result = -mp.pi / 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))