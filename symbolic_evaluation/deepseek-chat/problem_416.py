import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π/4
pi_over_4 = mp.pi / 4

# Compute e raised to the power of π/4
exp_pi_over_4 = mp.exp(pi_over_4)

# Compute square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply e^(π/4) by √2
product = exp_pi_over_4 * sqrt_2

# Subtract 1 from the product
numerator = product - 1

# Divide by 2 to get the final result
result = numerator / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))