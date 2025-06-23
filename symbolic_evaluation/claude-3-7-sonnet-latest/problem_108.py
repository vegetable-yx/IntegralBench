import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the numerator: 2 * sqrt(2) * pi
# Step 1: Compute sqrt(2) using mpmath
sqrt2 = mp.sqrt(2)

# Step 2: Multiply 2 * sqrt(2) * pi
numerator = 2 * sqrt2 * mp.pi

# Denominator is 3
denominator = 3

# Final result: numerator divided by denominator
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))