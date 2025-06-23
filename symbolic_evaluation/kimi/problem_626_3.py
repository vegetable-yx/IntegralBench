import mpmath as mp
mp.dps = 15

# Calculate Euler-Mascheroni constant using built-in mpmath constant
result = mp.euler

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))