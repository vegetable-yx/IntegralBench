import mpmath as mp
mp.dps = 15

# Calculate 21 times pi using high precision
result = 21 * mp.pi

# Print result with 10 decimal places
print(mp.nstr(result, n=10))