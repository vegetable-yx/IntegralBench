import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the numerical value of 3π/8
numerator = 3
denominator = 8
pi_constant = mp.pi  # Get mpmath's high-precision π value

result = (numerator / denominator) * pi_constant

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))