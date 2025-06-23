import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sin(1) using mpmath's sine function
result = mp.sin(1)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))