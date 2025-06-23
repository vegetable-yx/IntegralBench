import mpmath as mp
mp.dps = 15

# Assign the exact solution value
result = mp.mpf(1)

# Print the result with 10 decimal place precision
print(mp.nstr(result, n=10))