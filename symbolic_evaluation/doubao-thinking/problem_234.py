import mpmath as mp
mp.dps = 15

# Direct value assignment for simple constant result
result = mp.mpf(2)

# Print result with 10 decimal place formatting
print(mp.nstr(result, n=10))