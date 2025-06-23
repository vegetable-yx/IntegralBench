import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate numerator and denominator using high-precision floats
numerator = mp.mpf(8)
denominator = mp.mpf(7)

# Perform exact division using mpmath
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))