import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Calculate e raised to the power of pi/4
exp_pi_4 = mp.exp(mp.pi / 4)

# Multiply sqrt(2) by e^(pi/4)
product = sqrt2 * exp_pi_4

# Subtract 1 from the product
numerator = product - 1

# Divide the numerator by 2
result = numerator / 2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))