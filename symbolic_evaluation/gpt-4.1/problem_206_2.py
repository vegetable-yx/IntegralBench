import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute the constant factor: (1/2) * sqrt(pi) * 2^(-1/4)
sqrt_pi = mp.sqrt(mp.pi)
two_power = mp.power(2, -0.25)  # 2^{-1/4}
outer_factor = 0.5 * sqrt_pi * two_power

# Compute angle pi/8
pi_over_8 = mp.pi / 8

# Compute trigonometric functions at pi/8
cos_pi8 = mp.cos(pi_over_8)
sin_pi8 = mp.sin(pi_over_8)

# Compute ln(2)
ln2 = mp.log(2)

# Compute the expression inside the brackets
term1 = -1.5 * ln2 * cos_pi8  # - (3/2) * ln(2) * cos(pi/8)
term2 = -0.25 * mp.pi * sin_pi8  # - (pi/4) * sin(pi/8)
bracket = term1 + term2

# Combine all parts to get the final result
result = outer_factor * bracket

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))