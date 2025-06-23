import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate sin(1) using mpmath's sine function
result = mp.sin(1)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))