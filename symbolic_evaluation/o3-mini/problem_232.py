import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the constant factor: (π * √2) / 4
pi_sqrt2_over4 = (mp.pi * mp.sqrt(2)) / 4

# Compute the hypergeometric function: {}_2F_1(3/2, 3/4; 2; 1/4)
hyp2f1_val = mp.hyp2f1(1.5, 0.75, 2, 0.25)

# Multiply the constant factor by the hypergeometric value
result = pi_sqrt2_over4 * hyp2f1_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))