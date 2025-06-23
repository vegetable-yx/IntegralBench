import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the analytical result directly
result = mp.mpf(113)  # Convert integer 113 to mpmath floating-point

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))