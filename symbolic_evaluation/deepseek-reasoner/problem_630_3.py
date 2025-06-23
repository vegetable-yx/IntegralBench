import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the natural logarithm of 3
ln_3 = mp.log(3)

# Calculate the numerator: π * ln(3)
pi_times_ln3 = mp.pi * ln_3

# Calculate the denominator: 12 * sqrt(3)
sqrt_3 = mp.sqrt(3)
denominator = 12 * sqrt_3

# Compute the final result by dividing numerator by denominator
result = pi_times_ln3 / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))