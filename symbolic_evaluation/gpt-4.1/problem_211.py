import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi/2
pi_over_2 = mp.pi / 2

# Compute sqrt(2/pi)
sqrt_2_over_pi = mp.sqrt(2 / mp.pi)

# Compute sin(1) and cos(1)
sin_1 = mp.sin(1)
cos_1 = mp.cos(1)

# Sum sin(1) + cos(1)
sin_plus_cos = sin_1 + cos_1

# Multiply the components: (pi/2) * sqrt(2/pi) * (sin(1) + cos(1))
result = pi_over_2 * sqrt_2_over_pi * sin_plus_cos

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))