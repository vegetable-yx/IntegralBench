import mpmath as mp
mp.dps = 15  # Set internal decimal places for high precision

# Calculate square root of 2
sqrt_two = mp.sqrt(2)

# Compute 2 times square root of 2 for denominator
denominator = 2 * sqrt_two

# Calculate final result using exact formula: -π/(2√2)
result = -mp.pi / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))