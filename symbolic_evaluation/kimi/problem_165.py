import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/2
pi_over_2 = mp.pi / 2

# Calculate e^(-2)
exp_neg2 = mp.exp(-2)

# Multiply the components together
result = pi_over_2 * exp_neg2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))