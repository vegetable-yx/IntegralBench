import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the numerator (19) and denominator (512) as mpmath floats
numerator = mp.mpf(19)
denominator = mp.mpf(512)

# Compute the coefficient 19/512
coefficient = numerator / denominator

# Multiply by pi constant from mpmath
result = coefficient * mp.pi

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))