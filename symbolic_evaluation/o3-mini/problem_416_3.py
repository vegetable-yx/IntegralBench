import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute pi/4
pi_over_4 = mp.pi / 4

# Evaluate e^(pi/4)
exp_val = mp.exp(pi_over_4)

# Multiply sqrt(2) by e^(pi/4)
numerator_part = sqrt2 * exp_val

# Subtract 1 to get the numerator
numerator = numerator_part - 1

# Divide by 2 to get the final result
result = numerator / 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))