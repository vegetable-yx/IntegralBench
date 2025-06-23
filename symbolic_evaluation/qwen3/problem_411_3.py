import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the analytical result directly
result = mp.mpf(1)  # Assign the exact value 1 as a high-precision float

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))