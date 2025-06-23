import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute the final result as pi divided by 16
result = pi_value / 16

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))