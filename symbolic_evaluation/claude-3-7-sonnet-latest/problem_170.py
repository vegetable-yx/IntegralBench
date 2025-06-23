import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate the value of pi
pi_val = mp.pi

# Compute the square of pi
pi_squared = pi_val ** 2

# Divide pi squared by 2 to get the result
result = pi_squared / 2

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))