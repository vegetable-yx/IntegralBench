import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sqrt(2) using mpmath's square root function
sqrt2 = mp.sqrt(2)

# Calculate pi/4 using mpmath's constant
pi_over_4 = mp.pi / 4

# Compute e^(pi/4) using mpmath's exponential function
exp_pi_over4 = mp.exp(pi_over_4)

# Multiply sqrt(2) by e^(pi/4)
sqrt2_times_exp = sqrt2 * exp_pi_over4

# Subtract 1 from the product
numerator = sqrt2_times_exp - 1

# Divide by 2 to get the final result
result = numerator / 2

# Print the result with 10 decimal places using mpmath's number string function
print(mp.nstr(result, n=10))