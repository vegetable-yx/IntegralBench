import mpmath as mp
mp.dps = 15

# Assign the exact integer value from analytical solution
result = 4

# Print result with 10 decimal place formatting
print(mp.nstr(result, n=10))