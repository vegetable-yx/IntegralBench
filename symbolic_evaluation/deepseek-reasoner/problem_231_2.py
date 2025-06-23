import mpmath as mp
mp.dps = 15

# Calculate square root of 2 using mpmath's sqrt function
result = mp.sqrt(2)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))