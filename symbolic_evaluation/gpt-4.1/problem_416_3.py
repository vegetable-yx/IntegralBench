import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sqrt(2) and divide by 2
sqrt2_over_2 = mp.sqrt(2) / 2

# Calculate pi/4
pi_over_4 = mp.pi / 4

# Compute e^(pi/4)
exp_pi_4 = mp.exp(pi_over_4)

# Multiply the two components: (sqrt(2)/2) * e^(pi/4)
product = sqrt2_over_2 * exp_pi_4

# Subtract 1/2 from the product
result = product - 0.5

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))