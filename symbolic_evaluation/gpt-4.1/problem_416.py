import mpmath as mp

# Set internal precision to 15 decimal places for reliable 10-digit output
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Divide by 2 to get √2/2
sqrt2_over_2 = sqrt2 / 2

# Compute π/4
pi_over_4 = mp.pi / 4

# Calculate e^(π/4)
exp_pi4 = mp.exp(pi_over_4)

# Multiply √2/2 by e^(π/4)
product = sqrt2_over_2 * exp_pi4

# Subtract 1/2 from the product
result = product - 0.5

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))