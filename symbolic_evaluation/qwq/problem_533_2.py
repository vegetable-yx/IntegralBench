import mpmath as mp
mp.dps = 15  # Calculate numerator and denominator as high-precision floats
numerator = mp.mpf(8)
denominator = mp.mpf(7)

# Perform exact division using mpmath
result = numerator / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))