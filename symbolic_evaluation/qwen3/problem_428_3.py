import mpmath as mp
mp.dps = 15

# Direct assignment of the exact integer solution
result = mp.mpf(17)

# Print the result with 10 decimal place formatting
print(mp.nstr(result, n=10))