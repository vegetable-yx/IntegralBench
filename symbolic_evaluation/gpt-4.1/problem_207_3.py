import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute 2^(-1/4) using exponentiation
exponent_factor = mp.power(2, -0.25)

# Compute angle for sine function: π/8
angle = mp.pi / 8

# Calculate sin(π/8)
sine_value = mp.sin(angle)

# Multiply by π/2
pi_factor = mp.pi / 2

# Combine all factors: (π/2) * 2^(-1/4) * sin(π/8)
result = pi_factor * exponent_factor * sine_value

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))