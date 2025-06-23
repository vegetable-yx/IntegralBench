import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Compute the value of pi
pi_value = mp.pi

# Calculate the result as pi divided by 4
result = pi_value / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))