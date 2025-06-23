import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Direct assignment of the constant value
result = mp.mpf(17)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))