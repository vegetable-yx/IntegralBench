import mpmath as mp
mp.dps = 15  # Set internal precision

# Direct assignment of the exact integer solution
result = mp.mpf(17)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))