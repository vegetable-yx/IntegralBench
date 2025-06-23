import mpmath as mp
mp.dps = 15

# Calculate the exact fraction using mpmath precision
numerator = mp.mpf(-1)
denominator = mp.mpf(3)
result = numerator / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))