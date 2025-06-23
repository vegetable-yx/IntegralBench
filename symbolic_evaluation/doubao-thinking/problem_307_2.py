import mpmath as mp
mp.dps = 15

# Calculate Catalan's constant
G = mp.catalan

# Multiply by 2 to get final result
result = 2 * G

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))