import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π
pi_val = mp.pi

# Square π
pi_squared = pi_val ** 2

# Divide by 4
result = pi_squared / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))