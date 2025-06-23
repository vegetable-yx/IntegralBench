import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute pi/2
half_pi = mp.pi / 2

# Compute sqrt(pi/2)
sqrt_half_pi = mp.sqrt(half_pi)

# Compute the exponent: 1/8
exponent = mp.mpf(1) / 8

# Compute e^(1/8)
exp_term = mp.exp(exponent)

# Multiply the two parts
result = sqrt_half_pi * exp_term

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))