import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the value of π
pi_val = mp.pi

# Square π to get π²
pi_squared = mp.power(pi_val, 2)

# Divide π² by 4 to obtain the result
result = pi_squared / 4

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))