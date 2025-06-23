import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the value of pi
pi_value = mp.pi

# Compute the result: -pi/2
result = -pi_value / 2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))