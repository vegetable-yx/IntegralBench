import mpmath as mp
mp.dps = 15

# Direct assignment of zero result
result = mp.mpf(0)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))