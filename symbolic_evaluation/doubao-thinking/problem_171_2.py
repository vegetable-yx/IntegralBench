import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the numerator (π) and denominator (192)
numerator = mp.pi
denominator = 192

# Compute the final result as π divided by 192
result = numerator / denominator

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))