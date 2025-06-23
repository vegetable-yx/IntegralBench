import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate the constant pi
pi_val = mp.pi

# Compute pi/2
pi_over_2 = pi_val / 2

# Subtract from 2 to get the final result
result = 2 - pi_over_2

# Output the result to 10 decimal places
print(mp.nstr(result, n=10))