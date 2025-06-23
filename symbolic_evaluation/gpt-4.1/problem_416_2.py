import mpmath as mp

# Set internal decimal places for sufficient precision
mp.dps = 15

# Calculate e^(π/4)
exp_pi_4 = mp.exp(mp.pi / 4)

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply e^(π/4) by sqrt(2)
product = exp_pi_4 * sqrt_2

# Subtract 1 from the product
numerator = product - 1

# Divide the numerator by 2
result = numerator / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))