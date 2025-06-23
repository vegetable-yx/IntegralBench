import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate the components of the expression
pi_value = mp.pi
sqrt_3 = mp.sqrt(3)

# Compute denominator: 3 * sqrt(3)
denominator = 3 * sqrt_3

# Compute numerator: 7 * pi
numerator = 7 * pi_value

# Calculate final result: (7π) / (3√3)
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))