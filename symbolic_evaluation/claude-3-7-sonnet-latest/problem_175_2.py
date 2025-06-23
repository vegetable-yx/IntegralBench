import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate pi
pi_val = mp.pi

# Calculate pi squared
pi_sq = pi_val ** 2

# Compute 2 * pi_sq
two_pi_sq = 2 * pi_sq

# Subtract 3 from 2 * pi_sq
numerator_part = two_pi_sq - 3

# Multiply by pi: pi * (2 * pi_sq - 3)
numerator = pi_val * numerator_part

# Divide by 48 to get final result
result = numerator / 48

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))