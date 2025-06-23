import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sin(1) using mpmath's sin function
result = mp.sin(1)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))