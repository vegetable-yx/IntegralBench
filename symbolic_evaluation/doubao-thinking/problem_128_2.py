import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Direct assignment of the exact solution
result = mp.mpf(2)

# Print result with 10 decimal places using mpmath's nstr function
print(mp.nstr(result, n=10))