import mpmath as mp
mp.dps = 15

# Calculate 2 times Catalan's constant
result = 2 * mp.catalan

# Print result with 10 decimal places
print(mp.nstr(result, n=10))