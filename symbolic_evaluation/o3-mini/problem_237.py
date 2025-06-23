import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate 3 raised to the power of 5/4
base = mp.mpf(3)
exponent = mp.mpf(5)/mp.mpf(4)  # Exponent 5/4 = 1.25
term = base ** exponent  # 3^(5/4)

# Compute denominator: 2 * 3^(5/4)
denominator = mp.mpf(2) * term

# Compute numerator: 13 * pi
numerator = mp.mpf(13) * mp.pi

# Final result: (13 * pi) / (2 * 3^(5/4))
result = numerator / denominator

# Print result rounded to 10 decimal places
print(mp.nstr(result, n=10))