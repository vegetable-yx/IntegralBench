import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the result using the analytical expression π/8
result = mp.pi / 8

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))