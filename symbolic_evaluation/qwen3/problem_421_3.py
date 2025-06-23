import mpmath as mp
mp.dps = 15

# Calculate sin(1) using mpmath's sin function
result = mp.sin(1)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))