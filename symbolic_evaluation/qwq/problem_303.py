import mpmath as mp
mp.dps = 15

# Direct assignment of the numerical value
result = mp.mpf('0.0211456')

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))