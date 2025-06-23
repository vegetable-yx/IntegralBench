import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator as arbitrary-precision floats
numerator = mp.mpf(4)
denominator = mp.mpf(5)

# Perform exact division using mpmath
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))