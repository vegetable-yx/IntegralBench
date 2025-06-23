import mpmath as mp

# Set the internal decimal precision to 15
mp.dps = 15

# Calculate pi cubed
pi_val = mp.pi
pi_cubed = pi_val**3

# Divide by 32
denominator = 32
result = pi_cubed / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))