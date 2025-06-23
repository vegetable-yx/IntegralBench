import mpmath as mp
mp.dps = 15

# Calculate the numerator and denominator
numerator = mp.mpf(1)
denominator = mp.mpf(2)

# Compute the result of 1/2
result = numerator / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))