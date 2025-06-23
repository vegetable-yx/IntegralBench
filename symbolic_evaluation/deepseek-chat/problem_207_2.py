import mpmath as mp

# Set internal precision to 15 decimal places for accuracy
mp.dps = 15

# Calculate the constant factor: sqrt(pi/2)
pi_half = mp.pi / 2
sqrt_pi_half = mp.sqrt(pi_half)

# Calculate arctan(1/2)
atan_val = mp.atan(0.5)

# Multiply the two components
result = sqrt_pi_half * atan_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))