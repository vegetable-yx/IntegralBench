import mpmath as mp
mp.dps = 15

# Calculate pi using mpmath's built-in constant
result = mp.pi

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))