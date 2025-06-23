import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi*sqrt(pi) = pi^(3/2)
pi_sqrt_pi = mp.power(mp.pi, mp.mpf(3)/2)

# Calculate denominator: 2^(5/4)
denom = mp.power(2, mp.mpf(5)/4)

# Calculate the fraction: (pi*sqrt(pi)) / (2^(5/4))
fraction = pi_sqrt_pi / denom

# Calculate angle for cosine: π/8
angle = mp.pi / 8

# Calculate cosine of the angle
cos_term = mp.cos(angle)

# Multiply fraction by cosine term
result = fraction * cos_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))