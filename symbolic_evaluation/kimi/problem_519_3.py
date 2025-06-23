import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute pi/4: divide the constant pi by 4
pi_val = mp.pi
denominator = 4
result = pi_val / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))