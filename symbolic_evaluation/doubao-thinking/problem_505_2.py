import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi from mpmath constant
pi_value = mp.pi

# Compute the result as pi divided by 4
result = pi_value / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))