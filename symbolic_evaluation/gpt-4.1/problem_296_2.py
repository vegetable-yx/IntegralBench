import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate Catalan's constant
catalan = mp.catalan

# Calculate 2 times Catalan's constant
two_g = 2 * catalan

# Calculate pi divided by 2
pi_over_2 = mp.pi / 2

# Compute the result: 2G - π/2
result = two_g - pi_over_2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))