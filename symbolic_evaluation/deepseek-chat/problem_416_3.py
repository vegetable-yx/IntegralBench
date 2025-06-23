import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi/4
pi_over_4 = mp.pi / 4

# Compute e^(pi/4)
exp_pi_4 = mp.exp(pi_over_4)

# Compute sqrt(2)
sqrt_2 = mp.sqrt(2)

# Multiply sqrt(2) by e^(pi/4)
product_term = sqrt_2 * exp_pi_4

# Subtract 1 from the product
bracket_term = product_term - 1

# Multiply by 17/40
result = (mp.mpf(17)/40) * bracket_term

# Print result to 10 decimal places
print(mp.nstr(result, n=10))