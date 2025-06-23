import mpmath as mp
# Set precision to 15 decimal places
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute the result as -pi/2
result = -pi_value / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))