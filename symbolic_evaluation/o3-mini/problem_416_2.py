import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Calculate pi/4
pi_over_4 = mp.pi / 4

# Calculate exponential of pi/4
exp_pi4 = mp.exp(pi_over_4)

# Multiply sqrt(2) by exp(pi/4)
product = sqrt2 * exp_pi4

# Subtract 1 from the product
numerator = product - 1

# Divide by 2 to get the final result
result = numerator / 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))