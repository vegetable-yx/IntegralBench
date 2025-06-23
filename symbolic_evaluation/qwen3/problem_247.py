import mpmath as mp
mp.dps = 15

# Calculate the simple fraction 1/8 using mpmath precision
numerator = mp.mpf(1)
denominator = mp.mpf(8)
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))