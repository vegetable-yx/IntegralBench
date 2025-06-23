import mpmath as mp
mp.dps = 15

# Define numerator and denominator using arbitrary precision
numerator = mp.mpf(8)
denominator = mp.mpf(7)

# Perform exact rational division with mpmath
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))