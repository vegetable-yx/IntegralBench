import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate sqrt(2)
sqrt_2 = mp.sqrt(2)

# Calculate e^(pi/4)
exp_pi4 = mp.exp(mp.pi/4)

# Multiply sqrt(2) and e^(pi/4)
sqrt2_times_exp = sqrt_2 * exp_pi4

# Subtract 1 from the product
numerator = sqrt2_times_exp - 1

# Divide by 2 to get final result
result = numerator / 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))