import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.power(mp.pi, 3)

# Calculate 6 times pi
six_pi = 6 * mp.pi

# Compute the numerator: pi^3 - 6*pi
numerator = pi_cubed - six_pi

# Compute the denominator
denominator = 192

# Final result: (pi^3 - 6*pi) / 192
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))