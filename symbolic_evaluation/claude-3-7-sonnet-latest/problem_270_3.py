import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi
pi = mp.pi

# Calculate pi cubed
pi_cubed = mp.power(pi, 3)

# Compute 6 * pi
six_pi = 6 * pi

# Combine terms in the numerator: pi^3 + 6*pi - 18
numerator = pi_cubed + six_pi - 18

# Divide by 2304 to get the result
result = numerator / 2304

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))