import mpmath as mp
mp.dps = 15

# Calculate the simple fraction 1/2 using mpmath precision
result = mp.mpf(1)/2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))