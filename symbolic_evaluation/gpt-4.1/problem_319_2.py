import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the analytical solution
result = mp.mpf(1)  # Convert integer 1 to mpmath floating-point format

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))