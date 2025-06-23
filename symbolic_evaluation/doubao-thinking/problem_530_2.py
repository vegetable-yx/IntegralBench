import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# The analytical result is exactly 1
result = mp.mpf(1)  # Convert integer 1 to mpmath floating-point type

# Print the result with 10 decimal places of precision
print(mp.nstr(result, n=10))