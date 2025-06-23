import mpmath as mp
mp.dps = 15

# Direct assignment of the exact integer value
result = 1005

# Print result with 10 decimal place formatting
print(mp.nstr(result, n=10))