import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi/2
pi_over_2 = mp.pi / 2

# Calculate the square root of pi/2
sqrt_pi_over_2 = mp.sqrt(pi_over_2)

# Calculate the exponent value: 1/8
exponent_val = mp.mpf(1) / 8

# Calculate e^(1/8)
exp_term = mp.exp(exponent_val)

# Multiply the two terms: sqrt(pi/2) * e^(1/8)
result = sqrt_pi_over_2 * exp_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))