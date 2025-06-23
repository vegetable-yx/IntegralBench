import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Get the mathematical constant π
pi_val = mp.pi

# Compute π squared
pi_squared = pi_val ** 2

# Divide π squared by 4 to get the result
result = pi_squared / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))