import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the value of pi
pi_val = mp.pi

# Compute the value of pi divided by 2
pi_over_2 = pi_val / 2

# Compute the natural logarithm of pi/2
result = mp.log(pi_over_2)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))