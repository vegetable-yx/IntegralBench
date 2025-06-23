import mpmath as mp

# Set the internal decimal precision to 15 to ensure accuracy
mp.dps = 15

# Calculate numerator: 2^19 * 3^4
two_power_19 = mp.power(2, 19)  # 2^19 = 524288
three_power_4 = mp.power(3, 4)   # 3^4 = 81
numerator = two_power_19 * three_power_4

# Calculate denominator: pi^2
pi_squared = mp.power(mp.pi, 2)

# Compute the final result: numerator / denominator
result = numerator / pi_squared

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))