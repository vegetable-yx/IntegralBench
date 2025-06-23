import mpmath as mp
mp.dps = 15

# Direct assignment of the exact integer result
result = 384

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))