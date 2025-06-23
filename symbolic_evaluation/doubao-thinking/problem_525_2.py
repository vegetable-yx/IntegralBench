import mpmath as mp
mp.dps = 15

# Calculate the exact fraction 1/2 using arbitrary precision
numerator = mp.mpf(1)
denominator = mp.mpf(2)
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))