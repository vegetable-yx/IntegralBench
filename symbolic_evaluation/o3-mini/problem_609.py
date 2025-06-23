import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant pi
pi_val = mp.pi

# Compute half of pi
half_pi = pi_val / 2

# Subtract half_pi from 1
result = 1 - half_pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))