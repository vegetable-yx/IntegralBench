import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate numerator and denominator as mpmath floating-point numbers
numerator = mp.mpf(128)
denominator = mp.mpf(153)

# Perform exact division using mpmath
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))