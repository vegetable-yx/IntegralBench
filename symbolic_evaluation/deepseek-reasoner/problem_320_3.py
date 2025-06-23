import mpmath as mp
mp.dps = 15

# Calculate pi constant using mpmath's built-in constant
result = mp.pi

# Print result with 10 decimal place precision
print(mp.nstr(result, n=10))