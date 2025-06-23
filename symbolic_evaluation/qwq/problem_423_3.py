import mpmath as mp
mp.dps = 15

# Direct value assignment for simple integer result
result = mp.mpf(99)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))