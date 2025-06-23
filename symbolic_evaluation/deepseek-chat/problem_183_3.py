import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Add 2 to the square root of 5
sum_val = 2 + sqrt5

# Compute the natural logarithm of (2 + sqrt(5))
log_val = mp.log(sum_val)

# Compute pi divided by 4
pi_over_4 = mp.pi / 4

# Multiply pi/4 by the logarithm to get the result
result = pi_over_4 * log_val

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))