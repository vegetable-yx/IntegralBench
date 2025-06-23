import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute pi constant using mpmath
pi_val = mp.pi

# Calculate pi divided by 2
pi_over_2 = pi_val / 2

# Subtract from 2
result = 2 - pi_over_2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))