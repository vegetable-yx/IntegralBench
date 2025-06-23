import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sin(1) using mpmath's sin function
angle = 1
result = mp.sin(angle)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))