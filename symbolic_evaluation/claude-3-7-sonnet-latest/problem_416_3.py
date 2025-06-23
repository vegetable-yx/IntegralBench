import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Calculate pi/4
pi_over_4 = mp.pi / 4

# Compute e^(pi/4)
exp_term = mp.exp(pi_over_4)

# Multiply sqrt(2) by e^(pi/4)
product = sqrt2 * exp_term

# Subtract 1 from the product
numerator = product - 1

# Divide by 2 to get the final result
result = numerator / 2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))