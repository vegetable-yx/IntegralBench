import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sqrt(2)
sqrt_2 = mp.sqrt(2)

# Calculate e^(pi/4)
exp_pi_over_4 = mp.exp(mp.pi / 4)

# Multiply sqrt(2) by e^(pi/4)
numerator_part = sqrt_2 * exp_pi_over_4

# Subtract 1 from the product
numerator = numerator_part - 1

# Divide the result by 2 to get the final value
result = numerator / 2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))