import mpmath as mp

# Set precision to 15 decimal places
mp.dps = 15

# Calculate pi to the third power
pi_cubed = mp.pi ** 3

# Multiply by 3 for numerator
numerator = 3 * pi_cubed

# Calculate the square root of 3
sqrt_3 = mp.sqrt(3)

# Multiply by 8 for denominator
denominator = 8 * sqrt_3

# Divide numerator by denominator
result = numerator / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))