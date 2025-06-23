import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate the simple fraction 1/4 using mpmath types
numerator = mp.mpf(1)
denominator = mp.mpf(4)
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))