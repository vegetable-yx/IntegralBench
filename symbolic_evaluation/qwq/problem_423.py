import mpmath as mp
mp.dps = 15

# Direct assignment of the exact integer result
result = mp.mpf(99)

# Print the result with 10 decimal place formatting
print(mp.nstr(result, n=10))