import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Direct assignment of the exact solution
result = mp.mpf(7)

# Print result with exactly 10 decimal places precision
print(mp.nstr(result, n=10))