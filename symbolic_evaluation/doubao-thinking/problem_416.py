import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate e^(π/4)
exp_pi_over_4 = mp.exp(mp.pi / 4)

# Multiply by sqrt(2)
sqrt2_times_exp = exp_pi_over_4 * mp.sqrt(2)

# Subtract 1 from the result
numerator = sqrt2_times_exp - 1

# Divide by 2 to get the final result
result = numerator / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))